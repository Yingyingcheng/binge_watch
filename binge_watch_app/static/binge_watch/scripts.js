document.addEventListener("DOMContentLoaded", function () {
  // Function to update the score display next to a slider
  function updateScoreDisplay(slider, display) {
    if (display && slider) {
      // Get the value, round to one decimal place, and add the flame emoji
      const value = parseFloat(slider.value).toFixed(1);
      display.textContent = value + " 🔥";
    }
  }

  // Function to set up the change listeners for a specific slider/display pair
  function setupSlider(sliderId, displayClass) {
    const slider = document.getElementById(sliderId);

    // The score-display span is a sibling within the same .form-group
    const display = slider
      ? slider.parentElement.querySelector("." + displayClass)
      : null;

    if (slider && display) {
      // 1. Initialize the display on page load
      updateScoreDisplay(slider, display);

      // 2. Update the display whenever the user drags the slider
      slider.addEventListener("input", () =>
        updateScoreDisplay(slider, display)
      );
    }
  }

  // Call the setup function for both Quality Score and Risk Score
  setupSlider("id_quality_score", "score-display");
  setupSlider("id_binge_risk_score", "score-display");
});
