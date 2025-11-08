function checkStrength() {
  const password = document.getElementById("password").value;
  let score = 0;
  let feedback = [];

  if (password.length >= 8) {
    score++;
    feedback.push("Length is sufficient (8+ characters).");
  } else {
    feedback.push("Password is too short (less than 8 characters).");
  }

  if (/[a-z]/.test(password)) {
    score++;
    feedback.push("Contains lowercase letters.");
  } else {
    feedback.push("Missing lowercase letters.");
  }

  if (/[A-Z]/.test(password)) {
    score++;
    feedback.push("Contains uppercase letters.");
  } else {
    feedback.push("Missing uppercase letters.");
  }

  if (/\d/.test(password)) {
    score++;
    feedback.push("Contains digits.");
  } else {
    feedback.push("Missing digits.");
  }

  if (/[!@#$%^&*(),.?":{}|<>]/.test(password)) {
    score++;
    feedback.push("Contains special characters.");
  } else {
    feedback.push("Missing special characters.");
  }

  if (password.length >= 12) {
    score++;
    feedback.push("Bonus for length (12+ characters).");
  }

  let strength = "Weak";
  if (score >= 5) strength = "Strong";
  else if (score >= 3) strength = "Medium";

  document.getElementById("result").textContent =
    `${strength} Password\nScore: ${score}/6\nFeedback:\n- ${feedback.join("\n- ")}`;
}

// Show/Hide password toggle
document.getElementById("togglePassword").addEventListener("click", function () {
  const passwordField = document.getElementById("password");
  if (passwordField.type === "password") {
    passwordField.type = "text";
    this.textContent = "Hide";
  } else {
    passwordField.type = "password";
    this.textContent = "Show";
  }
});
