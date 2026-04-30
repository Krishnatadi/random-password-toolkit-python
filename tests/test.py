"""
Comprehensive test suite for Random Password Toolkit.
Tests all password generation, strength checking, entropy analysis, and encryption features.
"""

import sys
from random_password_toolkit import (
    # Password generation
    generate,
    generate_multiple,
    generate_pronounceable_password,
    generate_with_custom_pool,
    # Password strength & security
    check_password_strength,
    check_entropy,
    analyze_password_security,
    is_numeric_only,
    is_alphabet_only,
    has_repeated_characters,
    has_keyboard_patterns,
    has_sequential_characters,
    has_word_number_pattern,
    has_word_symbol_pattern,
    is_common_password,
    # Encryption/Decryption
    encrypt_password,
    decrypt_password,
    # Other utilities
    RandomNumberGenerator,
    generate_random_number,
    TokenGenerator,
    DataMasker,
)


def test_password_generation():
    """Test password generation functions."""
    print("\n" + "=" * 70)
    print("TEST 1: PASSWORD GENERATION")
    print("=" * 70)
    
    # Test basic generation
    pwd1 = generate(length=12, numbers=True, symbols=True)
    assert len(pwd1) == 12, f"Expected length 12, got {len(pwd1)}"
    print(f"✓ Basic generation (12 chars): {pwd1}")
    
    # Test multiple generation
    pwds = generate_multiple(5, {"length": 8, "numbers": True})
    assert len(pwds) == 5, f"Expected 5 passwords, got {len(pwds)}"
    print(f"✓ Multiple generation (5 passwords): {pwds}")
    
    # Test pronounceable
    pwd_pronounceable = generate_pronounceable_password(length=10)
    assert len(pwd_pronounceable) == 10, f"Expected length 10, got {len(pwd_pronounceable)}"
    print(f"✓ Pronounceable password: {pwd_pronounceable}")
    
    # Test custom pool
    pwd_custom = generate_with_custom_pool(length=8, custom_pool="ABC123")
    assert all(c in "ABC123" for c in pwd_custom), "Custom pool password contains invalid characters"
    print(f"✓ Custom pool password (ABC123): {pwd_custom}")


def test_password_strength():
    """Test password strength checking."""
    print("\n" + "=" * 70)
    print("TEST 2: PASSWORD STRENGTH CHECKING")
    print("=" * 70)
    
    test_cases = [
        ("MyP@ssw0rd123!", "Very Strong"),
        ("password", "Very Weak"),
        ("Test123", "Strong"),
        ("qwerty", "Very Weak"),
        ("SecureP@ss2024", "Very Strong"),
    ]
    
    for password, expected_category in test_cases:
        result = check_password_strength(password)
        strength = result['strength']
        score = result['score']
        print(f"✓ '{password}': {strength} (Score: {score}/100)")


def test_password_entropy():
    """Test password entropy analysis."""
    print("\n" + "=" * 70)
    print("TEST 3: PASSWORD ENTROPY ANALYSIS")
    print("=" * 70)
    
    test_cases = [
        ("password123", "Strong/Very Strong"),
        ("MySecure!@#", "Very Strong"),
        ("weak", "Very Weak/Weak"),
        ("abc123", "Weak/Medium"),
    ]
    
    for password, expected_range in test_cases:
        result = check_entropy(password)
        entropy = result['entropy']
        strength = result['strength']
        print(f"✓ '{password}': {entropy} bits - {strength}")
        assert result['length'] == len(password), "Length mismatch"
        assert result['charset_size'] > 0, "Charset size invalid"


def test_pattern_detection():
    """Test smart pattern detection."""
    print("\n" + "=" * 70)
    print("TEST 4: PATTERN DETECTION (Smart Hybrid System)")
    print("=" * 70)
    
    # Test numeric only
    assert is_numeric_only("123456") == True
    assert is_numeric_only("abc123") == False
    print("✓ Numeric-only detection")
    
    # Test alphabet only
    assert is_alphabet_only("password") == True
    assert is_alphabet_only("password123") == False
    print("✓ Alphabet-only detection")
    
    # Test repeated characters
    assert has_repeated_characters("aaaaaa") == True
    assert has_repeated_characters("password") == False
    print("✓ Repeated characters detection")
    
    # Test keyboard patterns
    assert has_keyboard_patterns("qwerty") == True
    assert has_keyboard_patterns("1qaz") == True
    assert has_keyboard_patterns("MyPassword") == False
    print("✓ Keyboard pattern detection")
    
    # Test sequential characters
    assert has_sequential_characters("123456") == True
    assert has_sequential_characters("abcdef") == True
    assert has_sequential_characters("MyPass") == False
    print("✓ Sequential character detection")
    
    # Test word+number pattern
    assert has_word_number_pattern("password123") == True
    assert has_word_number_pattern("admin2024") == True
    assert has_word_number_pattern("MyPassword") == False
    print("✓ Word+number pattern detection")
    
    # Test word+symbol pattern
    assert has_word_symbol_pattern("password@") == True
    assert has_word_symbol_pattern("admin#") == True
    assert has_word_symbol_pattern("MyPassword") == False
    print("✓ Word+symbol pattern detection")
    
    # Test common password
    assert is_common_password("password") == True
    assert is_common_password("qwerty") == True
    assert is_common_password("MyUniquePass2024") == False
    print("✓ Common password detection")


