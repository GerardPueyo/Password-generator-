import sys
import secrets
import string

def main():

    if '--help' in sys.argv:
        show_help()
        exit(0)

    password_length = check_len()

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    numbers = string.digits
    special_characters = string.punctuation

    alphabet = lower + upper
    if '-n' in sys.argv:
        alphabet += numbers
    if '-s' in sys.argv:
        alphabet += special_characters

    password = ''.join(secrets.choice(alphabet) for i in range(password_length))
    print(password)

def check_len():
    if len(sys.argv) < 2:
        print("Please provide the password length as the first parameter")
        exit(1)

    try:
        password_length = int(sys.argv[1])
    except ValueError:
        print("The password length must be an integer")
        exit(1)

    return password_length

def show_help():
    print("""
    Usage: password_generator.py <password length> -n -s
    
    Options:
    <password length>  : The length of the generated password.
    -n                 : Include numbers in the password.
    -s                 : Include special characters in the password.
    --help             : Show this help message.
    """)

if __name__ == "__main__":
    main()