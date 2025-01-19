from random_password_toolkit import (
    generate,
    generate_multiple,
    generate_pronounceable_password,
    generate_with_custom_pool,
    check_password_strength,
    encrypt_password,
    decrypt_password
)

if __name__ == "__main__":
    # Test generate functions
    generate_password = generate(length=10, numbers=True, symbols=False, lowercase=True, uppercase=True, exclude_similar_characters=False, exclude='', strict=False)
    print("Generated password:", generate_password)
    
    # Test generate_multiple function
    generate_multiple_password = generate_multiple(5, {"length": 8, "numbers": True, "uppercase": True})
    print("Multiple passwords:", generate_multiple_password)
    
    # Test generate_pronounceable_password functions
    pronounceable_password = generate_pronounceable_password(length=12)
    print("Pronounceable password:", pronounceable_password)
    
    # Test generate_with_custom_pool function
    generate_with_custom_pool_password = generate_with_custom_pool(length=8, custom_pool="p@ss")
    print("Custom pool password:", generate_with_custom_pool_password)

    # Test check_password_strength function
    password_strength_checker = "MySecureP@ssword123!"
    result = check_password_strength(password_strength_checker)
    print(f"Password: {password_strength_checker}")
    print(f"Strength: {result['strength']}")
    print(f"Score: {result['score']}")
    print(f"Stength: {result}")

    # Test encrypt_password and decrypt_password functions
    password = "MySecureP@ssword123!"
    
    # Encrypt the password
    encrypted_data = encrypt_password(password)
    print("Encrypted Password:", encrypted_data["encrypted_password"])
    print("IV:", encrypted_data["iv"])

    # Decrypt the password
    decrypted_password = decrypt_password(encrypted_data["encrypted_password"], encrypted_data["iv"])
    print("Decrypted Password:", decrypted_password)


    try:
        print(generate_multiple(0))
    except ValueError as error:
        print(error) 
