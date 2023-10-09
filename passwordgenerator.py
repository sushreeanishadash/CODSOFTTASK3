import random
import string

# Function to generate a random password
def generate_password(length):
    # Define the characters to choose from for the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a password with random characters
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Main function
def main():
    print("Password Generator")

    # Prompt the user for the desired password length
    while True:
        try:
            length = int(input("Enter the desired password length: "))
            if length <= 0:
                raise ValueError
            break
        except ValueError:
            print("Please enter a valid positive integer for the password length.")

    # Generate and display the password
    password = generate_password(length)
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
