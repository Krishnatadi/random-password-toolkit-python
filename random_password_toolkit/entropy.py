import math
import re
from collections import Counter

# Top 15 most common passwords - kept minimal for scalability
COMMON_PASSWORDS = {
    'password', '123456', '12345678', 'qwerty', 'abc123', 'monkey', 'letmein',
    'dragon', 'admin', 'password123', '123456789', '1234567890', 'admin123', 'root', 'letmein'
}

# Keyboard pattern detection - organized by rows
KEYBOARD_PATTERNS = {
    'qwerty', 'asdfgh', 'zxcvbn', 'qazwsx', 'qwertyuiop', 'asdfghjkl', 'zxcvbnm',
    'qweasd', 'asdfghjkl;', '[]{}', '1qaz', '2wsx', '3edc', '4rfv', '5tgb'
}

# Sequential digit and letter patterns (for quick detection)
SEQUENTIAL_PATTERNS = {
    '012', '123', '234', '345', '456', '567', '678', '789', '890',
    'abc', 'bcd', 'cde', 'def', 'efg', 'fgh', 'ghi', 'hij', 'ijk', 'jkl',
    'klm', 'lmn', 'mno', 'nop', 'opq', 'pqr', 'qrs', 'rst', 'stu', 'tuv',
    'uvw', 'vwx', 'wxy', 'xyz'
}


# ========== Smart Detection Functions ==========

def is_numeric_only(password):
    """Check if password contains only numbers."""
    return password.isdigit()


def is_alphabet_only(password):
    """Check if password contains only letters."""
    return password.isalpha()


def has_repeated_characters(password):
    """Detect if password has 3+ consecutive identical characters."""
    return bool(re.search(r'(.)\1{2,}', password))


def has_keyboard_patterns(password):
    """Detect common keyboard patterns (rows, diagonals, etc.)."""
    pwd_lower = password.lower()
    
    # Check against known keyboard patterns
    for pattern in KEYBOARD_PATTERNS:
        if pattern in pwd_lower:
            return True
    
    # Check for directional patterns: adjacent keys on keyboard
    # Horizontal: qwerty, asdfgh, zxcvbn
    # Diagonal: 1qaz, 2wsx, etc.
    keyboard_regex = r'[qwertyuiopasdfghjklzxcvbnm]{3,}|[0-9]{3,}'
    if re.search(keyboard_regex, pwd_lower):
        # Additional check for actual keyboard adjacency
        if any(pattern in pwd_lower for pattern in ['qwe', 'wer', 'ert', 'rty', 'qaz', 'wsx', 'edc', 'rfv']):
            return True
    
    return False


def has_sequential_characters(password):
    """Detect sequential digit/letter patterns like 123, abc."""
    pwd_lower = password.lower()
    
    # Check against sequential patterns
    for pattern in SEQUENTIAL_PATTERNS:
        if pattern in pwd_lower:
            return True
    
    return False


def has_word_number_pattern(password):
    """Detect word followed by numbers pattern (e.g., password123, admin2024)."""
    # Pattern: letters followed by 2+ digits
    return bool(re.search(r'[a-zA-Z]{4,}[0-9]{2,}$', password))


def has_word_symbol_pattern(password):
    """Detect word followed by symbols pattern (e.g., password@, admin#)."""
    # Pattern: letters followed by 1-3 symbols at end
    return bool(re.search(r'[a-zA-Z]{4,}[!@#$%^&*()_+=\-\[\]{};:\'",.<>?/\\|`~]{1,3}$', password))


def is_common_password(password):
    """Check if password is in common passwords list."""
    return password.lower() in COMMON_PASSWORDS


