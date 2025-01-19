from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os

# Key and IV (Initialization Vector) settings
key = os.urandom(32)  # 256-bit key
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

