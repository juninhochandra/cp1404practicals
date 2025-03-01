"""
Emails
Estimate: 25 minutes
Actual:   22 minutes
"""

name_to_email = dict()
email = input("Email: ")

# Should we check if the email is invalid?
while email != "":
    full_name = email.split("@")[0].split(".")
    full_name = " ".join(full_name).title()
    name_confirm = input(f"Is your name {full_name}? (Y/n) ").upper()
    if name_confirm != "" and name_confirm != "Y":
        full_name = input("Name: ")
    name_to_email[full_name] = email
    email = input("Email: ")

print()
for name, email in name_to_email.items():
    print(f"{name} ({email})")