from setuptools import setup, find_packages

setup(
    name="random-password-toolkit",
    version="1.0.4",
    author="krishna Tadi",
    description="AI Toolkit: random-password-toolkit is a robust Python package for generating secure passwords, tokens, and API keys. Includes encryption/decryption, strength checking, expiry-based token generation, and flexible data masking utilities for LLM and RAG workflows.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/krishnatadi/random-password-toolkit-python",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "cryptography>=38.0.0"
    ],
    keywords='"AI toolkit", "password generator", "secure passwords", "password strength checker", "password encryption", "password decryption", "token generator", "API key generator", "data masking", "PII protection", "sensitive data protection", "privacy tools", "RAG", "LLM", "AI security", "Python security library", "secure password management", "custom password generation", "random number generation"',
    project_urls={
    'Documentation': 'https://github.com/krishnatadi/random-password-toolkit-python#readme',
    'Source': 'https://github.com/krishnatadi/random-password-toolkit-python',
    'Issue Tracker': 'https://github.com/krishnatadi/random-password-toolkit-python/issues',
    },
    license='MIT'
)