def analyze_password_security(password):
    """
    Intelligent hybrid password security analysis.
    
    Uses pattern-based detection instead of large lists for scalability.
    
    Args:
        password (str): The password to analyze.
    
    Returns:
        dict: Security analysis containing:
            - 'is_common' (bool): Is in common passwords list
            - 'pattern_issues' (list): Detected pattern issues
            - 'entropy' (float): Shannon entropy in bits
            - 'strength' (str): Overall strength classification
    """
    pattern_issues = []
    
    # Check common passwords (small, focused list)
    is_common = is_common_password(password)
    if is_common:
        pattern_issues.append("common_password")
    
    # Dynamic pattern detection (scalable, no large lists)
    if is_numeric_only(password):
        pattern_issues.append("numeric_only")
    
    if is_alphabet_only(password):
        pattern_issues.append("alphabet_only")
    
    if has_repeated_characters(password):
        pattern_issues.append("repeated_characters")
    
    if has_keyboard_patterns(password):
        pattern_issues.append("keyboard_pattern")
    
    if has_sequential_characters(password):
        pattern_issues.append("sequential_characters")
    
    if has_word_number_pattern(password):
        pattern_issues.append("word_number_pattern")
    
    if has_word_symbol_pattern(password):
        pattern_issues.append("word_symbol_pattern")
    
    # Check character variety
    charset_types = 0
    if re.search(r'[a-z]', password):
        charset_types += 1
    if re.search(r'[A-Z]', password):
        charset_types += 1
    if re.search(r'[0-9]', password):
        charset_types += 1
    if re.search(r'[!@#$%^&*()_+\[\]{}|;:,.<>?`~\-=\\/"\']', password):
        charset_types += 1
    
    if charset_types < 2:
        pattern_issues.append("low_variety")
    
    # Length check
    if len(password) < 8:
        pattern_issues.append("too_short")
    
    # Get entropy and strength
    entropy_value = calculate_entropy(password)
    strength = classify_strength(entropy_value)
    
    return {
        'is_common': is_common,
        'pattern_issues': pattern_issues,
        'entropy': entropy_value,
        'strength': strength
    }


def calculate_entropy(password):
    """
    Calculate Shannon entropy of a password.
    
    Information entropy measures the randomness and unpredictability of the password.
    Higher entropy indicates more randomness and stronger password.
    
    Formula: H = -Σ(p_i * log2(p_i)) where p_i is the probability of each character
    
    Args:
        password (str): The password to analyze.
    
    Returns:
        float: Entropy value in bits. Typical ranges:
               - 0-20 bits: Very Weak
               - 20-40 bits: Weak
               - 40-60 bits: Medium
               - 60-90 bits: Strong
               - 90+ bits: Very Strong
    """
    if not password:
        return 0.0
    
    # Count frequency of each character
    char_counts = Counter(password)
    password_length = len(password)
    
    # Calculate entropy
    entropy = 0.0
    for count in char_counts.values():
        probability = count / password_length
        if probability > 0:
            entropy -= probability * math.log2(probability)
    
    # Normalize by password length and multiply by log2 of character pool size
    charset_size = get_charset_size(password)
    if charset_size > 0:
        entropy = entropy * math.log2(charset_size) if charset_size > 1 else 0
    
    # Scale entropy to bits
    entropy_bits = entropy * password_length
    
    return round(entropy_bits, 2)


def get_charset_size(password):
    """
    Determine the size of the character set used in the password.
    
    Args:
        password (str): The password to analyze.
    
    Returns:
        int: Size of character pool used.
    """
    charset_size = 0
    
    if re.search(r'[a-z]', password):
        charset_size += 26
    if re.search(r'[A-Z]', password):
        charset_size += 26
    if re.search(r'[0-9]', password):
        charset_size += 10
    if re.search(r'[!@#$%^&*()_+\[\]{}|;:,.<>?`~\-=\\/"\']', password):
        charset_size += 32
    
    return charset_size


