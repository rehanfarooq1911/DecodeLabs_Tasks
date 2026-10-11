import string
import secrets
import math

def main():
    print("--- Enterprise Random Password Generator ---")    
    while True:
        try:
            # Capture target integer representing password length
            length = int(input("Enter password length (minimum 8 for NIST 2024 compliance): "))
            
            if length < 8:
                print("Error: Passwords must be at least 8 characters long.")
                continue
            if length > 64:
                print("Error: Maximum length supported is 64 characters.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid target integer.")

    char_pool = string.ascii_letters + string.digits + string.punctuation
    pool_size = len(char_pool)
    
    password_list = []
    
    for _ in range(length):
        secure_char = secrets.choice(char_pool)
        password_list.append(secure_char)
        
    secure_password = ''.join(password_list)

    entropy = length * math.log2(pool_size)
    
    print("\n--- Output Provision ---")
    print(f"Generated Password: {secure_password}")
    print(f"Entropy Strength: {entropy:.2f} bits")

if __name__ == "__main__":
    main()