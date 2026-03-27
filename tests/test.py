from random_password_toolkit import (
    generate,
    generate_multiple,
    generate_pronounceable_password,
    generate_with_custom_pool,
    check_password_strength,
    encrypt_password,
    decrypt_password,
    RandomNumberGenerator,
    generate_random_number,
    TokenGenerator,
    DataMasker,
)

if __name__ == "__main__":
    # Test generate functions
    generate_password = generate(length=10, numbers=True, symbols=False, lowercase=True, uppercase=True, exclude_similar_characters=False, exclude='', strict=False)
    print("Generated password:", generate_password)
    
    # Test generate_multiple function
    generate_multiple_password = generate_multiple(5, {"length": 8, "numbers": True, "uppercase": True})
    print("Multiple passwords:", generate_multiple_password)
    
    # Test generate_pronounceable_password functions
    pronounceable_password = generate_pronounceable_password(length=12)
    print("Pronounceable password:", pronounceable_password)
    
    # Test generate_with_custom_pool function
    generate_with_custom_pool_password = generate_with_custom_pool(length=8, custom_pool="p@ss")
    print("Custom pool password:", generate_with_custom_pool_password)

    # Test check_password_strength function
    password_strength_checker = "MySecureP@ssword123!"
    result = check_password_strength(password_strength_checker)
    print(f"Password: {password_strength_checker}")
    print(f"Strength: {result['strength']}")
    print(f"Score: {result['score']}")
    print(f"Stength: {result}")

    # Test encrypt_password and decrypt_password functions
    password = "MySecureP@ssword123!"
    
    # Encrypt the password
    encrypted_data = encrypt_password(password)
    print("Encrypted Password:", encrypted_data["encrypted_password"])
    print("IV:", encrypted_data["iv"])

    # Decrypt the password
    decrypted_password = decrypt_password(encrypted_data["encrypted_password"], encrypted_data["iv"])
    print("Decrypted Password:", decrypted_password)


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
