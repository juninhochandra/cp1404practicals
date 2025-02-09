"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

sales = float(input("Enter sales: $"))

while sales >= 0:
    if sales < 1000:
        print(str(sales * 1 / 10))
    else:
        print(str(sales * 15 / 100))
    sales = float(input("Enter sales: $"))

# print("Do next thing")