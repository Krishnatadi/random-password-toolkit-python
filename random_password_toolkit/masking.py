import re

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

    @staticmethod
    def mask_text(text, config):
        """
        Mask full text using config.

        config = {
            "emails": True,
            "phones": True,
            "mask_char": "*",

            "specific": ["value1", "value2"],

            "patterns": [
                {
                    "regex": r"...",
                    "type": "full | partial | custom",
                    "start": 0,
                    "end": 5,
                    "visible_start": 2,
                    "visible_end": 2
                }
            ]
        }
        """

        if not isinstance(text, str):
            raise TypeError("Text must be a string")

        result = text
        mask_char = config.get("mask_char", "*")

        # Emails
        if config.get("emails"):
            result = re.sub(
                r'\b[\w\.-]+@[\w\.-]+\.\w+\b',
                lambda m: DataMasker.mask_email(m.group()),
                result
            )

        # Phones
        if config.get("phones"):
            result = re.sub(
                r'\b\d{10,15}\b',
                lambda m: DataMasker.mask_phone(m.group()),
                result
            )

        # Specific values
        for item in config.get("specific", []):
            result = result.replace(
                item,
                DataMasker.mask_custom(item, mask_char=mask_char)
            )

        # Custom patterns
        for rule in config.get("patterns", []):
            regex = rule.get("regex")
            if not regex:
                continue

            def replacer(m):
                value = m.group()
                t = rule.get("type", "custom")

                if t == "full":
                    return mask_char * len(value)

                elif t == "partial":
                    return DataMasker.mask_partial(
                        value,
                        start=rule.get("start", 0),
                        end=rule.get("end"),
                        mask_char=mask_char
                    )

                else:
                    return DataMasker.mask_custom(
                        value,
                        visible_start=rule.get("visible_start", 2),
                        visible_end=rule.get("visible_end", 2),
                        mask_char=mask_char
                    )

            result = re.sub(regex, replacer, result)

        return result


# Example Usage
if __name__ == "__main__":
    text = """
    Email: john@example.com
    Phone: 9876543210
    Token: ABCD-1234-XYZ
    Password: mysecret123
    """

    config = {
        "emails": True,
        "phones": True,
        "specific": ["mysecret123"],
        "patterns": [
            {
                "regex": r"[A-Z]{4}-\d{4}-[A-Z]{3}",
                "type": "partial",
                "start": 2,
                "end": 10
            }
        ]
    }

    print(DataMasker.mask_text(text, config))