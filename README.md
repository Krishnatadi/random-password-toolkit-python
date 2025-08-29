![PyPI Version](https://img.shields.io/pypi/v/random-password-toolkit)
![Dependencies](https://img.shields.io/librariesio/release/pypi/random-password-toolkit)
![PyPI - License](https://img.shields.io/pypi/l/random-password-toolkit)

# Random Password Toolkit

> **Random Password Toolkit** is a robust Python package for generating and managing random passwords, and now also generating random numbers with advanced features. It includes encryption, decryption, strength checking, customizable password generation, and flexible random number generation. This package is ideal for Python developers looking for a secure and feature-rich solution for handling password and number generation tasks.

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


---

## Benefits

- **Security**: Generate highly secure passwords and unique numbers to protect sensitive data.
- **Flexibility**: Customize password and number generation to suit any application.
- **Ease of Use**: Simple and intuitive API for both beginners and advanced users.
- **Compatibility**: Works seamlessly with Python projects.
- **Encryption & Decryption**: Securely store and retrieve passwords.
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
| `excludeSimilarCharacters`     | Boolean   | Exclude similar characters (e.g., 'i', 'l').                | false   |
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


## Where This Package Can Be Used

- **Web & Mobile Applications**: User authentication, OTPs, temporary passwords.
- **E-commerce & SaaS Platforms**: Order/invoice numbers, discount codes, subscription IDs.
- **Databases & Backend Systems**: Unique numeric identifiers, zero-padded IDs, batch data generation.
- **Security & IT Systems**: Password management, API keys, tokens, temporary credentials.
- **QA & Testing**: Automated test data, simulations, mock data for staging environments.
- **Educational & Research Use**: Teaching secure password generation, cryptography demos, numeric datasets.
- **Business & Operations**: Shipment tracking, inventory codes, survey or contest codes.
- **Developer Tools & Automation**: CLI tools, CI/CD pipelines, auto-generating credentials or IDs.

> **Note**: This module has countless use cases and is widely adopted by enterprises for internal applications. It can be easily integrated into various systems, offering secure passwords, unique numbers, and automation capabilities.



---

- **GitHub Discussions**: Share use cases, report bugs, and suggest features.

We'd love to hear from you and see how you're using **Random Password Toolkit** in your projects!


## Issues and Feedback
For issues, feedback, and feature requests, please open an issue on our [GitHub Issues page](http://github.com/krishnatadi/random-password-toolkit-python/issues). We actively monitor and respond to community feedback.



---

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/Krishnatadi/random-password-toolkit-python/blob/main/LICENSE) file for details.
