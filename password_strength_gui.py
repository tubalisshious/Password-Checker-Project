import re
import tkinter as tk
from tkinter import messagebox

# -------------------------------
# Password Strength Evaluation
# -------------------------------
def evaluate_password_strength(password):
    score = 0
    feedback = []

    # Length check
    if len(password) >= 8:
        score += 1
        feedback.append("✅ Length is sufficient (8+ characters).")
    else:
        feedback.append("❌ Password is too short (less than 8 characters).")

    # Lowercase
    if re.search(r'[a-z]', password):
        score += 1
        feedback.append("✅ Contains lowercase letters.")
    else:
        feedback.append("❌ Missing lowercase letters.")

    # Uppercase
    if re.search(r'[A-Z]', password):
        score += 1
        feedback.append("✅ Contains uppercase letters.")
    else:
        feedback.append("❌ Missing uppercase letters.")

    # Digits
    if re.search(r'\d', password):
        score += 1
        feedback.append("✅ Contains digits.")
    else:
        feedback.append("❌ Missing digits.")

    # Special characters
    if re.search(r'[!@#$%^&*(),.?\":{}|<>]', password):
        score += 1
        feedback.append("✅ Contains special characters.")
    else:
        feedback.append("❌ Missing special characters.")

    # Bonus for long passwords
    if len(password) >= 12:
        score += 1
        feedback.append("💪 Bonus for length (12+ characters).")

    # Determine strength
    if score <= 2:
        strength = "Weak"
        color = "red"
    elif score <= 4:
        strength = "Medium"
        color = "orange"
    else:
        strength = "Strong"
        color = "green"

    return strength, color, feedback


# -------------------------------
# GUI Setup
# -------------------------------
def check_password():
    password = password_entry.get()
    strength, color, feedback = evaluate_password_strength(password)

    # Clear previous feedback
    result_label.config(text=f"{strength} Password", fg=color)
    feedback_box.delete(1.0, tk.END)
    for item in feedback:
        feedback_box.insert(tk.END, f"{item}\n")

def toggle_password():
    if show_var.get():
        password_entry.config(show="")
    else:
        password_entry.config(show="*")


# -------------------------------
# Main Window
# -------------------------------
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("480x420")
root.configure(bg="#f7f9fc")

# Title label
title_label = tk.Label(root, text="🔒 Password Strength Checker",
                       font=("Helvetica", 16, "bold"), bg="#f7f9fc", fg="#222")
title_label.pack(pady=15)

# Entry box
password_entry = tk.Entry(root, width=40, font=("Arial", 12), show="*", relief="solid", bd=1)
password_entry.pack(pady=10)

# Show password checkbox
show_var = tk.BooleanVar(value=False)
show_checkbox = tk.Checkbutton(root, text="Show Password", variable=show_var,
                               onvalue=True, offvalue=False, bg="#f7f9fc",
                               command=toggle_password)
show_checkbox.pack()

# Check button
check_button = tk.Button(root, text="Check Strength", font=("Arial", 12, "bold"),
                         bg="#4CAF50", fg="white", relief="ridge", padx=10, pady=5,
                         command=check_password)
check_button.pack(pady=15)

# Result label
result_label = tk.Label(root, text="", font=("Helvetica", 14, "bold"), bg="#f7f9fc")
result_label.pack(pady=5)

# Feedback box
feedback_box = tk.Text(root, height=10, width=55, font=("Arial", 10), wrap="word", relief="solid", bd=1)
feedback_box.pack(pady=10)

# Footer
footer_label = tk.Label(root, text="Developed in Python 🐍 | GUI with Tkinter",
                        bg="#f7f9fc", fg="#666", font=("Arial", 9))
footer_label.pack(pady=5)

root.mainloop()
