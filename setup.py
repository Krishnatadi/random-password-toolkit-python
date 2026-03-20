from setuptools import setup, find_packages

setup(
    name="random-password-toolkit",
    version="1.0.3",
    author="krishna Tadi",
    description="random-password-toolkit is a robust Python package for generating secure passwords, tokens, and API keys. Includes encryption/decryption, strength checking, expiry-based token generation, and flexible data masking utilities.",
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
    keywords='""random password generator", "password strength checker", "password encryption", "password decryption", "secure password management", "customizable password generation", "Python password toolkit", "Random number generation", "token generation", "API key generation", "data masking", "sensitive data protection", "privacy tools"',
    project_urls={
    'Documentation': 'https://github.com/krishnatadi/random-password-toolkit-python#readme',
    'Source': 'https://github.com/krishnatadi/random-password-toolkit-python',
    'Issue Tracker': 'https://github.com/krishnatadi/random-password-toolkit-python/issues',
    },
    license='MIT'
)
