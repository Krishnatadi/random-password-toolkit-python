import random
import string
from typing import List

def generate(length=10, numbers=True, symbols=False, lowercase=True, uppercase=True, 
             exclude_similar_characters=False, exclude='', strict=False):
    if not (numbers or symbols or lowercase or uppercase):
        raise ValueError("At least one of numbers, symbols, lowercase, or uppercase must be True.")

    number_chars = '0123456789'
    symbol_chars = '!@#$%^&*()_+[]{}|;:,.<>?'
    lowercase_chars = string.ascii_lowercase
    uppercase_chars = string.ascii_uppercase

    character_pool = ''
    if numbers:
        character_pool += number_chars
    if symbols:
        character_pool += symbol_chars
    if lowercase:
        character_pool += lowercase_chars
    if uppercase:
        character_pool += uppercase_chars

    # Exclude similar characters
    if exclude_similar_characters:
        character_pool = character_pool.translate(str.maketrans('', '', 'ilLI|oO0'))

    # Exclude specific characters
    if exclude:
        character_pool = ''.join(c for c in character_pool if c not in exclude)

    if not character_pool:
        raise ValueError("Character pool is empty. Please check your options.")

    # Generate the password
    password = [random.choice(character_pool) for _ in range(length)]

    if strict:
        pools = []
        if numbers:
            pools.append(number_chars)
        if symbols:
            pools.append(symbol_chars)
        if lowercase:
            pools.append(lowercase_chars)
        if uppercase:
            pools.append(uppercase_chars)

        for pool in pools:
            password[random.randint(0, length - 1)] = random.choice(pool)

    return ''.join(password)

def generate_multiple(amount, options=None):
    if amount <= 0:
        raise ValueError("Amount must be greater than 0.")

    options = options or {}
    return [generate(**options) for _ in range(amount)]

def generate_pronounceable_password(length=10):
    vowels = 'aeiouAEIOU'
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    digits = '0123456789'

    password = []
    use_vowel = True

    for i in range(length):
        if use_vowel:
            char = random.choice(vowels)
        else:
            char = random.choice(consonants)

        # Randomly insert digits for added complexity
        if random.randint(0, 4) == 0 and (1 < i < length - 2):
            char = random.choice(digits)

        password.append(char)
        use_vowel = not use_vowel

    return ''.join(password)

def generate_with_custom_pool(length=10, custom_pool=''):
    if not custom_pool:
        raise ValueError("Custom character pool must not be empty.")

    return ''.join(random.choice(custom_pool) for _ in range(length))
