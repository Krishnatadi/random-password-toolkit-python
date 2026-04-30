from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os
import json
from pathlib import Path

# Key and IV (Initialization Vector) settings
def _get_or_create_key():
    """
    Get encryption key from multiple sources (in order of priority):
    1. Environment variable: RPT_ENCRYPTION_KEY
    2. .env file in current directory with RPT_ENCRYPTION_KEY
    3. Local config file: ~/.rpt_config/encryption_key
    4. Generate new key if none exist (local storage only)
    """
    
    # Priority 1: Check environment variable
    env_key = os.getenv('RPT_ENCRYPTION_KEY')
    if env_key:
        try:
            return bytes.fromhex(env_key)
        except ValueError:
            print("Warning: RPT_ENCRYPTION_KEY is not a valid hex string")
    
    # Priority 2: Check .env file in current directory
    env_file = Path('.env')
    if env_file.exists():
        try:
            with open(env_file, 'r') as f:
                for line in f:
                    line = line.strip()
                    if line.startswith('RPT_ENCRYPTION_KEY='):
                        key_hex = line.split('=', 1)[1].strip('"\'')
                        return bytes.fromhex(key_hex)
        except Exception as e:
            print(f"Warning: Could not read .env file: {e}")
    
    # Priority 3: Check local config file
    key_dir = Path.home() / ".rpt_config"
    key_file = key_dir / "encryption_key"
    
    if key_file.exists():
        try:
            with open(key_file, 'r') as f:
                key_data = json.load(f)
                return bytes.fromhex(key_data['key'])
        except Exception as e:
            print(f"Warning: Could not read local key file: {e}")
    
    # Priority 4: Generate new key (stored locally only)
    new_key = os.urandom(32)  # 256-bit key
    try:
        key_dir.mkdir(exist_ok=True)
        with open(key_file, 'w') as f:
            json.dump({'key': new_key.hex()}, f)
        # Secure file permissions (read/write for owner only)
        os.chmod(key_file, 0o600)
        print(f"Generated new encryption key at: {key_file}")
        print("For production, set RPT_ENCRYPTION_KEY environment variable or use .env file")
    except Exception as e:
        print(f"Warning: Could not save key locally: {e}")
    
    return new_key

key = _get_or_create_key()
algorithm = algorithms.AES(key)
backend = default_backend()

def encrypt_password(password):
    """
    Encrypt a password using AES-256-CBC encryption.

    Args:
        password (str): The password to encrypt.

    Returns:
        dict: A dictionary containing the encrypted password (hex) and IV (hex).
    """
    iv = os.urandom(16)  # 128-bit IV
    cipher = Cipher(algorithm, modes.CBC(iv), backend=backend)
    encryptor = cipher.encryptor()

    # Padding the password to a multiple of the block size (16 bytes for AES)
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_password = padder.update(password.encode()) + padder.finalize()

    # Encrypt the padded password
    encrypted_password = encryptor.update(padded_password) + encryptor.finalize()

    return {
        "encrypted_password": encrypted_password.hex(),
        "iv": iv.hex()
    }

def decrypt_password(encrypted_password_hex, iv_hex):
    """
    Decrypt an encrypted password using AES-256-CBC.

    Args:
        encrypted_password_hex (str): The encrypted password in hexadecimal format.
        iv_hex (str): The initialization vector in hexadecimal format.

    Returns:
        str: The decrypted password.
    """
    iv = bytes.fromhex(iv_hex)  # Convert IV back to bytes
    cipher = Cipher(algorithm, modes.CBC(iv), backend=backend)
    decryptor = cipher.decryptor()

    # Decrypt the encrypted password
    encrypted_password = bytes.fromhex(encrypted_password_hex)
    decrypted_padded_password = decryptor.update(encrypted_password) + decryptor.finalize()

    # Remove padding from the decrypted password
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    decrypted_password = unpadder.update(decrypted_padded_password) + unpadder.finalize()

    return decrypted_password.decode()
