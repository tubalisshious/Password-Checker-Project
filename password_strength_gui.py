import tkinter as tk
from tkinter import messagebox
import re

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

    return strength, feedback


def check_password():
    password = entry.get()
    strength, feedback = evaluate_password_strength(password)
    result_label.config(text=f"Strength: {strength}\n" + "\n".join(f"- {f}" for f in feedback))


# GUI window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("500x300")

tk.Label(root, text="Enter a password:", font=("Segoe UI", 12)).pack(pady=10)
entry = tk.Entry(root, show="*", width=40)
entry.pack()

tk.Button(root, text="Check Strength", command=check_password, bg="#3b82f6", fg="white").pack(pady=10)
result_label = tk.Label(root, text="", justify="left", font=("Consolas", 10))
result_label.pack(pady=10)

root.mainloop()