def detect_issues(password):
    """
    Detect common password issues and weaknesses using smart pattern detection.
    
    Uses dynamic pattern recognition instead of static lists for better scalability.
    
    Args:
        password (str): The password to analyze.
    
    Returns:
        list: List of detected issues with human-readable descriptions.
    """
    issues = []
    
    # Use the smart analysis function
    security = analyze_password_security(password)
    
    # Map pattern issues to human-readable descriptions
    issue_descriptions = {
        'too_short': "Password is too short (less than 8 characters)",
        'common_password': "Password is a common/weak password",
        'numeric_only': "Password contains only numbers",
        'alphabet_only': "Password contains only letters",
        'repeated_characters': "Password contains repeated characters (3+ same character in a row)",
        'keyboard_pattern': "Password contains keyboard patterns",
        'sequential_characters': "Password contains sequential characters",
        'word_number_pattern': "Password follows word+number pattern (e.g., password123)",
        'word_symbol_pattern': "Password follows word+symbol pattern (e.g., password@)",
        'low_variety': "Password lacks character variety (use uppercase, lowercase, numbers, symbols)"
    }
    
    for pattern_issue in security['pattern_issues']:
        if pattern_issue in issue_descriptions:
            issues.append(issue_descriptions[pattern_issue])
    
    return issues


def classify_strength(entropy_value):
    """
    Classify password strength based on entropy value.
    
    Args:
        entropy_value (float): The entropy in bits.
    
    Returns:
        str: Strength classification.
    """
    if entropy_value < 20:
        return "Very Weak"
    elif entropy_value < 40:
        return "Weak"
    elif entropy_value < 60:
        return "Medium"
    elif entropy_value < 90:
        return "Strong"
    else:
        return "Very Strong"


def get_improvement_suggestions(password, entropy_value, issues):
    """
    Generate actionable suggestions to improve password strength.
    
    Args:
        password (str): The password to analyze.
        entropy_value (float): The entropy in bits.
        issues (list): List of detected issues.
    
    Returns:
        str: Actionable suggestion for improvement.
    """
    if not issues:
        return "Password meets security standards."
    
    suggestions = []
    
    if entropy_value < 60:
        suggestions.append(f"Increase password length (currently {len(password)} characters, aim for 12+)")
    
    if any("sequential" in issue.lower() for issue in issues):
        suggestions.append("Avoid sequential characters like '123' or 'abc'")
    
    if any("keyboard" in issue.lower() for issue in issues):
        suggestions.append("Avoid keyboard patterns like 'qwerty' or 'asdfgh'")
    
    if any("repeated" in issue.lower() for issue in issues):
        suggestions.append("Avoid repeating the same character multiple times")
    
    if any("variety" in issue.lower() for issue in issues):
        suggestions.append("Mix uppercase, lowercase, numbers, and symbols")
    
    if any("only" in issue.lower() for issue in issues):
        suggestions.append("Include different character types (letters, numbers, symbols)")
    
    if any("common" in issue.lower() for issue in issues):
        suggestions.append("Choose a unique password that's not in common password lists")
    
    if any("short" in issue.lower() for issue in issues):
        suggestions.append("Increase password length to at least 12 characters")
    
    return " | ".join(suggestions) if suggestions else "Password meets security standards."


def check_entropy(password):
    """
    Comprehensive password entropy analysis.
    
    Analyzes a password using Information Entropy theory and provides:
    - Entropy value (in bits)
    - Strength classification
    - Detected issues
    - Improvement suggestions
    
    Args:
        password (str): The password to analyze.
    
    Returns:
        dict: A dictionary containing:
            - 'entropy' (float): Entropy value in bits
            - 'strength' (str): Strength classification
            - 'issues' (list): List of detected issues
            - 'suggestion' (str): Actionable improvement suggestions
            - 'length' (int): Password length
            - 'charset_size' (int): Size of character pool used
    """
    entropy_value = calculate_entropy(password)
    strength = classify_strength(entropy_value)
    issues = detect_issues(password)
    suggestion = get_improvement_suggestions(password, entropy_value, issues)
    charset_size = get_charset_size(password)
    
    return {
        'entropy': entropy_value,
        'strength': strength,
        'issues': issues,
        'suggestion': suggestion,
        'length': len(password),
        'charset_size': charset_size
    }
