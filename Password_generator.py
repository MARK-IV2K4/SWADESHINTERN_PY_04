import random
import string

def generate_password(length=12, use_uppercase=True, use_digits=True, use_special_characters=True):
    """
    Generate a secure, random password with customizable length and complexity.
    
    Parameters:
        length (int): The desired length of the password (default: 12).
        use_uppercase (bool): Include uppercase letters in the password (default: True).
        use_digits (bool): Include digits in the password (default: True).
        use_special_characters (bool): Include special characters in the password (default: True).
    
    Returns:
        str: The generated password.
    """
    if length < 4:
        raise ValueError("Password length must be at least 4 characters for security.")
    
    # Define character pools
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if use_uppercase else ""
    digits = string.digits if use_digits else ""
    special = string.punctuation if use_special_characters else ""
    
    # Combine pools and ensure at least one character from each selected pool
    all_characters = lower + upper + digits + special
    if not all_characters:
        raise ValueError("At least one character set must be selected.")
    
    # Guarantee the password includes at least one character from each selected category
    password = []
    if use_uppercase:
        password.append(random.choice(upper))
    if use_digits:
        password.append(random.choice(digits))
    if use_special_characters:
        password.append(random.choice(special))
    password.append(random.choice(lower))
    
    # Fill the rest of the password length
    while len(password) < length:
        password.append(random.choice(all_characters))
    
    # Shuffle to randomize the order of characters
    random.shuffle(password)
    
    return ''.join(password)

if __name__ == "__main__":
    print("Welcome to the Password Generator!")
    try:
        length = int(input("Enter desired password length (minimum 4): "))
        use_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == 'y'
        use_digits = input("Include digits? (y/n): ").strip().lower() == 'y'
        use_special_characters = input("Include special characters? (y/n): ").strip().lower() == 'y'
        
        password = generate_password(
            length=length,
            use_uppercase=use_uppercase,
            use_digits=use_digits,
            use_special_characters=use_special_characters
        )
        print(f"Your generated password is: {password}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
