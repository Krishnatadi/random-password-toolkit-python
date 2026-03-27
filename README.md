![PyPI Version](https://img.shields.io/pypi/v/random-password-toolkit)
![Dependencies](https://img.shields.io/librariesio/release/pypi/random-password-toolkit)
![PyPI - License](https://img.shields.io/pypi/l/random-password-toolkit)

# Random Password Toolkit

> **Random Password Toolkit** is a robust AI-powered Python package designed for generating and managing secure passwords, tokens, API keys, and sensitive data. Developed for AI/GenAI workflows, LLMs, and RAG pipelines, it includes password generation, encryption & decryption, strength checking, secure token and API key generation with expiry support, and flexible data masking utilities. With highly customizable options and a simple API, this package is ideal for Python developers looking for a complete, secure, and AI-ready solution for authentication, security, and privacy-focused data handling.

---

## Features

### Password Features

- **Random Password Generation**: Generate strong and secure passwords.
- **Generate Multiple Passwords**: Create multiple passwords in bulk.
- **Pronounceable Passwords**: Generate passwords that are easier to read and pronounce.
- **Custom Password Generation**: Create passwords using a custom pool of characters.
- **Password Strength Checker**: Evaluate the strength of passwords with actionable feedback.
- **Password Encryption & Decryption**: Secure passwords with AES-256 encryption and safely decrypt them.
- **Customizable Options**: Fully customizable password generation settings.

### Random Number Generator Features

- **Exact Length Random Numbers**: Generate random numbers of any specified length.
- **Multiple Numbers at Once**: Generate multiple numbers in a single call.
- **Prefix and Suffix Support**: Add custom prefixes or suffixes to numbers.
- **String Formatting**: Return numbers as zero-padded strings for database-friendly IDs.
- **Flexible Usage**: Use via a simple function or through a class for advanced control.
- **Lightweight & Production-ready**: Fast generation without memory overhead.

### Token & API Key Features

- **Secure Token Generation**: Generate cryptographically secure tokens using Python’s `secrets` module.
- **Multiple Token Types**: Support for access, refresh, and generic tokens.
- **Expiry Support**: Define expiration time for tokens and API keys with built-in validation.
- **API Key Generator**: Generate secure API keys with configurable bit strength and character types.
- **Optional Prefix & Suffix**: Add identifiers for environment-based usage if needed.
- **Reset Token Generation**: Generate secure hash-based tokens for password reset workflows.
- **Expiry Validation**: Easily check whether a token or API key is expired.

### Data Masking Features

- **Email Masking**: Protect sensitive email data (e.g., `t***@example.com`).
- **Phone Masking**: Hide sensitive digits in phone numbers.
- **Custom Data Masking**: Mask any string with configurable visible portions.
- **Partial Masking**: Mask specific sections of a string using index ranges.
- **Privacy Utilities**: Useful for logs, UI display, and data protection.
- **AI/GenAI Ready**: Automatically preprocess and anonymize PII for LLMs, generative AI, and retrieval-augmented generation (RAG) systems.

---

## Benefits

- **Security**: Generate highly secure passwords, tokens, API keys, and unique numbers to protect sensitive data.
- **Flexibility**: Customize password, token, API key, number generation, and masking to suit any application.
- **Ease of Use**: Simple and intuitive API for both beginners and advanced users.
- **Compatibility**: Works seamlessly with Python projects.
- **Encryption & Decryption**: Securely store and retrieve passwords.
- **Token Management**: Generate and manage tokens with expiry support.
- **API Key Control**: Create structured, secure API keys suitable for production systems.
- **Data Privacy**: Protect sensitive information using masking utilities.
- **Random Numbers**: Generate secure, unique random numbers for IDs, tokens, or codes; supports custom formatting, bulk generation, and is suitable for production use.

---

## Installation

This package is available through the [PyPI registry](__https://pypi.org/project/random-password-toolkit/__).

Before installing, ensure you have Python 3.6 or higher installed. You can download and install Python from [python.org](__https://www.python.org/downloads/__).

You can install the package using `pip`:

```bash
pip install random-password-toolkit

```

---

## Options

### Password Generation Options

| Option                        | Type      | Description                                                | Default |
|-------------------------------|-----------|------------------------------------------------------------|---------|
| `length`                       | Integer   | Length of the password.                                    | 10      |
| `numbers`                      | Boolean   | Include numbers in the password.                           | false   |
| `symbols`                      | Boolean   | Include symbols in the password.                           | false   |
| `lowercase`                    | Boolean   | Include lowercase letters.                                 | true    |
| `uppercase`                    | Boolean   | Include uppercase letters.                                 | true    |
| `excludeSimilarCharacters`     | Boolean   | Exclude similar characters (e.g., 'i', 'l').               | false   |
| `exclude`                      | String    | Characters to exclude from the password.                   | ''      |
| `strict`                       | Boolean   | Enforce at least one character from each pool.             | false   |

---

### Random Number Generation Options

| Option                        | Type      | Description                                                | Default |
|-------------------------------|-----------|------------------------------------------------------------|---------|
| `length`                       | Integer   | Number of digits in the generated number.                  | 6       |
| `count`                        | Integer   | How many numbers to generate at once.                      | 1       |
| `as_string`                    | Boolean   | Return numbers as zero-padded strings instead of integers. | false   |
| `prefix`                       | String    | Optional string to prepend to each generated number.       | ''      |
| `suffix`                       | String    | Optional string to append to each generated number.        | ''      |

---

### Token Generation Options

| Option            | Type              | Description                                                     | Default  |
|-------------------|-------------------|-----------------------------------------------------------------|----------|
| `token_type`      | String            | Type of token: `generic`, `access`, `refresh`.                  | generic  |
| `length`          | Integer           | Length of the generated token.                                 | 32       |
| `expiry_seconds`  | Integer / Float   | Expiry time in seconds (auto-set for access/refresh if not given). | None     |
| `prefix`          | String (Optional) | Optional prefix to prepend to token.                           | ''       |
| `suffix`          | String (Optional) | Optional suffix to append to token.                           | ''       |

---

### API Key Generation Options

| Option            | Type              | Description                                                     | Default  |
|-------------------|-------------------|-----------------------------------------------------------------|----------|
| `bits`            | Integer           | Strength of the API key (128, 256, 512, 1024, 2048).            | 256      |
| `char_type`       | String            | Character set: `letters`, `numbers`, `alphanumeric`, `mixed`.   | mixed    |
| `separator`       | String (Optional) | Character used to separate groups (e.g., `-`).                  | None     |
| `group_size`      | Integer           | Number of characters per group when using separator.            | 4        |
| `expiry_seconds`  | Integer / Float   | Expiry time for the API key in seconds.                         | None     |
| `prefix`          | String (Optional) | Optional prefix to prepend to API key.                          | ''       |
| `suffix`          | String (Optional) | Optional suffix to append to API key.                          | ''       |

---

### Data Masking Options

| Option            | Type      | Description                                                                                       | Default |
|-------------------|-----------|---------------------------------------------------------------------------------------------------|---------|
| `visible_start`   | Integer   | Number of characters to keep visible at the start for custom masking.                             | 2       |
| `visible_end`     | Integer   | Number of characters to keep visible at the end for custom masking.                               | 2       |
| `mask_char`       | String    | Character used for masking.                                                                      | '*'     |
| `start`           | Integer   | Start index for partial masking.                                                                  | 0       |
| `end`             | Integer   | End index for partial masking.                                                                    | None    |
| `emails`          | Boolean   | Automatically detect and mask all email addresses in the text.                                    | False   |
| `phones`          | Boolean   | Automatically detect and mask all phone numbers in the text.                                      | False   |
| `specific`        | List      | List of specific values (e.g., passwords, tokens) to mask exactly as provided.                   | []      |
| `patterns`        | List      | List of custom regex patterns with masking type (`full`, `partial`, `custom`) and optional params. | []      |

---

## Usage

### Importing the Package

```python
from random_password_toolkit import (
    generate,
    generate_multiple,
    generate_pronounceable_password,
    generate_with_custom_pool,
    check_password_strength,
    encrypt_password,
    decrypt_password,
    generate_random_number,
    RandomNumberGenerator
)
```

---

### 1. Generate a Random Password

Generate a single random password with customizable options:
```python

generate_password = generate(5);
console.log(generate_password);
# Output: yKsmtgtDsJ
```

```python
generate_password = generate(
  length=10, 
  numbers=True, 
  symbols=False, 
  lowercase=True, 
  uppercase=True, 
  exclude_similar_characters=False, 
  exclude='', 
  strict=False)
print("Generated password:", generate_password)
# Output: @D8cP#9Zr2&f
```

---

### 2. Generate Multiple Passwords

Generate multiple passwords at once:
```python
generate_multiple_password = generateMultiple(5);
console.log(generate_multiple_password);
# Output: ['g8sFwLp4Rx', 'pR2zT9qMf7', ...]
```

```python
generate_multiple_password = generate_multiple(5, {"length": 8, "numbers": True, "uppercase": True})
print("Multiple passwords:", generate_multiple_password)
# Output: ['Fi:G+D1oTU','jec*<KSP:3','Z@ie>^]n7Q','6&J4O12}e?','K$9J|xDv|Y']
```

---

### 3. Generate Pronounceable Passwords

Create passwords that are easier to pronounce:

```python
pronounceable_password = generate_pronounceable_password(length=12)
print("Pronounceable password:", pronounceable_password)
# Output: bolozuna
```

---

### 4. Generate Password with Custom Pool

Generate passwords using a specific set of characters:

```python
generate_with_custom_pool_password = generate_with_custom_pool(length=8, custom_pool="p@ss")
print("Custom pool password:", generate_with_custom_pool_password)
# Output: 2c1ea3fb
```

---

### 5. Check Password Strength

Evaluate the strength of a password:

```python
password_strength_checker = "MySecureP@ssword123!"
result = check_password_strength(password_strength_checker)
print(f"Password: {password_strength_checker}")
print(f"Stength: {result}")
print(f"Strength: {result['strength']}")
print(f"Score: {result['score']}")
    
# Output: Very Strong
```

---

### 6. Encrypt a Password

Securely encrypt a password:

```python
password = "MySecureP@ssword123!"
//  Encrypt the password
encrypted_data = encrypt_password(password)
print("Encrypted Password:", encrypted_data["encrypted_password"])
print("IV:", encrypted_data["iv"])
''' Output:
Encrypted Password: 7de8fc05ab01ed48605fa1983c830e98e13716f507b59bbf1203f7f1361ee497
IV: dc23c48d84eed6b07d89c479af6c5845 '''
```

---

### 7. Decrypt a Password

Decrypt an encrypted password:

```python
// Decrypt the password using the returned IV
decrypted_password = decrypt_password(encrypted_data["encrypted_password"], encrypted_data["iv"])
print("Decrypted Password:", decrypted_password)
# Output: MySecureP@ssword123!
```

---
### 8. Test generating zero secrets

Test generating zero secrets

```python
try:
    print(generate_multiple(0))
except ValueError as error:
    print(error) 
# output: 'Amount must be greater than 0.'

```

---

### Random Number Generator Usage Examples

**1. Function-based usage (quick and simple)**

```python
from random_password_toolkit import generate_random_number

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

```

---

**2. Class-based usage (advanced/flexible)**

```python
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

```


---


---

### Token Generation Usage Examples

```python
from random_password_toolkit import TokenGenerator

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

api_key = tg1.generate_api_key(
    bits=512,                 # Key strength (128, 256, 512, 1024, 2048)
    char_type="mixed",        # 'letters', 'numbers', 'alphanumeric', 'mixed'
    separator="-",            # Optional separator
    group_size=5,             # Group size for separator formatting
    expiry_seconds=3600       # Expiry time in seconds (1 hour)
)
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


api_key2 = tg2.generate_api_key(
    bits=512,                 # Key strength (128, 256, 512, 1024, 2048)
    char_type="mixed",        # 'letters', 'numbers', 'alphanumeric', 'mixed'
    separator="-",            # Optional separator
    group_size=5,             # Group size for separator formatting
    expiry_seconds=3600       # Expiry time in seconds (1 hour)
)
print("API Key:", api_key2)

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

```

---

### Masking Data Usage Examples


``` python
from random_password_toolkit import DataMasker

print(DataMasker.mask_email("test@example.com"))
print(DataMasker.mask_phone("9876543210"))
print(DataMasker.mask_custom("SensitiveData123"))
print(DataMasker.mask_partial("ABCDEFGHIJ", 2, 7))



# Sample text containing sensitive data
text = """
    Hello krishna, please contact me at krishna.demo@example.com or call 9898989898.
    Also, your API key is ABCD-1234-EFGH-5678 and password is MySecret123!
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

#output
Hello John, please contact me at j***@example.com or call 98******10.
Also, your API key is **************** and password is ***********!

```

---


## Where This Package Can Be Used

- **Web & Mobile Applications**: User authentication, OTPs, temporary passwords.
- **E-commerce & SaaS Platforms**: Order/invoice numbers, discount codes, subscription IDs.
- **Databases & Backend Systems**: Unique numeric identifiers, zero-padded IDs, batch data generation.
- **Security & IT Systems**: Password management, API keys, tokens, temporary credentials.
- **QA & Testing**: Automated test data, simulations, mock data for staging environments.
- **Educational & Research Use**: Teaching secure password generation, cryptography demos, numeric datasets.
- **Business & Operations**: Shipment tracking, inventory codes, survey or contest codes.
- **Developer Tools & Automation**: CLI tools, CI/CD pipelines, auto-generating credentials or IDs.
- **AI & Machine Learning Pipelines**: Preprocessing sensitive data before sending to LLMs, GenAI, or RAG systems.
- **Generative AI Applications**: Masking PII and confidential information for AI content generation or model training.
- **LLM & RAG Workflows**: Ensuring safe data handling and privacy compliance when querying or indexing documents.
- **AI/GenAI Research**: Data anonymization for training, testing, and evaluating generative AI models.

> **Note**: This module has countless use cases and is widely adopted by enterprises for internal applications. It can be easily integrated into various systems, offering secure passwords, unique numbers, and automation capabilities.



---

- **GitHub Discussions**: Share use cases, report bugs, and suggest features.

We'd love to hear from you and see how you're using **Random Password Toolkit** in your projects!


## Issues and Feedback
For issues, feedback, and feature requests, please open an issue on our [GitHub Issues page](http://github.com/krishnatadi/random-password-toolkit-python/issues). We actively monitor and respond to community feedback.



---

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/Krishnatadi/random-password-toolkit-python/blob/main/LICENSE) file for details.
