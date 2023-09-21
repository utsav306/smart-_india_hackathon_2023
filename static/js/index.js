
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

