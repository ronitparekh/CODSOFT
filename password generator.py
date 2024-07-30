import random
import string

def generate_password(length):
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation 

    all_characters = lowercase_letters + uppercase_letters + digits + special_characters
    
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password

def main():
    while True:
        try:
            length = int(input("Enter the desired length of the password (enter 0 to exit): "))
            
            if length == 0:
                break
            
            password = generate_password(length)
            print("Generated password:", password)
            
        except ValueError:
            print("Invalid input. Please enter a valid integer for the password length.")
            
if __name__ == "__main__":
    main()
