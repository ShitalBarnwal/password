import random
import string

def generate_password(length=12):
    # Define character sets
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    punctuation = string.punctuation

    # Combine character sets
    all_characters = lowercase_letters + uppercase_letters + digits + punctuation

    # Ensure at least one character from each set is included
    password = random.choice(lowercase_letters) + random.choice(uppercase_letters) + \
               random.choice(digits) + random.choice(punctuation)

    # Generate the remaining characters
    password += ''.join(random.choice(all_characters) for _ in range(length - 4))

    # Shuffle the characters to make it more random
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    return password

# Example usage:
password = generate_password()
print("Generated Password:", password)