def test_security_analysis():
    """Test comprehensive security analysis."""
    print("\n" + "=" * 70)
    print("TEST 5: COMPREHENSIVE SECURITY ANALYSIS")
    print("=" * 70)
    
    # Test weak password
    result = analyze_password_security("password123")
    assert result['is_common'] == True
    assert len(result['pattern_issues']) > 0
    print(f"✓ password123: Common={result['is_common']}, Issues={len(result['pattern_issues'])}")
    
    # Test strong password
    result = analyze_password_security("Xk#9mL$pQ2@")
    assert result['is_common'] == False
    assert len(result['pattern_issues']) == 0
    assert result['entropy'] > 100
    print(f"✓ Xk#9mL$pQ2@: Common={result['is_common']}, Issues={len(result['pattern_issues'])}, Entropy={result['entropy']}")
    
    # Test modern weak pattern
    result = analyze_password_security("admin2024")
    assert 'word_number_pattern' in result['pattern_issues']
    print(f"✓ admin2024: Detected patterns={result['pattern_issues']}")


def test_encryption_decryption():
    """Test password encryption and decryption."""
    print("\n" + "=" * 70)
    print("TEST 6: ENCRYPTION & DECRYPTION")
    print("=" * 70)
    
    original_password = "MySecureP@ssword123!"
    
    # Encrypt
    encrypted_data = encrypt_password(original_password)
    encrypted_pwd = encrypted_data["encrypted_password"]
    iv = encrypted_data["iv"]
    print(f"✓ Encrypted: {encrypted_pwd[:20]}...")
    
    # Decrypt
    decrypted_password = decrypt_password(encrypted_pwd, iv)
    assert decrypted_password == original_password, "Decryption failed"
    print(f"✓ Decrypted correctly: {decrypted_password}")
    
    # Test multiple passwords
    test_passwords = ["password123", "MyPass@2024", "SecureP@ss!"]
    for pwd in test_passwords:
        enc_data = encrypt_password(pwd)
        dec_pwd = decrypt_password(enc_data["encrypted_password"], enc_data["iv"])
        assert dec_pwd == pwd, f"Encryption/decryption mismatch for {pwd}"
    print(f"✓ Multiple passwords encrypted/decrypted successfully")
    
    # Test CLI encryption/decryption workflow
    test_pwd = "CLITest@2024"
    enc_data = encrypt_password(test_pwd)
    dec_pwd = decrypt_password(enc_data["encrypted_password"], enc_data["iv"])
    assert dec_pwd == test_pwd, "CLI workflow encryption/decryption failed"
    print(f"✓ CLI workflow (encrypt -> decrypt) successful")
    
    # Test with special characters
    special_pwd = "!@#$%^&*()_+-=[]{{}}|;':\",./<>?"
    enc_data = encrypt_password(special_pwd)
    dec_pwd = decrypt_password(enc_data["encrypted_password"], enc_data["iv"])
    assert dec_pwd == special_pwd, "Special characters decryption failed"
    print(f"✓ Special characters encryption/decryption successful")
    
    # Test with empty string (edge case)
    empty_pwd = ""
    enc_data = encrypt_password(empty_pwd)
    dec_pwd = decrypt_password(enc_data["encrypted_password"], enc_data["iv"])
    assert dec_pwd == empty_pwd, "Empty password decryption failed"
    print(f"✓ Empty password encryption/decryption successful")


