"""
Utility class for masking sensitive data such as email, phone numbers,
or any custom string. Helps in protecting user privacy in logs, UI, etc.
"""
class DataMasker:

    @staticmethod
    def mask_email(email):
        """
        Mask an email address by hiding most of the username part.
        """
        if not isinstance(email, str):
            raise TypeError("Email must be a string")

        if "@" not in email:
            raise ValueError("Invalid email format: missing '@' symbol")

        try:
            name, domain = email.split("@")

            if not name or not domain:
                raise ValueError

            return name[0] + "***@" + domain

        except ValueError:
            raise ValueError("Invalid email format. Expected format: 'user@example.com'")

    @staticmethod
    def mask_phone(phone):
        """
        Mask a phone number by hiding middle digits.
        """
        if not isinstance(phone, str):
            raise TypeError("Phone number must be a string")

        if not phone.isdigit():
            raise ValueError("Phone number must contain only digits")

        if len(phone) < 4:
            return "*" * len(phone)

        return phone[:2] + "*" * (len(phone) - 4) + phone[-2:]

    @staticmethod
    def mask_custom(data, visible_start=2, visible_end=2, mask_char="*"):
        """
        Generic masking for any string.
        """
        if not isinstance(data, str):
            raise TypeError("Data must be a string")

        if not isinstance(visible_start, int) or not isinstance(visible_end, int):
            raise TypeError("visible_start and visible_end must be integers")

        if visible_start < 0 or visible_end < 0:
            raise ValueError("visible_start and visible_end must be non-negative")

        if not isinstance(mask_char, str) or len(mask_char) != 1:
            raise ValueError("mask_char must be a single character string")

        if not data:
            return ""

        if len(data) <= visible_start + visible_end:
            return mask_char * len(data)

        return (
            data[:visible_start] +
            mask_char * (len(data) - visible_start - visible_end) +
            data[-visible_end:]
        )

    @staticmethod
    def mask_partial(data, start=0, end=None, mask_char="*"):
        """
        Mask a specific portion of a string using index range.
        """
        if not isinstance(data, str):
            raise TypeError("Data must be a string")

        if not isinstance(start, int):
            raise TypeError("start must be an integer")

        if end is not None and not isinstance(end, int):
            raise TypeError("end must be an integer or None")

        if not isinstance(mask_char, str) or len(mask_char) != 1:
            raise ValueError("mask_char must be a single character string")

        if start < 0:
            raise ValueError("start index cannot be negative")

        if end is None:
            end = len(data)

        if end < start:
            raise ValueError("end index cannot be less than start index")

        if end > len(data):
            raise ValueError("end index exceeds data length")

        return (
            data[:start] +
            mask_char * (end - start) +
            data[end:]
        )