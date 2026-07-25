document.addEventListener("DOMContentLoaded", function () {
  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---------------- Splash / ignition sequence ---------------- */
  var splash = document.getElementById("splash");
  if (splash) {
    if (reduceMotion) {
      splash.style.display = "none";
    } else {
      window.setTimeout(function () {
        splash.classList.add("fade-out");
        window.setTimeout(function () {
          splash.style.display = "none";
        }, 500);
      }, 1300);
    }
  }

  /* ---------------- Toast auto-dismiss ---------------- */
  var toast = document.querySelector(".toast");
  if (toast) {
    window.setTimeout(function () {
      toast.classList.add("fade-out");
    }, 2600);
  }

  /* ---------------- Live trip preview (add / edit form) ---------------- */
  var form = document.getElementById("trip-form");
  if (!form) return;

  var startInput = form.querySelector("[name='start_km']");
  var endInput = form.querySelector("[name='end_km']");
  var fuelInput = form.querySelector("[name='fuel_litres']");

  var distanceOut = document.getElementById("preview-distance");
  var efficiencyOut = document.getElementById("preview-efficiency");
  var statusOut = document.getElementById("preview-status-badge");
  var kmHint = document.getElementById("km-hint");
  var fuelHint = document.getElementById("fuel-hint");

  var GOOD = parseFloat(form.dataset.good);
  var AVERAGE = parseFloat(form.dataset.average);

  function updatePreview() {
    var start = parseFloat(startInput.value);
    var end = parseFloat(endInput.value);
    var fuel = parseFloat(fuelInput.value);

    kmHint.textContent = (!isNaN(start) && !isNaN(end) && end <= start)
      ? "End KM must be greater than Start KM."
      : "";

    fuelHint.textContent = (!isNaN(fuel) && fuel <= 0)
      ? "Fuel litres must be greater than zero."
      : "";

    var validInputs = !isNaN(start) && !isNaN(end) && !isNaN(fuel) && end > start && fuel > 0;

    if (!validInputs) {
      distanceOut.textContent = "—";
      efficiencyOut.textContent = "—";
      statusOut.innerHTML = "";
      statusOut.parentElement.querySelector(".helper").textContent =
        "Fill in the trip details to see the reading.";
      return;
    }

    var distance = end - start;
    var efficiency = Math.round((distance / fuel) * 100) / 100;

    var status = "poor";
    var statusLabel = "Poor";
    if (efficiency >= GOOD) {
      status = "good";
      statusLabel = "Good";
    } else if (efficiency >= AVERAGE) {
      status = "average";
      statusLabel = "Average";
    }

    distanceOut.textContent = distance + " km";
    efficiencyOut.textContent = efficiency + " km/l";
    statusOut.innerHTML = '<span class="status-badge ' + status + '">' + statusLabel + "</span>";
    statusOut.parentElement.querySelector(".helper").textContent =
      "Live reading — updates as you type.";
  }

  [startInput, endInput, fuelInput].forEach(function (input) {
    input.addEventListener("input", updatePreview);
  });

  updatePreview();
});
