import random
import string

def generate_password(length=5):
    #length changed from 6 to 5
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    length = int(input("Enter password length: "))
    print("Generated Password:", generate_password(length))

if __name__ == "__main__":
    main()
