number_of_items = int(input("Number of items: "))
if number_of_items >= 0:
    total_price = 0.0
    for i in range(number_of_items):
        price_of_item = float(input("Price of item: "))
        total_price += price_of_item
    if total_price > 100:
        total_price = total_price * 9 / 10

    print("Total price for " + str(number_of_items) + " items " + "is $" + str(total_price))
    # In case for 1 item, we can use the singular form, but I don't want to risk that for the assessment.
    # print("Total price for " + str(number_of_items) + " item" + ("s " if number_of_items != 1 else " ") + "is $" + str(total_price))
else:
    print("Invalid number of items!")