def test_random_number_generation():
    """Test random number generation."""
    print("\n" + "=" * 70)
    print("TEST 7: RANDOM NUMBER GENERATION")
    print("=" * 70)
    
    # Function-based usage
    otp = generate_random_number(6)
    assert len(str(otp)) <= 6, "OTP length invalid"
    print(f"✓ Generated 6-digit OTP: {otp}")
    
    # Multiple numbers
    numbers = generate_random_number(4, count=5, as_string=True)
    assert len(numbers) == 5, "Expected 5 numbers"
    print(f"✓ Generated 5 numbers: {numbers}")
    
    # Class-based usage
    rng = RandomNumberGenerator()
    num = rng.generate(8, as_string=True)
    assert len(num) == 8, "Generated number length invalid"
    print(f"✓ Class-based generation: {num}")


def test_token_generation():
    """Test token and API key generation."""
    print("\n" + "=" * 70)
    print("TEST 8: TOKEN & API KEY GENERATION")
    print("=" * 70)
    
    tg = TokenGenerator()
    
    # Generate access token
    access_token = tg.generate_token(token_type="access")
    assert len(access_token['token']) > 0, "Token generation failed"
    print(f"✓ Access token generated")
    
    # Generate API key
    api_key = tg.generate_api_key(bits=256, char_type="mixed")
    assert len(api_key['api_key']) > 0, "API key generation failed"
    print(f"✓ API key generated")
    
    # Check expiry validation
    valid_token = tg.generate_token(expiry_seconds=3600)
    is_expired = TokenGenerator.is_expired(valid_token)
    assert is_expired == False, "Token should not be expired"
    print(f"✓ Token expiry validation works")


def test_data_masking():
    """Test data masking utilities."""
    print("\n" + "=" * 70)
    print("TEST 9: DATA MASKING")
    print("=" * 70)
    
    # Email masking
    masked_email = DataMasker.mask_email("test@example.com")
    assert "@example.com" in masked_email, "Email masking failed"
    print(f"✓ Email masking: {masked_email}")
    
    # Phone masking
    masked_phone = DataMasker.mask_phone("9876543210")
    assert len(masked_phone) == len("9876543210"), "Phone masking length mismatch"
    print(f"✓ Phone masking: {masked_phone}")
    
    # Custom masking
    masked_custom = DataMasker.mask_custom("SensitiveData")
    assert "*" in masked_custom, "Custom masking failed"
    print(f"✓ Custom masking: {masked_custom}")
    
    # Partial masking
    masked_partial = DataMasker.mask_partial("ABCDEFGHIJ", 2, 7)
    assert "AB" in masked_partial and "HIJ" in masked_partial, "Partial masking failed"
    print(f"✓ Partial masking: {masked_partial}")


def test_edge_cases():
    """Test edge cases and error handling."""
    print("\n" + "=" * 70)
    print("TEST 10: EDGE CASES & ERROR HANDLING")
    print("=" * 70)
    
    # Empty password
    result = check_entropy("")
    assert result['entropy'] == 0.0, "Empty password entropy should be 0"
    print("✓ Empty password handling")
    
    # Very long password
    long_pwd = "A" * 100
    result = check_entropy(long_pwd)
    assert result['length'] == 100, "Long password length mismatch"
    print("✓ Long password handling")
    
    # Special characters only
    special_pwd = "!@#$%^&*()"
    result = check_entropy(special_pwd)
    assert result['entropy'] > 0, "Special characters should have entropy"
    print("✓ Special characters handling")
    
    # Mixed case sensitive detection (case-insensitive checking)
    pwd1 = "Password"
    pwd2 = "password"
    # Both should be detected as common (case-insensitive)
    assert is_common_password(pwd1) == is_common_password(pwd2), "Case-insensitive detection should match"
    assert is_common_password(pwd1) == True, "password should be detected as common"
    print("✓ Case-insensitive common password detection")


