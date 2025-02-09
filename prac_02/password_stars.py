MIN_LENGTH = 8
PROMPT = "Enter a password: "

password = input(PROMPT)
while len(password) < 8:
    print("Password is too short! Minimum length is " + str(MIN_LENGTH))
    password = input(PROMPT)

print("*" * len(password))