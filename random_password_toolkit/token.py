import secrets
import string
import time
import math
import hashlib


class TokenGenerator:
    """
    Unified Token Generator for:
    - Generic tokens
    - Access tokens
    - Refresh tokens
    - API keys

    Notes:
    - Tokens are simple and secure (no formatting complexity)
    - API keys support advanced customization
    """

    def __init__(self, prefix=None, suffix=None):
        if prefix is not None and not isinstance(prefix, str):
            raise TypeError("prefix must be a string or None")

        if suffix is not None and not isinstance(suffix, str):
            raise TypeError("suffix must be a string or None")

        self.prefix = prefix or ""
        self.suffix = suffix or ""

    # =========================
    # TOKEN GENERATION
    # =========================
    def generate_token(self, token_type="generic", length=32, expiry_seconds=None):
        """
        Generate token (generic / access / refresh)
        """

        if token_type not in ["generic", "access", "refresh"]:
            raise ValueError("token_type must be: generic, access, refresh")

        if not isinstance(length, int) or length <= 0:
            raise ValueError("length must be a positive integer")

        # Default expiry
        if expiry_seconds is None:
            if token_type == "access":
                expiry_seconds = 900  # 15 mins
            elif token_type == "refresh":
                expiry_seconds = 7 * 24 * 60 * 60  # 7 days

        if expiry_seconds is not None:
            if not isinstance(expiry_seconds, (int, float)) or expiry_seconds <= 0:
                raise ValueError("expiry_seconds must be a positive number")

        raw = secrets.token_urlsafe(length)
        created_at = int(time.time())

        token = f"{self.prefix}{raw}{self.suffix}"

        data = {
            "token": token,
            "type": token_type,
            "created_at": created_at
        }

        if expiry_seconds:
            data["expires_at"] = created_at + int(expiry_seconds)

        return data

    # =========================
    # API KEY GENERATOR
    # =========================
    def generate_api_key(
        self,
        bits=256,
        char_type="mixed",
        separator=None,
        group_size=4,
        expiry_seconds=None
    ):
        """
        Generate API key with entropy-based strength
        """

        valid_bits = [128, 256, 512, 1024, 2048]
        if bits not in valid_bits:
            raise ValueError(f"bits must be one of {valid_bits}")

        if char_type not in ["letters", "numbers", "mixed", "alphanumeric"]:
            raise ValueError("Invalid char_type")

        if separator is not None and not isinstance(separator, str):
            raise TypeError("separator must be string")

        if not isinstance(group_size, int) or group_size <= 0:
            raise ValueError("group_size must be positive integer")

        if expiry_seconds is not None:
            if not isinstance(expiry_seconds, (int, float)) or expiry_seconds <= 0:
                raise ValueError("expiry_seconds must be positive")

        # Character pool
        if char_type == "letters":
            pool = string.ascii_letters
        elif char_type == "numbers":
            pool = string.digits
        elif char_type == "alphanumeric":
            pool = string.ascii_letters + string.digits
        else:
            pool = string.ascii_letters + string.digits + "!@#$%^&*()"

        # Entropy-based length
        length = math.ceil(bits / math.log2(len(pool)))

        raw = ''.join(secrets.choice(pool) for _ in range(length))

        # Apply separator
        if separator:
            raw = separator.join(
                raw[i:i + group_size] for i in range(0, len(raw), group_size)
            )

        key = f"{self.prefix}{raw}{self.suffix}"
        created_at = int(time.time())

        result = {
            "api_key": key,
            "bits": bits,
            "strength": (
                "weak" if bits <= 128 else
                "medium" if bits <= 256 else
                "strong" if bits <= 512 else
                "very_strong"
            ),
            "char_type": char_type,
            "created_at": created_at
        }

        if expiry_seconds:
            result["expires_at"] = created_at + int(expiry_seconds)

        return result

    # =========================
    # RESET TOKEN
    # =========================
    def generate_reset_token(self, user_identifier):
        if not isinstance(user_identifier, str) or not user_identifier.strip():
            raise ValueError("user_identifier must be a non-empty string")

        data = f"{user_identifier}{secrets.token_hex(16)}{time.time()}"
        return hashlib.sha256(data.encode()).hexdigest()

    # =========================
    # COMMON EXPIRY CHECK
    # =========================
    @staticmethod
    def is_expired(data):
        if not isinstance(data, dict):
            raise TypeError("data must be a dictionary")

        if "expires_at" not in data:
            return False

        if not isinstance(data["expires_at"], (int, float)):
            raise ValueError("expires_at must be a valid timestamp")

        return time.time() > data["expires_at"]