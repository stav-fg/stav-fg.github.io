// The subway map on the About page. Each stop holds one paragraph of the cover letter, and the
// card under the map shows the selected stop's paragraph. Without this script every paragraph
// is shown as a list, so nothing is lost.
(function () {
  var route = document.querySelector("[data-route]");
  if (!route) return;

  var stops = route.querySelectorAll(".stop");
  var hotspots = route.querySelectorAll(".route-hotspots button");
  var labels = route.querySelectorAll(".route-labels text");
  var selected = route.querySelector(".route-selected");
  var halo = route.querySelector(".route-halo");
  var bar = route.querySelector(".stop-bar");
  var count = route.querySelector(".stop-count");
  var prev = route.querySelector('[data-step="-1"]');
  var next = route.querySelector('[data-step="1"]');
  var scroller = route.querySelector(".route-scroll");
  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var current = 0;

  function show(i, focusStop) {
    current = Math.max(0, Math.min(stops.length - 1, i));
    var color = stops[current].getAttribute("data-color");
    var spot = hotspots[current];
    var x = spot.style.getPropertyValue("--x").trim();
    var y = spot.style.getPropertyValue("--y").trim();

    for (var k = 0; k < stops.length; k++) {
      stops[k].hidden = k !== current;
      hotspots[k].setAttribute("aria-pressed", k === current ? "true" : "false");
    }
    selected.style.transform = "translate(" + x + "px, " + y + "px)";
    halo.setAttribute("fill", color);
    bar.style.background = color;
    count.textContent = current + 1 + " of " + stops.length;
    prev.disabled = current === 0;
    next.disabled = current === stops.length - 1;
    if (focusStop) spot.focus({ preventScroll: true });

    // On a narrow screen the map scrolls sideways: bring the selected stop into the middle.
    if (scroller.scrollWidth > scroller.clientWidth) {
      var left = (Number(x) / 1152) * scroller.scrollWidth - scroller.clientWidth / 2;
      scroller.scrollTo({ left: Math.max(0, left), behavior: reduceMotion ? "auto" : "smooth" });
    }
  }

  route.classList.add("is-live");

  for (var h = 0; h < hotspots.length; h++) {
    hotspots[h].addEventListener("click", function () {
      show(Number(this.getAttribute("data-stop")));
    });
  }
  // The station names on the map are clickable too, as on a real map.
  for (var l = 0; l < labels.length; l++) {
    labels[l].addEventListener("click", function () {
      show(Number(this.getAttribute("data-stop")));
    });
  }
  prev.addEventListener("click", function () { show(current - 1); });
  next.addEventListener("click", function () { show(current + 1); });

  // Arrow keys move along the line while a stop has focus.
  route.querySelector(".route-hotspots").addEventListener("keydown", function (e) {
    if (e.key === "ArrowRight" || e.key === "ArrowDown") { e.preventDefault(); show(current + 1, true); }
    if (e.key === "ArrowLeft" || e.key === "ArrowUp") { e.preventDefault(); show(current - 1, true); }
    if (e.key === "Home") { e.preventDefault(); show(0, true); }
    if (e.key === "End") { e.preventDefault(); show(stops.length - 1, true); }
  });

  show(0);
})();
