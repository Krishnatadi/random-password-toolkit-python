from setuptools import setup, find_packages

setup(
    name="random-password-toolkit",
    version="1.0.1",
    author="krishna Tadi",
    description="random-password-toolkit is a robust Python package for generating and managing random passwords with advanced features, including encryption, decryption, strength checking, and customizable generation options. This package is ideal for Python developers looking for a secure and feature-rich solution for handling password-related tasks.",
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
        "cryptography==38.0.0"
    ],
    keywords='""random password generator", "password strength checker", "password encryption", "password decryption", "secure password management", "customizable password generation", "Python password toolkit", "Random number generation"',
    project_urls={
    'Documentation': 'https://github.com/krishnatadi/random-password-toolkit-python#readme',
    'Source': 'https://github.com/krishnatadi/random-password-toolkit-python',
    'Issue Tracker': 'https://github.com/krishnatadi/random-password-toolkit-python/issues',
    },
    license='MIT'
)
