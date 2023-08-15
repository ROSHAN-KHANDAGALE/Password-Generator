import random
import string
import welcome as wc

def password_generate(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        passlength = int(input("PLEASE! Provide the Length of Password: "))
        if passlength <= 0:
            print('INVALID GENERATION')
            return
        generated = password_generate(passlength)
        print("Generated Password:", generated)
        print('\n\n')
    except ValueError:
        print("Invalid input. Please enter a valid positive integer.")

if __name__ == "__main__":
    wc.welcome()
    main()
