#!/usr/bin/env python3
"""
Advanced CLI tool for password management and security analysis.
Supports password generation, strength checking, entropy analysis, encryption, and more.
"""

import sys
import json
from .entropy import check_entropy, analyze_password_security
from .strength_checker import check_password_strength
from .generator import generate
from .encryptor import encrypt_password, decrypt_password


def print_help():
    """Display help information."""
    print("\n" + "=" * 70)
    print("RANDOM PASSWORD TOOLKIT - ADVANCED CLI")
    print("=" * 70)
    print("\nUSAGE: rpt <command> [options]")
    print("\nCOMMANDS:")
    print("\n  GENERATION:")
    print("    gen, rpt, generate    Generate random password")
    print("                          Usage: rpt gen [length] [--with-symbols] [--no-upper] [--no-lower]")
    print("                          Example: rpt gen 16 --with-symbols")
    print("\n  ANALYSIS:")
    print("    check, strength       Check password strength")
    print("                          Usage: rpt check <password>")
    print("                          Example: rpt check 'MyP@ssw0rd123'")
    print("\n    entropy, analyze      Analyze password entropy & patterns")
    print("                          Usage: rpt entropy <password> [--json]")
    print("                          Example: rpt entropy 'password123'")
    print("\n  ENCRYPTION:")
    print("    encrypt, enc          Encrypt a password")
    print("                          Usage: rpt encrypt <password>")
    print("                          Example: rpt encrypt 'MyPassword'")
    print("\n  DECRYPTION:")
    print("    decrypt, dec          Decrypt a password")
    print("                          Usage: rpt decrypt <encrypted_password> <iv>")
    print("                          Example: rpt decrypt 'fef041b0...' '803a89d6...'")
    print("\n  HELP:")
    print("    help, -h, --help      Show this help message")
    print("\n" + "=" * 70 + "\n")


def cmd_generate(args):
    """Generate a random password."""
    length = 12
    numbers = True
    symbols = False
    lowercase = True
    uppercase = True
    
    # Parse arguments
    if len(args) > 0:
        try:
            length = int(args[0])
        except ValueError:
            pass
    
    if '--with-symbols' in args or '-s' in args:
        symbols = True
    if '--no-upper' in args:
        uppercase = False
    if '--no-lower' in args:
        lowercase = False
    
    # Generate password
    password = generate(
        length=length,
        numbers=numbers,
        symbols=symbols,
        lowercase=lowercase,
        uppercase=uppercase,
        strict=True
    )
    
    print("\n" + "=" * 70)
    print("PASSWORD GENERATOR")
    print("=" * 70)
    print(f"\nGenerated Password:       {password}")
    print(f"Length:                   {len(password)} characters")
    print(f"Includes Numbers:         {numbers}")
    print(f"Includes Symbols:         {symbols}")
    print(f"Includes Uppercase:       {uppercase}")
    print(f"Includes Lowercase:       {lowercase}")
    
    # Analyze the generated password
    result = check_entropy(password)
    print(f"\nStrength:                 {result['strength']}")
    print(f"Entropy:                  {result['entropy']} bits")
    print("=" * 70 + "\n")


def cmd_strength(args):
    """Check password strength."""
    if not args:
        print("Error: Please provide a password")
        print("Usage: check <password>")
        return
    
    password = args[0]
    result = check_password_strength(password)
    
    print("\n" + "=" * 70)
    print("PASSWORD STRENGTH CHECKER")
    print("=" * 70)
    print(f"\nPassword:                 {'*' * len(password)}")
    print(f"Length:                   {len(password)} characters")
    print(f"Strength:                 {result['strength']}")
    print(f"Score:                    {result['score']}/100")
    print("=" * 70 + "\n")


