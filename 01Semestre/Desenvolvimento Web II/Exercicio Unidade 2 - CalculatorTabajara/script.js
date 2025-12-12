const display = document.getElementById("display");

function addToDisplay(value) {
  display.value += value;
}

function clearDisplay() {
  display.value = "";
}

function calculate() {
  try {
    display.value = eval(display.value); // eval só para fins didáticos em projetos simples
  } catch (error) {
    display.value = "Erro";
  }
}

const buttons = document.querySelectorAll(".btn");

buttons.forEach((button) => {
  button.addEventListener("click", () => {
    const value = button.dataset.value;
    const action = button.dataset.action;

    if (action === "clear") {
      clearDisplay();
      return;
    }

    if (action === "equal") {
      calculate();
      return;
    }

    addToDisplay(value);
  });
});
