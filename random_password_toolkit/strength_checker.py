import re

def check_password_strength(password):
    """
    Check the strength of a password based on several criteria and provide a score.
    
    Args:
        password (str): The password to evaluate.
    
    Returns:
        dict: A dictionary containing the password's strength and score.
    """
    is_length_sufficient = False
    has_digits = False
    has_lowercase_letters = False
    has_uppercase_letters = False
    has_special_characters = False

    # Check if password length is sufficient (>= 12)
    if len(password) >= 12:
        is_length_sufficient = True

    # Check for digits
    if re.search(r'\d', password):
        has_digits = True

    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        has_lowercase_letters = True

    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        has_uppercase_letters = True

    # Check for special characters
    if re.search(r'[!@#$%^&*()_+\[\]{}|;:,.<>?]', password):
        has_special_characters = True

    # Count the number of criteria met
    criteria_met = sum([
        is_length_sufficient,
        has_digits,
        has_lowercase_letters,
        has_uppercase_letters,
        has_special_characters,
    ])

    # Determine password strength based on criteria met and assign a score
    if criteria_met == 5:
        password_strength = "Very Strong"
        score = 100  # Maximum score
    elif criteria_met == 4:
        password_strength = "Strong"
        score = 80
    elif criteria_met == 3:
        password_strength = "Moderate"
        score = 60
    elif criteria_met == 2:
        password_strength = "Weak"
        score = 40
    else:
        password_strength = "Very Weak"
        score = 20  # Minimum score

    return {
        "strength": password_strength,
        "score": score
    }

