from flask import Flask, render_template, request, jsonify
import re
import math

app = Flask(__name__)

def evaluate_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
        feedback.append("Length is sufficient (8+ characters).")
    else:
        feedback.append("Password is too short (less than 8 characters).")

    if re.search(r'[a-z]', password):
        score += 1
        feedback.append("Contains lowercase letters.")
    else:
        feedback.append("Missing lowercase letters.")

    if re.search(r'[A-Z]', password):
        score += 1
        feedback.append("Contains uppercase letters.")
    else:
        feedback.append("Missing uppercase letters.")

    if re.search(r'\d', password):
        score += 1
        feedback.append("Contains digits.")
    else:
        feedback.append("Missing digits.")

    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
        feedback.append("Contains special characters.")
    else:
        feedback.append("Missing special characters.")

    if len(password) >= 12:
        score += 1
        feedback.append("Bonus for length (12+ characters).")

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    return strength, score, feedback

def calculate_entropy(password):
    charset = 0
    if re.search(r'[a-z]', password):
        charset += 26
    if re.search(r'[A-Z]', password):
        charset += 26
    if re.search(r'\d', password):
        charset += 10
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        charset += 33
    entropy = len(password) * math.log2(charset) if charset else 0
    return round(entropy, 2)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/evaluate', methods=['POST'])
def api_evaluate():
    data = request.get_json() or {}
    password = data.get('password', '')
    strength, score, feedback = evaluate_password_strength(password)
    entropy = calculate_entropy(password)
    # Return structured JSON for the frontend
    return jsonify({
        "strength": strength,
        "score": score,
        "feedback": feedback,
        "entropy": entropy
    })

if __name__ == "__main__":
    app.run(debug=True)
