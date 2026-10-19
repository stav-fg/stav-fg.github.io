// The vertical subway map on the About page (Figma: "About · get to know me (vertical scroll)").
// The line runs down the left of the stops. It is drawn from where each stop actually sits on
// the page, so it follows the text as it wraps. As the page scrolls, the line draws itself down
// to the middle of the screen and the stop there becomes the current one. That is decoration
// only: every stop is readable without it.
// Without this script the stops are a plain list with a thin rule beside them.
(function () {
  var track = document.querySelector("[data-journey]");
  if (!track) return;

  var NS = "http://www.w3.org/2000/svg";
  var PALE = "#E4E2EA";
  var INK = "#17161A";
  var stops = [].slice.call(track.querySelectorAll(".jstop"));
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)");
  var svg, clipRect, stations = [], current, halo, ys = [], end = 0, ticking = false, now = -1;

  function el(name, attrs, parent) {
    var n = document.createElementNS(NS, name);
    for (var k in attrs) n.setAttribute(k, attrs[k]);
    if (parent) parent.appendChild(n);
    return n;
  }
  function path(points) {
    return "M" + points.map(function (p) { return p[0] + " " + p[1]; }).join(" L");
  }

  // Lines as in the horizontal map: Air Force green to Webiks, Study blue as a branch beside it,
  // Industry purple on from Webiks, Life orange as a branch beside that. Dotted after the last
  // station on each line, because the route goes on.
  function draw() {
    var css = getComputedStyle(track);
    var x0 = parseFloat(css.getPropertyValue("--x0"));
    var x1 = parseFloat(css.getPropertyValue("--x1"));
    var d = 32;
    var top = track.getBoundingClientRect().top;
    ys = stops.map(function (s) {
      var h = s.querySelector("h3").getBoundingClientRect();
      return Math.round(h.top + h.height / 2 - top);
    });
    end = ys[ys.length - 1] + 100;
    var W = x1 + 24;

    if (svg) svg.remove();
    svg = el("svg", { class: "journey-svg", width: W, height: end, viewBox: "0 0 " + W + " " + end, "aria-hidden": "true", focusable: "false" });
    var defs = el("defs", {}, svg);
    var clip = el("clipPath", { id: "journey-drawn" }, defs);
    clipRect = el("rect", { x: 0, y: 0, width: W, height: 0 }, clip);

    // The lines are worked out from the stops. The trunk runs through every stop on it, each
    // segment in the colour of the station it leaves, and dotted into a stop marked data-future.
    // Each branch (stops on data-line="branch", grouped by colour) leaves the trunk at the last
    // interchange before its first stop and runs beside it. If an interchange follows its last
    // stop it rejoins the trunk there (Study at Webiks); if not, it trails off dotted (Life).
    var trunk = [], branches = {}, order = [], lines = [];
    stops.forEach(function (s, i) {
      if (s.getAttribute("data-line") === "branch") {
        var c = s.getAttribute("data-color");
        if (!branches[c]) { branches[c] = []; order.push(c); }
        branches[c].push(i);
      } else trunk.push(i);
    });
    trunk.forEach(function (a, k) {
      var b = trunk[k + 1];
      if (b === undefined) return;
      lines.push([stops[a].getAttribute("data-color"), [[x0, ys[a]], [x0, ys[b]]], stops[b].hasAttribute("data-future")]);
    });
    var lastT = trunk[trunk.length - 1];
    lines.push([stops[lastT].getAttribute("data-color"), [[x0, ys[lastT]], [x0, end - 8]], true]);
    order.forEach(function (c) {
      var idx = branches[c], first = idx[0], last = idx[idx.length - 1];
      var inter = trunk.filter(function (t) { return stops[t].hasAttribute("data-interchange"); });
      var from = inter.filter(function (t) { return t < first; }).pop();
      if (from === undefined) from = trunk.filter(function (t) { return t < first; }).pop();
      var to = inter.filter(function (t) { return t > last; })[0];
      if (to !== undefined) {
        lines.push([c, [[x0, ys[from]], [x1, ys[from] + d], [x1, ys[to] - d], [x0, ys[to]]]]);
      } else {
        lines.push([c, [[x0, ys[from]], [x1, ys[from] + d], [x1, ys[last]]]]);
        lines.push([c, [[x1, ys[last]], [x1, end - 8]], true]);
      }
    });
    var pale = el("g", { fill: "none", stroke: PALE, "stroke-width": 7, "stroke-linecap": "round", "stroke-linejoin": "round" }, svg);
    var drawn = el("g", { fill: "none", "stroke-width": 7, "stroke-linecap": "round", "stroke-linejoin": "round", "clip-path": "url(#journey-drawn)" }, svg);
    lines.forEach(function (l) {
      var a = { d: path(l[1]) };
      if (l[2]) a["stroke-dasharray"] = "1 15";
      el("path", a, pale);
      a.stroke = l[0];
      el("path", a, drawn);
    });

    current = el("g", { class: "journey-current" }, svg);
    halo = el("circle", { r: 26, "fill-opacity": 0.18 }, current);
    var g = el("g", { fill: "#fff", "stroke-width": 4 }, svg);
    stations = stops.map(function (s, i) {
      var x = s.getAttribute("data-line") === "branch" ? x1 : x0;
      var inter = s.hasAttribute("data-interchange");
      // The key milestone has its own station: a disc in the line's colour with a white ring.
      if (s.hasAttribute("data-milestone")) {
        var c = s.getAttribute("data-color");
        el("circle", { cx: x, cy: ys[i], r: 17, fill: c, "fill-opacity": 0.3, stroke: "none" }, g);
        return el("circle", { cx: x, cy: ys[i], r: 13, fill: c, stroke: "#fff", "data-color": "#fff", "data-milestone": "" }, g);
      }
      var minor = s.classList.contains("jstop--minor");
      return el("circle", { cx: x, cy: ys[i], r: inter ? 11 : minor ? 6 : 8.5, "stroke-width": minor ? 3 : 4,
        stroke: inter ? INK : PALE, "data-color": inter ? INK : s.getAttribute("data-color") }, g);
    });
    // The current stop's ring and dot sit above the stations.
    el("circle", { r: 13, fill: "#fff", stroke: INK, "stroke-width": 4 }, current);
    el("circle", { r: 5, fill: INK }, current);
    svg.appendChild(current);
    track.insertBefore(svg, track.firstChild);
    now = -1;
    update();
  }

  function update() {
    ticking = false;
    var vh = window.innerHeight;
    var top = track.getBoundingClientRect().top;
    var still = reduce.matches;
    // The pen is the middle of the screen, in the track's own coordinates.
    var pen = still ? end : Math.max(0, Math.min(end, vh * 0.55 - top));
    clipRect.setAttribute("height", pen);

    var cur = 0;
    for (var i = 0; i < ys.length; i++) if (ys[i] <= pen + 4) cur = i;
    stops.forEach(function (s, i) {
      var reached = still || ys[i] <= pen + 4;
      s.classList.toggle("is-reached", reached);
      stations[i].setAttribute("stroke", reached ? stations[i].getAttribute("data-color") : PALE);
    });
    if (cur !== now) {
      now = cur;
      stops.forEach(function (s, i) { s.classList.toggle("is-current", i === cur); });
      current.setAttribute("transform", "translate(" + stations[cur].getAttribute("cx") + " " + ys[cur] + ")");
      current.style.opacity = stops[cur].hasAttribute("data-milestone") ? 0 : 1;
      halo.setAttribute("fill", stops[cur].getAttribute("data-color"));
    }
  }

  function onScroll() {
    if (!ticking) { ticking = true; requestAnimationFrame(update); }
  }

  track.classList.add("is-live");
  draw();
  window.addEventListener("scroll", onScroll, { passive: true });
  window.addEventListener("resize", function () { requestAnimationFrame(draw); });
  if (reduce.addEventListener) reduce.addEventListener("change", update);
  // Web fonts change line breaks, and with them where each stop sits.
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(draw);
})();