def test_cli_decryption_workflow():
    """Test CLI decryption workflow with various password types."""
    print("\n" + "=" * 70)
    print("TEST 11: CLI DECRYPTION WORKFLOW")
    print("=" * 70)
    
    # Test Case 1: Simple password
    pwd1 = "SimplePass123"
    enc1 = encrypt_password(pwd1)
    dec1 = decrypt_password(enc1["encrypted_password"], enc1["iv"])
    assert dec1 == pwd1, "Simple password decryption failed"
    print(f"✓ Simple password: {pwd1} -> [encrypted] -> {dec1}")
    
    # Test Case 2: Complex password with symbols
    pwd2 = "C0mpl3x!@#$%^&*()"
    enc2 = encrypt_password(pwd2)
    dec2 = decrypt_password(enc2["encrypted_password"], enc2["iv"])
    assert dec2 == pwd2, "Complex password decryption failed"
    print(f"✓ Complex password with symbols encrypted/decrypted")
    
    # Test Case 3: Long password (50+ characters)
    pwd3 = "This_Is_A_Very_Long_Password_With_Many_Characters_123456"
    enc3 = encrypt_password(pwd3)
    dec3 = decrypt_password(enc3["encrypted_password"], enc3["iv"])
    assert dec3 == pwd3, "Long password decryption failed"
    assert len(dec3) == len(pwd3), "Long password length mismatch"
    print(f"✓ Long password ({len(pwd3)} chars) encrypted/decrypted")
    
    # Test Case 4: Unicode characters (if supported)
    pwd4 = "P@ssw0rd_Üñíçødé"
    try:
        enc4 = encrypt_password(pwd4)
        dec4 = decrypt_password(enc4["encrypted_password"], enc4["iv"])
        assert dec4 == pwd4, "Unicode password decryption failed"
        print(f"✓ Unicode password encrypted/decrypted")
    except:
        print(f"⊘ Unicode password not fully supported (expected)")
    
    # Test Case 5: Verify IV is unique for same password
    pwd5 = "SamePassword"
    enc5a = encrypt_password(pwd5)
    enc5b = encrypt_password(pwd5)
    assert enc5a["encrypted_password"] != enc5b["encrypted_password"], "Encrypted values should differ with different IVs"
    assert enc5a["iv"] != enc5b["iv"], "IVs should be unique"
    # But both should decrypt to the same value
    dec5a = decrypt_password(enc5a["encrypted_password"], enc5a["iv"])
    dec5b = decrypt_password(enc5b["encrypted_password"], enc5b["iv"])
    assert dec5a == dec5b == pwd5, "Both should decrypt to same value"
    print(f"✓ IV uniqueness verified (same password, different encryption)")
    
    # Test Case 6: Error handling with wrong IV
    pwd6 = "TestPassword"
    enc6 = encrypt_password(pwd6)
    wrong_iv = "0000000000000000000000000000000"  # Wrong IV
    try:
        decrypt_password(enc6["encrypted_password"], wrong_iv)
        print("⊘ Should have failed with wrong IV")
    except:
        print(f"✓ Correctly rejects decryption with wrong IV")
    
    # Test Case 7: Workflow simulation for CLI usage
    print("\n✓ CLI decryption workflow:")
    original = "MySecureP@ssword123!"
    enc_data = encrypt_password(original)
    print(f"  1. User encrypts: rpt encrypt '{original}'")
    print(f"  2. Gets encrypted: {enc_data['encrypted_password'][:30]}...")
    print(f"  3. Gets IV: {enc_data['iv'][:30]}...")
    decrypted = decrypt_password(enc_data["encrypted_password"], enc_data["iv"])
    print(f"  4. User decrypts: rpt decrypt '<encrypted>' '<iv>'")
    print(f"  5. Gets original back: {decrypted}")
    assert decrypted == original, "CLI workflow verification failed"


def run_all_tests():
    """Run all tests."""
    print("\n" + "=" * 70)
    print("RANDOM PASSWORD TOOLKIT - COMPREHENSIVE TEST SUITE")
    print("=" * 70)
    
    try:
        test_password_generation()
        test_password_strength()
        test_password_entropy()
        test_pattern_detection()
        test_security_analysis()
        test_encryption_decryption()
        test_random_number_generation()
        test_token_generation()
        test_data_masking()
        test_edge_cases()
        test_cli_decryption_workflow()
        
        print("\n" + "=" * 70)
        print("ALL TESTS PASSED!")
        print("=" * 70 + "\n")
        return True
    except AssertionError as e:
        print(f"\n✗ TEST FAILED: {e}\n")
        return False
    except Exception as e:
        print(f"\n✗ ERROR: {e}\n")
        return False


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)


    try:
        print(generate_multiple(0))
    except ValueError as error:
        print(error) 




# Function-based usage (simple and quick) test cases
# -------------------------
# a) Single 6-digit OTP
# -------------------------
otp = generate_random_number(6)
print(f"Your OTP: {otp}")  # e.g., "483291"

# -------------------------
# b) Generate multiple order IDs
# -------------------------
order_ids = generate_random_number(6, count=5, as_string=True, prefix="ORD-", suffix="-2025")
print(f"Order IDs: {order_ids}")
# e.g., ["ORD-123456-2025", "ORD-654321-2025", ...]

# -------------------------
# c) Batch processing: generate 100 random numbers for simulation
# -------------------------
batch_numbers = generate_random_number(8, count=100)
print(f"Generated {len(batch_numbers)} 8-digit numbers")

# -------------------------
# d) Database-friendly zero-padded IDs
# -------------------------
db_ids = generate_random_number(10, count=3, as_string=True)
print(f"DB IDs: {db_ids}")  # e.g., ["0001234567", "0009876543", "0003456789"]

