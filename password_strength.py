import re

def evaluate_password_strength(password):
    """
    Evaluates the strength of a password based on length and character diversity.
    
    Returns:
        str: Strength level ('Weak', 'Medium', or 'Strong') and a brief explanation.
    """
    score = 0
    feedback = []
    
    # Check length
    if len(password) >= 8:
        score += 1
        feedback.append("Length is sufficient (8+ characters).")
    else:
        feedback.append("Password is too short (less than 8 characters).")
    
    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        score += 1
        feedback.append("Contains lowercase letters.")
    else:
        feedback.append("Missing lowercase letters.")
    
    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        score += 1
        feedback.append("Contains uppercase letters.")
    else:
        feedback.append("Missing uppercase letters.")
    
    # Check for digits
    if re.search(r'\d', password):
        score += 1
        feedback.append("Contains digits.")
    else:
        feedback.append("Missing digits.")
    
    # Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
        feedback.append("Contains special characters.")
    else:
        feedback.append("Missing special characters.")
    
    # Bonus for longer passwords
    if len(password) >= 12:
        score += 1
        feedback.append("Bonus for length (12+ characters).")
    
    # Determine strength
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"
    
    return f"{strength} Password\nScore: {score}/6\nFeedback:\n" + "\n".join(f"- {item}" for item in feedback)

# Main execution for user input
if __name__ == "__main__":
    password = input("Enter a password to evaluate: ")
    result = evaluate_password_strength(password)
    print(result)