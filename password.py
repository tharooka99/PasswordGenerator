import secrets
import string

def generate_password(length=12):
    # Define individual character pools
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation
    
    # Combine pools for the remaining character selection
    all_characters = lowercase + uppercase + digits + symbols

    # Rule 1: Ensure at least ONE character from each required category is included
    password_parts = [
        secrets.choice(lowercase),
        secrets.choice(uppercase),
        secrets.choice(digits),
        secrets.choice(symbols)
    ]

    # Rule 2: Fill the rest of the password length with purely random choices
    password_parts += [secrets.choice(all_characters) for _ in range(length - 4)]

    # Rule 3: Shuffle the list using a cryptographically secure method
    # secrets.SystemRandom() provides access to OS-level secure shuffling
    secure_random = secrets.SystemRandom()
    secure_random.shuffle(password_parts)

    return ''.join(password_parts)

if __name__ == "__main__":
    try:
        password_length = int(input("Enter desired password length (minimum 8 recommended): "))
        
        # Enforcing a stronger baseline security standard (8 characters)
        if password_length < 8:
            print("Security Warning: Password length must be at least 8 characters to resist brute-force attacks.")
        else:    
            generated_password = generate_password(password_length)
            print("\nSuccessfully Generated Secure Password:")
            print(generated_password)
            
    except ValueError:
        print("Error: Please enter a valid integer for the password length.")
