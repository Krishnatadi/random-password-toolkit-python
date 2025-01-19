from setuptools import setup, find_packages

setup(
    name="random-password-toolkit",
    version="1.0.0",
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
    keywords='"color", "color conversion", "hex to rgb", "rgb to hex", "hex to hsl", "rgb to hsl", "hsl to rgb", "hsl to hex", "color parser", "random color", "web development", "design", "javascript", "css colors", "hex color", "rgb color", "hsl color", "colorcycle", "frontend tools", "color utilities", "color manipulation", "color names", "color library", "web design", "frontend development"',
    project_urls={
    'Documentation': 'https://github.com/krishnatadi/random-password-toolkit-python#readme',
    'Source': 'https://github.com/krishnatadi/random-password-toolkit-python',
    'Issue Tracker': 'https://github.com/krishnatadi/random-password-toolkit-python/issues',
    },
    license='MIT'
)
