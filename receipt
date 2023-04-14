import datetime

# Define the items and their prices
menu = {
    "Burger": 10.99,
    "Fries": 4.99,
    "Drink": 2.99
}

# Define a function to print the receipt
def print_receipt(order_items):
    # Get the current date and time
    now = datetime.datetime.now()

    # Print the receipt header
    print("========== RECEIPT ==========")
    print("Date: ", now.strftime("%Y-%m-%d"))
    print("Time: ", now.strftime("%H:%M:%S"))
    print("=============================")

    # Print the order items and their prices
    total = 0
    for item, price in order_items.items():
        print(item, "\t", "R{:.2f}".format(price))
        total += price

    # Print the order number and total cost
    print("=============================")
    print("Order number: ", now.strftime("%m%d"))
    print("Total: ", "R{:.2f}".format(total))
    print("=============================")

# Test the function with an order of a burger and fries
order_items = {"Burger": 10.99, "Fries": 4.99}
print_receipt(order_items)
