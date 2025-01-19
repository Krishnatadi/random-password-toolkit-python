**# Random Password Toolkit**

> ****Random Password Toolkit**** is a robust Python package for generating and managing random passwords with advanced features, including encryption, decryption, strength checking, and customizable generation options. This package is ideal for Python developers looking for a secure and feature-rich solution for handling password-related tasks.

---

**## Features**

- ****Random Password Generation****: Generate strong and secure passwords.
- ****Generate Multiple Passwords****: Create multiple passwords in bulk.
- ****Pronounceable Passwords****: Generate passwords that are easier to read and pronounce.
- ****Custom Password Generation****: Create passwords using a custom pool of characters.
- ****Password Strength Checker****: Evaluate the strength of passwords with actionable feedback.
- ****Password Encryption****: Secure passwords with AES-256 encryption.
- ****Password Decryption****: Decrypt encrypted passwords safely.
- ****Customizable Options****: Fully customizable password generation settings.

---

**## Benefits**

- ****Security****: Generate highly secure passwords to protect sensitive data.
- ****Flexibility****: Customize password generation to suit any application.
- ****Ease of Use****: Simple and intuitive API.
- ****Compatibility****: Works seamlessly with Python projects.
- ****Encryption & Decryption****: Securely store and retrieve passwords.

---

**## Installation**

This package is available through the [PyPI registry](__https://pypi.org/project/random-password-toolkit/__).

Before installing, ensure you have Python 3.6 or higher installed. You can download and install Python from [python.org](__https://www.python.org/downloads/__).

You can install the package using `pip`:

```bash
pip install random-password-toolkit

```

---

**## Options**

The following options can be used with the password generation functions:

| Option                  | Type     | Description                                             | Default |
|-------------------------|----------|---------------------------------------------------------|---------|
| `length`                | Integer  | Length of the password.                                 | `10`    |
| `numbers`               | Boolean  | Include numbers in the password.                        | `false` |
| `symbols`               | Boolean  | Include symbols in the password.                        | `false` |
| `lowercase`             | Boolean  | Include lowercase letters.                              | `true`  |
| `uppercase`             | Boolean  | Include uppercase letters.                              | `true`  |
| `excludeSimilarCharacters` | Boolean  | Exclude similar characters (e.g., 'i', 'l').         | `false` |
| `exclude`               | String   | Characters to exclude from the password.                | `''`    |
| `strict`                | Boolean  | Enforce at least one character from each pool.          | `false` |



**## Usage**

**### Importing the Package**

```python
from random_password_toolkit import (
    generate,
    generate_multiple,
    generate_pronounceable_password,
    generate_with_custom_pool,
    check_password_strength,
    encrypt_password,
    decrypt_password
)
```

---

**### 1. Generate a Random Password**

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

**### 2. Generate Multiple Passwords**

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

**### 3. Generate Pronounceable Passwords**

Create passwords that are easier to pronounce:

```python
pronounceable_password = generate_pronounceable_password(length=12)
print("Pronounceable password:", pronounceable_password)
# Output: bolozuna
```

---

**### 4. Generate Password with Custom Pool**

Generate passwords using a specific set of characters:

```python
generate_with_custom_pool_password = generate_with_custom_pool(length=8, custom_pool="p@ss")
print("Custom pool password:", generate_with_custom_pool_password)
# Output: 2c1ea3fb
```

---

**### 5. Check Password Strength**

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

**### 6. Encrypt a Password**

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

**### 7. Decrypt a Password**

Decrypt an encrypted password:

```python
// Decrypt the password using the returned IV
decrypted_password = decrypt_password(encrypted_data["encrypted_password"], encrypted_data["iv"])
print("Decrypted Password:", decrypted_password)
# Output: MySecureP@ssword123!
```

---
**### 8. Test generating zero secrets**

Test generating zero secrets

```python
try:
    print(generate_multiple(0))
except ValueError as error:
    print(error) 
# output: 'Amount must be greater than 0.'

```

---

- **GitHub Discussions**: Share use cases, report bugs, and suggest features.

We'd love to hear from you and see how you're using **Random Password Toolkit** in your projects!


## Issues and Feedback
For issues, feedback, and feature requests, please open an issue on our [GitHub Issues page](http://github.com/krishnatadi/random-password-toolkit-python/issues). We actively monitor and respond to community feedback.



---

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/Krishnatadi/random-password-toolkit-python/blob/main/LICENSE) file for details.
