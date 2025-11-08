const checkBtn = document.getElementById('checkBtn');
const passwordInput = document.getElementById('passwordInput');
const strengthBar = document.getElementById('strengthBar');
const strengthLabel = document.getElementById('strengthLabel');
const entropyLabel = document.getElementById('entropyLabel');
const feedbackList = document.getElementById('feedbackList');

function setBar(percent, color){
  strengthBar.style.width = percent + "%";
  strengthBar.style.background = color;
}

function colorForEntropy(entropy){
  // rough color mapping by entropy or use score in backend
  if(entropy < 28) return getComputedStyle(document.documentElement).getPropertyValue('--bad');
  if(entropy < 36) return getComputedStyle(document.documentElement).getPropertyValue('--warn');
  return getComputedStyle(document.documentElement).getPropertyValue('--good');
}

checkBtn.addEventListener('click', async () => {
  const password = passwordInput.value || '';
  const resp = await fetch('/api/evaluate', {
    method: 'POST',
    headers: {'Content-Type':'application/json'},
    body: JSON.stringify({password})
  });
  const data = await resp.json();

  // Strength label
  strengthLabel.textContent = `Strength: ${data.strength} (${data.score}/6)`;
  entropyLabel.textContent = `Entropy: ${data.entropy} bits`;

  // Feedback
  feedbackList.innerHTML = '';
  data.feedback.forEach(f => {
    const li = document.createElement('li');
    li.textContent = f;
    feedbackList.appendChild(li);
  });

  // Bar fill: map score (0-6) -> percent 0-100
  const percent = Math.round((data.score / 6) * 100);
  let color;
  if(data.score <= 2) color = getComputedStyle(document.documentElement).getPropertyValue('--bad');
  else if(data.score <= 4) color = getComputedStyle(document.documentElement).getPropertyValue('--warn');
  else color = getComputedStyle(document.documentElement).getPropertyValue('--good');

  setBar(percent, color);

  // If you prefer entropy coloring:
  // setBar(Math.min(100, Math.round(data.entropy)), colorForEntropy(data.entropy));
});

// Optional: allow Enter key to trigger check
passwordInput.addEventListener('keydown', (e)=>{
  if(e.key === 'Enter') checkBtn.click();
});
