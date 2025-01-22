# Password Generator Script

This is a Python script that generates a secure random password based on user-defined parameters. The password can include lowercase letters, uppercase letters, numbers, and special characters.

## Features
- Generate a password of any specified length.
- Optionally include numbers and/or special characters in the password.
- Uses the `secrets` module for cryptographically secure randomness.
  
## Requirements
- Python 3.x

## Usage

### Basic Command:
To run the script, use the following command in your terminal:

python password_generator.py `<password length>`

Where `<password length>` is the desired length of the generated password.

### Options:
- `-n`: Include numbers in the password.
- `-s`: Include special characters (punctuation) in the password.
- `--help`: Display the help message with usage instructions.
