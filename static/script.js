function evaluatePasswordStrength(password) {
  let score = 0;
  let feedback = [];

  if (password.length >= 8) {
    score++;
    feedback.push("✅ Length is sufficient (8+ characters).");
  } else {
    feedback.push("❌ Password is too short (less than 8 characters).");
  }

  if (/[a-z]/.test(password)) {
    score++;
    feedback.push("✅ Contains lowercase letters.");
  } else {
    feedback.push("❌ Missing lowercase letters.");
  }

  if (/[A-Z]/.test(password)) {
    score++;
    feedback.push("✅ Contains uppercase letters.");
  } else {
    feedback.push("❌ Missing uppercase letters.");
  }

  if (/\d/.test(password)) {
    score++;
    feedback.push("✅ Contains digits.");
  } else {
    feedback.push("❌ Missing digits.");
  }

  if (/[!@#$%^&*(),.?":{}|<>]/.test(password)) {
    score++;
    feedback.push("✅ Contains special characters.");
  } else {
    feedback.push("❌ Missing special characters.");
  }

  if (password.length >= 12) {
    score++;
    feedback.push("💪 Bonus for length (12+ characters).");
  }

  let strength, color;
  if (score <= 2) {
    strength = "Weak Password";
    color = "red";
  } else if (score <= 4) {
    strength = "Medium Password";
    color = "orange";
  } else {
    strength = "Strong Password";
    color = "green";
  }

  return { strength, color, feedback };
}

// -----------------------
// DOM Interactions
// -----------------------
const passwordInput = document.getElementById("passwordInput");
const checkBtn = document.getElementById("checkBtn");
const feedbackList = document.getElementById("feedbackList");
const strengthLabel = document.getElementById("strengthLabel");
const showPassword = document.getElementById("showPassword");

// Show/hide password
showPassword.addEventListener("change", () => {
  passwordInput.type = showPassword.checked ? "text" : "password";
});

// Check strength on button click
checkBtn.addEventListener("click", () => {
  const password = passwordInput.value.trim();
  if (!password) {
    alert("Please enter a password!");
    return;
  }

  const { strength, color, feedback } = evaluatePasswordStrength(password);

  strengthLabel.textContent = strength;
  strengthLabel.style.color = color;

  feedbackList.innerHTML = "";
  feedback.forEach(item => {
    const li = document.createElement("li");
    li.textContent = item;
    feedbackList.appendChild(li);
  });

  // Bar fill: map score (0-6) -> percent 0-100
  const percent = Math.round((data.score / 6) * 100);
  let color;
  if(data.score <= 2) color = getComputedStyle(document.documentElement).getPropertyValue('--bad');
  else if(data.score <= 4) color = getComputedStyle(document.documentElement).getPropertyValue('--warn');
  else color = getComputedStyle(document.documentElement).getPropertyValue('--good');

  setBar(percent, color);

  // setBar(Math.min(100, Math.round(data.entropy)), colorForEntropy(data.entropy));
});

// allow Enter key to trigger check
passwordInput.addEventListener('keydown', (e)=>{
  if(e.key === 'Enter') checkBtn.click();

});
