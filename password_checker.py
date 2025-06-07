import re

def check_password_strength(password):
    """
    We will check the strength of password based on multiple criteria.
    
    Returns a dictionary with strength score, feedback messages, and a boolean indicating if the password meets basic strong criteria.
    """
    
    score = 0
    feedback = []
    
    #Criteria A: Length
    #A Longer Password Is Stronger.
    if len(password) >= 12:
        score += 3
        feedback.append("Excellent Length!")
    elif len(password) >= 8:
        score +=2
        feedback.append("Good Length!")
    else:
        score += 1
        feedback.append("Consider a longer password for better security.")
        
    #Criteria B: UpperCase
    #Presence of UpperCase increases complexity
    if re.search(r"[A-Z]", password):
        score += 1
        feedback.append("Contains UpperCase")
    else:
        feedback.append("Add UpperCase for more strength.")
        
    #Criteria C: LowerCase
    #Presence of LowerCase increases complexity
    if re.search(r"[a-z]", password):
        score += 1
        feedback.append("Contains LowerCase")
    else:
        feedback.append("Add LowerCase for more strength.")
        
    #Criteria D: Numbers
    #Presence of Numbers increases complexity
    if re.search(r"\d", password):
        score += 1
        feedback.append("Contains numbers")
    else:
        feedback.append("Add Numbers for more strength.")
        
    #Criteria E: Special Characters
    #Presence of Special Characters increases complexity
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 2
        feedback.append("Contains Special Characters.")
    else:
        feedback.append("Add Special Characters for more strength.")
        
    #Criteria F: Avoid Common Passwords
    #Very Basic Check
    if "password" in password.lower() or "123456" in password or "qwerty" in password or "abcdef" in password:
        score -= 2
        feedback.append("Avoid common and easily guessable patterns.")
        
    #Overall strength based on score.
    strength_level = ""
    is_strong = False
    if score >= 8:
        strength_level = "Very Strong"
        is_strong = True
    elif score >= 6:
        strength_level = "Strong"
        is_strong = True
    elif score >= 4:
        strength_level = "Moderate"
    elif score >= 2:
        strength_level = "Weak"
    else:
        strength_level = "Very Weak"
        
    return {
        "score": score,
        "strength": strength_level,
        "feedback": feedback,
        "is_strong": is_strong
    }
    
if __name__ == "__main__":
    print("---Password Strength Checker (Command Line)---")
    while True:
        password_input = input("Enter a password (or 'quit' to exit):")
        if password_input.lower() == "quit":
            break
        
        result = check_password_strength(password_input)
        print(f"\nPassword: {password_input}")
        print(f"Strength: {result['strength']} (Score: {result['score']})")
        print("Feedback:")
        for msg in result['feedback']:
            print(f"- {msg}")
        print("-" * 40)