def cmd_entropy(args):
    """Analyze password entropy and patterns."""
    if not args:
        print("Error: Please provide a password")
        print("Usage: entropy <password> [--json]")
        return
    
    password = args[0]
    json_output = '--json' in args
    
    # Get both entropy and pattern analysis
    entropy_result = check_entropy(password)
    security_result = analyze_password_security(password)
    
    if json_output:
        combined = {**entropy_result, **security_result}
        print(json.dumps(combined, indent=2))
        return
    
    # Display results in a formatted way
    print("\n" + "=" * 70)
    print("PASSWORD ENTROPY & SECURITY ANALYSIS")
    print("=" * 70)
    print(f"\nPassword Length:          {entropy_result['length']} characters")
    print(f"Character Pool Size:      {entropy_result['charset_size']} characters")
    print(f"Entropy:                  {entropy_result['entropy']} bits")
    print(f"Strength:                 {entropy_result['strength']}")
    
    print("\n" + "-" * 70)
    print("\nSECURITY ANALYSIS:")
    print(f"Common Password:          {'YES' if security_result['is_common'] else 'NO'}")
    
    if security_result['pattern_issues']:
        print(f"Pattern Issues:           {len(security_result['pattern_issues'])} detected")
        for i, issue in enumerate(security_result['pattern_issues'], 1):
            issue_name = issue.replace('_', ' ').title()
            print(f"                          {i}. {issue_name}")
    else:
        print(f"Pattern Issues:           None detected")
    
    print("\n" + "-" * 70)
    
    if entropy_result['issues']:
        print("\nDETAILED ISSUES:")
        for i, issue in enumerate(entropy_result['issues'], 1):
            print(f"  {i}. {issue}")
    else:
        print("\nNo issues detected!")
    
    print("\n" + "-" * 70)
    print(f"\nRECOMMENDATION:")
    print(f"  {entropy_result['suggestion']}")
    print("\n" + "=" * 70 + "\n")


def cmd_encrypt(args):
    """Encrypt a password."""
    if not args:
        print("Error: Please provide a password to encrypt")
        print("Usage: encrypt <password>")
        return
    
    password = args[0]
    encrypted_data = encrypt_password(password)
    
    print("\n" + "=" * 70)
    print("PASSWORD ENCRYPTION")
    print("=" * 70)
    print(f"\nOriginal Password:        {'*' * len(password)}")
    print(f"Encrypted Password:       {encrypted_data['encrypted_password']}")
    print(f"IV (Initialization Vector): {encrypted_data['iv']}")
    print("\nNote: Save both values to decrypt later")
    print("=" * 70 + "\n")


def cmd_decrypt(args):
    """Decrypt a password."""
    if len(args) < 2:
        print("Error: Please provide both encrypted password and IV")
        print("Usage: decrypt <encrypted_password> <iv>")
        return
    
    encrypted_password = args[0]
    iv = args[1]
    
    try:
        decrypted_password = decrypt_password(encrypted_password, iv)
        
        print("\n" + "=" * 70)
        print("PASSWORD DECRYPTION")
        print("=" * 70)
        print(f"\nEncrypted Password:       {encrypted_password[:20]}...")
        print(f"IV (Initialization Vector): {iv}")
        print(f"\nDecrypted Password:       {decrypted_password}")
        print("=" * 70 + "\n")
    except Exception as e:
        print(f"\nError: Failed to decrypt password")
        print(f"Details: {str(e)}")
        print("Please ensure both encrypted password and IV are correct.\n")


def main():
    """Main CLI entry point."""
    if len(sys.argv) < 2:
        print_help()
        return
    
    command = sys.argv[1].lower()
    args = sys.argv[2:] if len(sys.argv) > 2 else []
    
    # Command routing
    if command in ['help', '-h', '--help']:
        print_help()
    elif command in ['gen', 'rpt', 'generate']:
        cmd_generate(args)
    elif command in ['check', 'strength']:
        cmd_strength(args)
    elif command in ['entropy', 'analyze']:
        cmd_entropy(args)
    elif command in ['encrypt', 'enc']:
        cmd_encrypt(args)
    elif command in ['decrypt', 'dec']:
        cmd_decrypt(args)
    else:
        # Default: treat as password analysis if it looks like a password
        if command.startswith('-'):
            print(f"Unknown option: {command}")
            print_help()
        else:
            # Assume it's a password to analyze
            args = [command] + args
            cmd_entropy(args)


if __name__ == '__main__':
    main()
