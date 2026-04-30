![PyPI Version](https://img.shields.io/pypi/v/random-password-toolkit)
![Dependencies](https://img.shields.io/librariesio/release/pypi/random-password-toolkit)
![PyPI - License](https://img.shields.io/pypi/l/random-password-toolkit)

# Random Password Toolkit

> **Random Password Toolkit** is a robust AI-powered Python package & CLI tool designed for generating and managing secure passwords, tokens, API keys, and sensitive data. Developed for AI/GenAI workflows, LLMs, and RAG pipelines, it includes password generation, encryption & decryption, strength checking, secure token and API key generation with expiry support, and flexible data masking utilities. With highly customizable options and a simple API, this package is ideal for Python developers looking for a complete, secure, and AI-ready solution for authentication, security, and privacy-focused data handling.
---

## Features

### Password Features

- **Random Password Generation**: Generate strong and secure passwords.
- **Generate Multiple Passwords**: Create multiple passwords in bulk.
- **Pronounceable Passwords**: Generate passwords that are easier to read and pronounce.
- **Custom Password Generation**: Create passwords using a custom pool of characters.
- **Password Strength Checker**: Evaluate the strength of passwords with actionable feedback.
- **Password Entropy Checker**: Calculate Shannon entropy and detect security issues (common passwords, sequential patterns, repeated characters, low variety).
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

### Password Entropy Checker Options

| Option            | Type      | Description                                                                                       | Default |
|-------------------|-----------|---------------------------------------------------------------------------------------------------|---------||
| `password`        | String    | The password to analyze for entropy and security issues.                                          | N/A     |

**Returns:**
- `entropy` (float): Entropy value in bits
- `strength` (str): Strength classification (Very Weak, Weak, Medium, Strong, Very Strong)
- `issues` (list): List of detected security issues
- `suggestion` (str): Actionable improvement suggestions
- `length` (int): Password length
- `charset_size` (int): Size of character pool used

**Entropy Ranges:**
- 0-20 bits: Very Weak
- 20-40 bits: Weak
- 40-60 bits: Medium
- 60-90 bits: Strong
- 90+ bits: Very Strong

---

### Data Masking Options

| Option            | Type      | Description                                                                                       | Default |
|-------------------|-----------|---------------------------------------------------------------------------------------------------|---------|}
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


## Advanced CLI Tool

The package includes a powerful command-line interface (CLI) for quick password management and security analysis without writing code.

### CLI Commands

#### 1. Password Generation (gen, rpt, generate)
Generate random passwords from the command line:

```bash
# Generate 12-character password (default)
rpt gen

# Generate 16-character password with symbols
rpt gen 16 --with-symbols

# Generate 14-character password
rpt gen 14

# Generate without uppercase
rpt gen 12 --no-upper

# Combine options
rpt gen 20 --with-symbols --no-lower
```

**Output:**
```
======================================================================
PASSWORD GENERATOR
======================================================================

Generated Password:       Xk9#mL$pQ2@yRtW
Length:                   16 characters
Includes Numbers:         True
Includes Symbols:         True
Includes Uppercase:       True
Includes Lowercase:       True

Strength:                 Very Strong
Entropy:                  406.38 bits
======================================================================
```

#### 2. Password Strength Checking (check, strength)
Evaluate password security:

```bash
# Check password strength
rpt check "MyPassword123!"

# Using 'strength' command
rpt strength "password123"
```

**Output:**
```
======================================================================
PASSWORD STRENGTH CHECKER
======================================================================

Password:                 **************
Length:                   14 characters
Strength:                 Very Strong
Score:                    100/100
======================================================================
```

#### 3. Password Entropy & Pattern Analysis (entropy, analyze)
Deep security analysis using Shannon entropy and pattern detection:

```bash
# Analyze password entropy and patterns
rpt entropy "password123"

# Get JSON output
rpt entropy "password123" --json

# Using 'analyze' command
rpt analyze "admin2024"
```

**Output:**
```
======================================================================
PASSWORD ENTROPY & SECURITY ANALYSIS
======================================================================

Password Length:          11 characters
Character Pool Size:      36 characters
Entropy:                  186.4 bits
Strength:                 Very Strong

------------------------------------------------------------

SECURITY ANALYSIS:
Common Password:          YES
Pattern Issues:           3 detected
                          1. Common Password
                          2. Sequential Characters
                          3. Word+Number Pattern

------------------------------------------------------------

DETAILED ISSUES:
  1. Password is a common/weak password
  2. Password contains sequential characters
  3. Password follows word+number pattern (e.g., password123)

------------------------------------------------------------

RECOMMENDATION:
  Avoid sequential characters like '123' or 'abc' | Choose a unique password that's not in common password lists

======================================================================
```

#### 4. Password Encryption (encrypt, enc)
Encrypt passwords for secure storage:

```bash
# Encrypt a password
rpt encrypt "MySecurePassword"

# Using 'enc' shortcut
rpt enc "password123"
```

**Output:**
```
======================================================================
PASSWORD ENCRYPTION
======================================================================

Original Password:        ***
Encrypted Password:       fef041b0d0edc0c43992...
IV (Initialization Vector): 803a89d633171e0e2269...

Note: Save both values to decrypt later
======================================================================
```

#### 5. Password Decryption (decrypt, dec)
Decrypt encrypted passwords:

```bash
# Decrypt a password using encrypted password and IV
rpt decrypt "69bf152c698471b541a737f9a234c47a" "8542adf099b6f71af3fe2f08d5e46421"

# Using 'dec' shortcut
rpt dec "69bf152c698471b541a737f9a234c47a" "8542adf099b6f71af3fe2f08d5e46421"
```

**Output:**
```
======================================================================
PASSWORD DECRYPTION
======================================================================

Encrypted Password:       69bf152c698471b541a7...
IV (Initialization Vector): 8542adf099b6f71af3fe2f08d5e46421

Decrypted Password:       TestPassword456
======================================================================
```

**How Decryption Works:**

The decryption uses **AES-256-CBC encryption** with a persistent secret key stored on your computer:

1. **Encryption Key** (the "secret"): Stored in `~/.rpt_config/encryption_key` 
   - **NOT** part of the project (created at runtime)
   - Created automatically on **first encryption** in your home directory
   - Same key used for both encryption and decryption
   - Securely protected with read/write permissions for owner only (mode 0o600)

2. **Decryption Process:**
   - Takes your encrypted password (hex string)
   - Takes the IV (Initialization Vector - hex string you provide)
   - Reads the encryption key from `~/.rpt_config/encryption_key` (created on first use)
   - Combines all three to decrypt and recover your original password

3. **Why this works:**
   ```
   Encrypt: Original Password + Key + Random IV → Encrypted Data + IV
   Decrypt: Encrypted Data + Key + IV → Original Password
   ```

**Example Workflow:**
```bash
# Step 1: Encrypt (creates key file automatically if not exists)
$ rpt encrypt "MyDatabasePassword123"
# Creates: ~/.rpt_config/encryption_key (first time only)
Encrypted Password: 69bf152c698471b541a737f9a234c47a
IV: 8542adf099b6f71af3fe2f08d5e46421

# Step 2: Save these values somewhere safe (encrypted password + IV)
# The encryption key stays in ~/.rpt_config/encryption_key automatically

# Step 3: Decrypt anytime (uses the same persistent key)
$ rpt dec "69bf152c698471b541a737f9a234c47a" "8542adf099b6f71af3fe2f08d5e46421"
Decrypted Password: MyDatabasePassword123
```

**Important Security Notes:**

- **Don't lose the key file** at `~/.rpt_config/encryption_key` - if you delete it, you won't be able to decrypt previously encrypted passwords
- **Back up the key file** if you want to decrypt passwords on other computers
- **Keep the IV safe** - save the IV alongside your encrypted password
- ✓ The key file has restrictive permissions (readable/writable only by you)
- ✓ Different encrypted passwords use different random IVs for security
- ✓ Key file is created in user's home directory (never in git repo)

#### 6. Help & Usage (help, -h, --help)
Display help information:

```bash
rpt help
rpt -h
rpt --help
```

### Smart Pattern Detection

The CLI uses intelligent pattern detection to identify weak passwords:

- **Common Passwords**: Detects 15 most common weak passwords
- **Numeric-Only**: Identifies passwords with only numbers (e.g., 123456)
- **Alphabet-Only**: Detects passwords with only letters (e.g., password)
- **Repeated Characters**: Finds 3+ consecutive identical characters (e.g., aaaaaa)
- **Keyboard Patterns**: Detects keyboard walks (e.g., qwerty, asdfgh, 1qaz)
- **Sequential Characters**: Identifies numeric/letter sequences (e.g., 123, abc)
- **Word+Number Pattern**: Detects patterns like password123, admin2024
- **Word+Symbol Pattern**: Detects patterns like password@, admin#

### CLI Usage Examples

**Example 1: Generate and Analyze**
```bash
# Generate a password with symbols
rpt gen 16 --with-symbols

# Then analyze it
rpt entropy "Xk9#mL$pQ2@yRtW"
```

**Example 2: Quick Security Check**
```bash
# Check if password is secure
rpt check "MyPassword2024"
```

**Example 3: Encryption & Decryption Workflow**
```bash
# Step 1: Encrypt a sensitive password
rpt encrypt "MyDatabasePassword123"
# Output:
# Encrypted Password: 69bf152c698471b541a737f9a234c47a
# IV: 8542adf099b6f71af3fe2f08d5e46421

# Step 2: Save the encrypted password and IV somewhere safe

# Step 3: Later, decrypt when needed
rpt dec "69bf152c698471b541a737f9a234c47a" "8542adf099b6f71af3fe2f08d5e46421"
# Output: MyDatabasePassword123
```

**Example 4: Batch Analysis (via JSON)**
```bash
# Get JSON output for programmatic use
rpt entropy "test123" --json

# Output:
# {
#   "entropy": 109.47,
#   "strength": "Very Strong",
#   "issues": ["Password is a common/weak password"],
#   "suggestion": "Choose a unique password that's not in common password lists",
#   "length": 8,
#   "charset_size": 36,
#   "is_common": true,
#   "pattern_issues": ["common_password", "word_number_pattern"]
# }
```

---


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
    check_entropy,
    calculate_entropy,
    detect_issues,
    classify_strength,
    get_improvement_suggestions,
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

### 5a. Check Password Entropy (Information Entropy Analysis)

Perform comprehensive password security analysis using Shannon entropy:

```python
from random_password_toolkit import check_entropy

password = "MySecureP@ssword123!"
result = check_entropy(password)

print(f"Password: {password}")
print(f"Entropy: {result['entropy']} bits")
print(f"Strength: {result['strength']}")
print(f"Length: {result['length']}")
print(f"Charset Size: {result['charset_size']}")
print(f"Issues: {result['issues']}")
print(f"Suggestion: {result['suggestion']}")

# Output:
# Password: MySecureP@ssword123!
# Entropy: 89.45 bits
# Strength: Strong
# Length: 20
# Charset Size: 94
# Issues: []
# Suggestion: Password meets security standards.
```

**Individual Functions:**

```python
from random_password_toolkit import (
    calculate_entropy,
    detect_issues,
    classify_strength,
    get_improvement_suggestions
)

password = "weak123"

# Calculate entropy in bits
entropy = calculate_entropy(password)
print(f"Entropy: {entropy} bits")  # e.g., 18.5 bits

# Detect security issues
issues = detect_issues(password)
print(f"Issues: {issues}")
# Output: ['Password is too short (less than 8 characters)', 
#          'Password contains sequential characters',
#          'Password lacks character variety']

# Classify strength based on entropy
strength = classify_strength(entropy)
print(f"Strength: {strength}")  # Output: Weak

# Get improvement suggestions
suggestions = get_improvement_suggestions(password, entropy, issues)
print(f"Suggestion: {suggestions}")
# Output: Increase password length (currently 7 characters, aim for 12+) | 
#         Avoid sequential characters like '123' or 'abc' | 
#         Mix uppercase, lowercase, numbers, and symbols
```

**CLI Usage:**

```bash
# Run entropy checker from command line
rpt entropy "MySecureP@ssword123!"

# Output:
# ============================================================
# PASSWORD ENTROPY ANALYSIS REPORT
# ============================================================
#
# Password Length:          20 characters
# Character Pool Size:      94 characters
# Entropy:                  89.45 bits
# Strength:                 Strong
#
# ────────────────────────────────────────────────────────────
#
# ✓ No issues detected!
#
# ────────────────────────────────────────────────────────────
#
# SUGGESTION:
#    Password meets security standards.
#
# ============================================================

# Output JSON format
rpt entropy "password123" --json
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


## Testing

The package includes a comprehensive test suite. Run tests with:

```bash
python tests/test.py
```

**Test Coverage:**
- ✓ Password generation (basic, multiple, pronounceable, custom pool)
- ✓ Password strength checking
- ✓ Password entropy analysis
- ✓ Smart pattern detection (8 types)
- ✓ Comprehensive security analysis
- ✓ Encryption & decryption
- ✓ Random number generation
- ✓ Token & API key generation
- ✓ Data masking utilities
- ✓ Edge cases & error handling

---

## Deployment Guide: Encryption Key Management

### Overview

The encryption key storage strategy depends on your deployment environment:

| Environment | Storage | Best For |
|------------|---------|----------|
| **Local Development** | `~/.rpt_config/encryption_key` | Single user, local machine |
| **Server / Production** | Environment variable | Multi-user, application servers |
| **Docker / Kubernetes** | Mounted secrets or env vars | Containerized deployments |
| **Cloud (AWS/GCP/Azure)** | Secrets Manager | Enterprise, cloud-native |

---

### 1. Local Development (Current)

**How it works:**
```bash
# Key stored in user's home directory
~/.rpt_config/encryption_key

# Automatically created on first encryption
$ rpt encrypt "password123"
```

**Pros:**
- ✓ Automatic, no configuration needed
- ✓ User-isolated (each user has own key)
- ✓ Simple for development

**Cons:**
- ✗ Not suitable for shared servers
- ✗ Not portable across machines

---

### 2. Server / Production (Environment Variable)

**Setup:**

Create a `.env` file or set environment variable:
```bash
# Option A: Create a key and store in environment
export RPT_ENCRYPTION_KEY="your_256_bit_hex_key_here"

# Option B: Generate a new key
python -c "import os; print(os.urandom(32).hex())"
# Output: a1b2c3d4e5f6...

# Option C: Copy from existing key
cat ~/.rpt_config/encryption_key | python -c "import sys, json; print(json.load(sys.stdin)['key'])"
```

**Production deployment:**
```bash
# Export before running application
export RPT_ENCRYPTION_KEY="a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0u1v2w3x4y5z6"

# Run application
python myapp.py
# or
rpt encrypt "password"
```

---

### 3. Docker / Containerized

**Dockerfile:**
```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# Key provided at runtime
ENV RPT_ENCRYPTION_KEY=""

ENTRYPOINT ["python", "-m", "random_password_toolkit.cli"]
```

**Docker Compose:**
```yaml
version: '3.8'

services:
  app:
    build: .
    environment:
      RPT_ENCRYPTION_KEY: ${RPT_ENCRYPTION_KEY}
    volumes:
      - /secure/keys:/app/keys:ro
    
secrets:
  encryption_key:
    file: ./secrets/encryption_key

services:
  myapp:
    environment:
      RPT_ENCRYPTION_KEY_FILE: /run/secrets/encryption_key
```

**Run with secrets:**
```bash
# Generate key
openssl rand -hex 32 > secrets/encryption_key

# Run container
docker-compose up
```

---

### 4. Kubernetes (Cloud-Native)

**Create Secret:**
```bash
# Generate and create secret
kubectl create secret generic rpt-encryption-key \
  --from-literal=key=$(openssl rand -hex 32)

# Verify
kubectl get secret rpt-encryption-key
```

**Deployment manifest:**
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: password-app
spec:
  replicas: 3
  template:
    spec:
      containers:
      - name: app
        image: myapp:latest
        env:
        - name: RPT_ENCRYPTION_KEY
          valueFrom:
            secretKeyRef:
              name: rpt-encryption-key
              key: key
```

---

### 5. AWS Secrets Manager (Enterprise)

**Store key:**
```bash
# Store encryption key in AWS Secrets Manager
aws secretsmanager create-secret \
  --name random-password-toolkit/encryption-key \
  --secret-string "a1b2c3d4e5f6..."
```

**Retrieve in application:**
```python
import boto3
import json

def get_key_from_aws():
    client = boto3.client('secretsmanager')
    response = client.get_secret_value(
        SecretId='random-password-toolkit/encryption-key'
    )
    return bytes.fromhex(response['SecretString'])
```

---

### 6. Multi-User Server

**Problem:** Multiple users need to encrypt/decrypt same data

**Solution A: Shared Key in Secure Location**
```bash
# Store key with restricted permissions
sudo mkdir -p /etc/rpt
sudo bash -c 'echo "your_key_hex" > /etc/rpt/encryption_key'
sudo chmod 600 /etc/rpt/encryption_key
sudo chown root:root /etc/rpt/encryption_key

# Update application to read from there
export RPT_ENCRYPTION_KEY_FILE=/etc/rpt/encryption_key
```

**Solution B: Key Derivation (NOT recommended for sensitive data)**
```python
# Derive key from master password
import hashlib

master_password = os.getenv('RPT_MASTER_PASSWORD')
key = hashlib.sha256(master_password.encode()).digest()  # 32 bytes = 256 bits
```

---

### 7. Best Practices Summary

| Scenario | Recommendation | Example |
|----------|---|---------|
| **Solo Developer** | `~/.rpt_config/encryption_key` (default) | Local testing |
| **Team / Shared Server** | Environment variable + `.env` file | `export RPT_ENCRYPTION_KEY=...` |
| **Docker** | Docker Secrets + environment | `docker-compose.yml` |
| **Kubernetes** | K8s Secrets | `kubectl create secret` |
| **AWS/GCP/Azure** | Cloud Secrets Manager | AWS Secrets Manager, GCP Secret Manager |
| **Sensitive Production** | Hardware Security Module (HSM) | AWS CloudHSM, Azure Dedicated HSM |

---

### 8. Security Checklist

**Before deploying to production:**
- [ ] Encryption key is NOT in git repository
- [ ] Encryption key is NOT hard-coded in application
- [ ] Encryption key is stored in secure location (env var, secrets manager)
- [ ] Only necessary services/users have access to the key
- [ ] Key rotation policy is defined
- [ ] Backup of key exists in secure location
- [ ] Key is not logged or printed in debug output
- [ ] Access to key is audited/monitored
- [ ] Use HTTPS/TLS for transmitting encrypted passwords
- [ ] Database of encrypted passwords is backed up regularly

---

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/Krishnatadi/random-password-toolkit-python/blob/main/LICENSE) file for details.
