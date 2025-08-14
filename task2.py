import random
import string

def generate_password(length, use_uppercase=True, use_numbers=True, use_symbols=True):
    characters = string.ascii_lowercase  # always include lowercase

    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return "Error: No character set selected."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# --- User Input ---
try:
    length = int(input("Enter desired password length: "))
    if length <= 0:
        raise ValueError

    use_uppercase = input("Include capital letters? (Y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    # --- Generate and Display ---
    password = generate_password(length, use_uppercase, use_numbers, use_symbols)
    print("\nGenerated Password:", password)

except ValueError:
    print("Please enter a valid positive number for password length.")
