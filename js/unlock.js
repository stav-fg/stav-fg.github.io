// Decrypts what tools/lock_cases.py locked: a case study, or the project list on the home page.
// PBKDF2-SHA256 to an AES-256-GCM key; every blob is a 12-byte iv followed by the ciphertext.
// A correct password is remembered for the browser session: as this page's derived key, and as
// the password itself, so the other pages open without asking again.
(function () {
  var root = document.documentElement;
  var form = document.querySelector('.gate');
  var holder = document.getElementById('locked');
  function showForm() { root.classList.remove('unlocking'); }
  if (!form || !holder || !window.crypto || !crypto.subtle) { showForm(); return; }

  var keyStore = 'unlock:' + form.dataset.slug;
  var pwStore = 'unlock:pw';
  var payload = JSON.parse(holder.textContent);
  var msg = form.querySelector('.gate-msg');

  function bytes(b64) {
    var s = atob(b64), out = new Uint8Array(s.length);
    for (var i = 0; i < s.length; i++) out[i] = s.charCodeAt(i);
    return out;
  }
  function toB64(buf) {
    var s = '', b = new Uint8Array(buf);
    for (var i = 0; i < b.length; i++) s += String.fromCharCode(b[i]);
    return btoa(s);
  }
  function saved(name) {
    try { return sessionStorage.getItem(name); } catch (e) { return null; }
  }
  function save(name, value) {
    try { sessionStorage.setItem(name, value); } catch (e) { /* fine without it */ }
  }
  function open(key, blob) {
    return crypto.subtle.decrypt({ name: 'AES-GCM', iv: blob.slice(0, 12) }, key, blob.slice(12));
  }
  function derive(password) {
    return crypto.subtle.importKey('raw', new TextEncoder().encode(password), 'PBKDF2', false, ['deriveKey'])
      .then(function (base) {
        return crypto.subtle.deriveKey(
          { name: 'PBKDF2', salt: bytes(payload.salt), iterations: payload.rounds, hash: 'SHA-256' },
          base, { name: 'AES-GCM', length: 256 }, true, ['decrypt']);
      });
  }

  // On a case study, `hero` goes where the form was and `body` after the section the form was in.
  // On the home page the project list takes the place of the whole "Selected work" sign-in section.
  function reveal(key, page) {
    var gate = form.closest('.work-gate');
    if (gate) {
      gate.outerHTML = page.body;
    } else {
      var section = form.closest('.case-hero, .intro');
      var column = form.parentElement;
      form.remove();
      if (page.hero) column.insertAdjacentHTML('beforeend', page.hero);
      section.insertAdjacentHTML('afterend', page.body);
    }
    document.querySelectorAll('img[data-locked]').forEach(function (img) {
      fetch(img.dataset.locked)
        .then(function (r) { return r.arrayBuffer(); })
        .then(function (buf) { return open(key, new Uint8Array(buf)); })
        .then(function (plain) { img.src = URL.createObjectURL(new Blob([plain], { type: img.dataset.type })); });
    });
    showForm();
  }

  function tryKey(key) {
    return open(key, bytes(payload.data)).then(function (plain) {
      reveal(key, JSON.parse(new TextDecoder().decode(plain)));
      return key;
    });
  }
  function remember(key, password) {
    if (password) save(pwStore, password);
    return crypto.subtle.exportKey('raw', key).then(function (raw) { save(keyStore, toB64(raw)); });
  }

  // Signed in earlier in this session: on this page, or on another one with the same password.
  var key = saved(keyStore), password = saved(pwStore);
  (key ? crypto.subtle.importKey('raw', bytes(key), 'AES-GCM', true, ['decrypt']).then(tryKey)
       : Promise.reject())
    .catch(function () {
      if (!password) throw new Error('not signed in');
      return derive(password).then(tryKey).then(remember);
    })
    .catch(showForm);

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    var button = form.querySelector('button');
    var typed = form.pw.value;
    button.disabled = true;
    msg.textContent = 'Checking…';
    derive(typed)
      .then(tryKey)
      .then(function (k) { return remember(k, typed); })
      .catch(function () {
        msg.textContent = "That password didn't work. Try again.";
        button.disabled = false;
        form.pw.select();
      });
  });
})();
