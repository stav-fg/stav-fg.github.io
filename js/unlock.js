// Decrypts a case study page built by tools/lock_cases.py.
// PBKDF2-SHA256 to an AES-256-GCM key; every blob is a 12-byte iv followed by the ciphertext.
// A correct password is remembered for the browser session, per case study, as the derived key.
(function () {
  var form = document.querySelector('.gate');
  var holder = document.getElementById('locked');
  if (!form || !holder || !window.crypto || !crypto.subtle) return;

  var slug = form.dataset.slug;
  var store = 'unlock:' + slug;
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

  function reveal(key, page) {
    var hero = form.closest('.case-hero');
    var column = form.parentElement;
    form.remove();
    column.insertAdjacentHTML('beforeend', page.hero);
    hero.insertAdjacentHTML('afterend', page.body);
    document.querySelectorAll('img[data-locked]').forEach(function (img) {
      fetch(img.dataset.locked)
        .then(function (r) { return r.arrayBuffer(); })
        .then(function (buf) { return open(key, new Uint8Array(buf)); })
        .then(function (plain) { img.src = URL.createObjectURL(new Blob([plain], { type: img.dataset.type })); });
    });
  }

  function tryKey(key) {
    return open(key, bytes(payload.data)).then(function (plain) {
      reveal(key, JSON.parse(new TextDecoder().decode(plain)));
      return key;
    });
  }

  // Already unlocked earlier in this session.
  try {
    var saved = sessionStorage.getItem(store);
    if (saved) {
      crypto.subtle.importKey('raw', bytes(saved), 'AES-GCM', true, ['decrypt'])
        .then(tryKey)
        .catch(function () { sessionStorage.removeItem(store); });
    }
  } catch (e) { /* storage blocked: ask for the password as usual */ }

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    var button = form.querySelector('button');
    button.disabled = true;
    msg.textContent = 'Checking…';
    derive(form.pw.value)
      .then(tryKey)
      .then(function (key) {
        return crypto.subtle.exportKey('raw', key).then(function (raw) {
          try { sessionStorage.setItem(store, toB64(raw)); } catch (e2) { /* fine without it */ }
        });
      })
      .catch(function () {
        msg.textContent = "That password didn't work. Try again.";
        button.disabled = false;
        form.pw.select();
      });
  });
})();
