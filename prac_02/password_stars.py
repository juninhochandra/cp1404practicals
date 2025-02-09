# imports
# CONSTANTS

def main():
    # password check and print the length of the password amount of stars
    password = get_password()
    print_asterisks(password)

def print_asterisks(password):
    print("*" * len(password))

def get_password():
    min_length = 8
    prompt = "Enter a password: "
    password = input(prompt)
    while len(password) < min_length:
        print("Password is too short! Minimum length is " + str(min_length))
        password = input(prompt)
    return password

main()