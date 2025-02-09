"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""

def main():
    # Converting Celsius to Fahrenheit and vice versa.
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            print(f"Result: {calculate_fahrenheit(celsius):.2f} F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            print(f"Result: {calculate_celsius(fahrenheit):.2f} C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def calculate_celsius(fahrenheit):
    # fahrenheit to celsius
    return 5 / 9 * (fahrenheit - 32)


def calculate_fahrenheit(celsius):
    # celsius to fahrenheit
    return celsius * 9.0 / 5 + 32

main()