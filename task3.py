import random
import string

def generate_password(length=12):
    """
    Generates a random password containing uppercase, lowercase, digits, and special characters.

    Parameters:
        length (int): Length of the password. Default is 12.

    Returns:
        str: Generated password.
    """
    if length < 4:
        raise ValueError("Password length must be at least 4 characters.")

    # Character pools
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special = string.punctuation

    # Ensure the password contains at least one of each character type
    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(special)
    ]

    # Fill the rest of the password length with random choices from all pools
    all_characters = uppercase + lowercase + digits + special
    password += random.choices(all_characters, k=length - 4)

    # Shuffle the password to ensure randomness
    random.shuffle(password)

    return ''.join(password)

if __name__ == "__main__":
    print("Welcome to the Password Generator!")
    count = int(input("How many passwords do you want to generate? "))
    try:
        length = int(input("Enter the desired password length (default is 12): ") or 12)
        for _ in range(count):
            print(f"Generated password: {generate_password(length)}")
    except ValueError as e:
        print(f"Error: {e}")
