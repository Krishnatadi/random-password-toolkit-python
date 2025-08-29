import random

class RandomNumberGenerator:
    """
    Production-ready random number generator for exact length numbers.
    Supports multiple numbers at once, string formatting, and optional prefix/suffix.
    """

    def generate(self, length: int, count: int = 1, as_string: bool = False,
                 prefix: str = "", suffix: str = ""):
        """
        Generate one or more random numbers of exact length.

        Args:
            length (int): Number of digits per number.
            count (int): How many numbers to generate. Default is 1.
            as_string (bool): Return numbers as zero-padded strings if True.
            prefix (str): Optional prefix to add.
            suffix (str): Optional suffix to add.

        Returns:
            int or list[int] or list[str]: Random number(s) with optional formatting.

        Raises:
            ValueError: For invalid length or count.
        """
        if not isinstance(length, int) or length <= 0:
            raise ValueError("Length must be a positive integer.")
        if length > 18:
            raise ValueError("Length too large! Maximum allowed is 18 digits.")
        if not isinstance(count, int) or count <= 0:
            raise ValueError("Count must be a positive integer.")

        start = 10**(length - 1)
        end = (10**length) - 1

        numbers = []
        for _ in range(count):
            num = random.randint(start, end)
            if as_string:
                num_str = f"{num:0{length}d}"  # zero-padded
                numbers.append(f"{prefix}{num_str}{suffix}")
            else:
                numbers.append(num)

        return numbers[0] if count == 1 else numbers


# --------------------------
# Function wrapper for easy use
# --------------------------
_default_rng = RandomNumberGenerator()

def generate_random_number(length: int, count: int = 1, as_string: bool = False,
                           prefix: str = "", suffix: str = ""):
    """
    Simple function wrapper to generate random numbers quickly.

    Example:
        generate_random_number(6) -> 123456
        generate_random_number(6, count=5) -> [123456, 654321, ...]
        generate_random_number(6, as_string=True, prefix="INV-", suffix="-2025") -> ["INV-123456-2025"]
    """
    return _default_rng.generate(length, count, as_string, prefix, suffix)