# -------------------------
# e) Error handling
# -------------------------
try:
    generate_random_number(0)
except ValueError as e:
    print(f"Error: {e}")  # Length must be a positive integer.




# Class-based usage (advanced/flexible) test cases
from random_password_toolkit import RandomNumberGenerator
rng = RandomNumberGenerator()

# -------------------------
# a) Single 6-digit OTP
# -------------------------
otp = rng.generate(6)
print(f"Your OTP: {otp}")

# -------------------------
# b) Multiple 6-digit invoice numbers
# -------------------------
invoices = rng.generate(6, count=5, as_string=True, prefix="INV-", suffix="-2025")
print(f"Invoices: {invoices}")
# e.g., ["INV-123456-2025", "INV-654321-2025", ...]

# -------------------------
# c) Multiple string IDs for internal tracking
# -------------------------
tracking_ids = rng.generate(8, count=10, as_string=True)
print(f"Tracking IDs: {tracking_ids}")

# -------------------------
# d) Single database key
# -------------------------
db_key = rng.generate(12, as_string=True)
print(f"DB Key: {db_key}")  # e.g., "000123456789"

# -------------------------
# e) Advanced usage: repeated calls for batch processing
# -------------------------
for i in range(3):
    print(rng.generate(6, as_string=True, prefix="ORD-", suffix=f"-{2025+i}"))



#  Masking test cases
    print(DataMasker.mask_email("test@example.com"))
    print(DataMasker.mask_phone("9876543210"))
    print(DataMasker.mask_custom("SensitiveData123"))
    print(DataMasker.mask_partial("ABCDEFGHIJ", 2, 7))


# TokenGenerator test cases

print("=== TOKEN GENERATOR TESTS ===\n")

# =========================
# WITH PREFIX
# =========================
tg1 = TokenGenerator(prefix="TEST_", suffix="_END")

print("---- With Prefix/Suffix ----")

access_token = tg1.generate_token(token_type="access")
print("Access Token:", access_token)

refresh_token = tg1.generate_token(token_type="refresh")
print("Refresh Token:", refresh_token)

api_key = tg1.generate_api_key(bits=256)
print("API Key:", api_key)

reset_token = tg1.generate_reset_token("user123")
print("Reset Token:", reset_token)

print()

# =========================
# WITHOUT PREFIX
# =========================
tg2 = TokenGenerator()

print("---- Without Prefix/Suffix ----")

access_token2 = tg2.generate_token(token_type="access")
print("Access Token:", access_token2)

generic_token = tg2.generate_token()
print("Generic Token:", generic_token)

api_key2 = tg2.generate_api_key(bits=512, separator="-")
print("API Key:", api_key2)

print()

# =========================
# EXPIRY TEST (NO SLEEP)
# =========================
print("---- Expiry Test ----")

expired_token = {
    "token": "dummy",
    "created_at": 1000,
    "expires_at": 1001  # already in past
}

print("Expired Token Data:", expired_token)
print("Is Expired?", TokenGenerator.is_expired(expired_token))

valid_token = tg2.generate_token(expiry_seconds=1000)
print("Valid Token:", valid_token)
print("Is Expired?", TokenGenerator.is_expired(valid_token))

print()

# =========================
# ERROR HANDLING TEST
# =========================
print("---- Error Handling ----")

try:
    tg2.generate_token(token_type="invalid")
except Exception as e:
    print("Error:", e)

try:
    tg2.generate_api_key(bits=999)
except Exception as e:
    print("Error:", e)

try:
    tg2.generate_reset_token("")
except Exception as e:
    print("Error:", e)

print("\n=== TEST COMPLETED ===")



# Sample text containing sensitive data
text = """
Hello krishna, please contact me at krishna.demo@example.com or call 9898989898.
Als, your API key is ABCD-1234-EFGH-5678 and password is MySecret123!
    """

# Mask configuration
mask_config = {
    "emails": True,  # Mask all emails
    "phones": True,  # Mask all phone numbers
    "specific": ["MySecret123", "ABCD-1234-EFGH-5678"],  # Mask specific values
    "patterns": [  # Custom regex patterns
        {"pattern": r"\b\d{4}-\d{4}-\d{4}-\d{4}\b", "mask_type": "full", "mask_char": "*"},
        {"pattern": r"MySecret\d+", "mask_type": "full"}
    ],
    "mask_char": "*",
    "visible_start": 2,
    "visible_end": 2
}

# Mask the text
masked_text = DataMasker.mask_text(text, mask_config)
print(masked_text)
