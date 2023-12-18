
const modeToggleCheckbox = document.getElementById('dark-mode-toggle');
let currentMode = localStorage.getItem('mode');

const logoLight = document.getElementById('logo-light');
const logoDark = document.getElementById('logo-dark');

function setMode() {
  if (modeToggleCheckbox.checked) {
    document.body.classList.add('dark-mode');
    currentMode = 'dark';
    logoLight.style.display = 'none';
    logoDark.style.display = 'block';
  } else {
    document.body.classList.remove('dark-mode');
    currentMode = 'light';
    logoLight.style.display = 'block';
    logoDark.style.display = 'none';
  }
  localStorage.setItem('mode', currentMode);
}

modeToggleCheckbox.addEventListener('change', setMode);

if (currentMode === 'dark') {
  modeToggleCheckbox.checked = true;
  setMode();
}

const darkTab = document.getElementById('dark-mode-toggle');
darkTab.addEventListener('click', (e) => {
  e.preventDefault();
  modeToggleCheckbox.checked = !modeToggleCheckbox.checked;
  setMode();
});

var preload= document.getElementById("loading")
function onloade() {
  // You can perform additional actions here if needed
  document.getElementById("loading").style.display = "none"; // Hide the loading div
}

var dynamicButtonId = "your_dynamic_button_id";

// Set the dynamic ID to the "Go to" button
document.getElementById("goToButton1").id = dynamicButtonId;
console.log(document.getElementById("goToButton1"))

