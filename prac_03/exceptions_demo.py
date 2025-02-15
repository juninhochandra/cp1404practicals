"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
When we try to enter a non-number string, it fails to convert the string to an integer.
2. When will a ZeroDivisionError occur?
When we try to enter 0 as the denominator, assuming the numerator input doesn't throw an error.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Yes
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        print("Cannot divide by zero!")
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")