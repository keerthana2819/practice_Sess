import random
import string

def generate_password(length=6):
    #length changed from 8 to 6
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    length = int(input("Enter password length: "))
    print("Generated Password:", generate_password(length))

if __name__ == "__main__":
    main()
