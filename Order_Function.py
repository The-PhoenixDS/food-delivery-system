import random
import datetime
now = datetime.datetime.now()


def take_order():
    menu = {
        'Burger': 40.00,
        'Drink': 15.00,
        'Fries': 20.00,
        'Wraps': 32.00,
        'Wings': 43.00,
        'Lamb Chops': 76.00,
    }

    order = {}
    total_cost = 0.0

    while True:
        food_name = input("What would you like to order? (type 'n' to finish) ")
        if food_name == 'n':
            break

        if food_name not in menu:
            print("Sorry, we don't have that at the moment.")
            continue

        else:
            exit

        item_num = int(input(f"How many {food_name}s would you like to order? "))
        total = menu[food_name] * item_num
        order[food_name] = item_num
        total_cost += total

        order_number = random.randint(10, 1000)
        date = now.strftime("%Y-%m-%d")
        time = now.strftime("%H:%M:%S")
    print("Your order number: ", order_number)
    with open('order.txt', 'a') as f:
        f.write(str(order_number) + ',' + str(date) + ',' + str(time) + ',')
        for food_name, item_num,  in order.items():
            order_line = f"{food_name},{item_num},"
            print(order_line, end='')
            f.write(order_line)

        status_line = f"{Status},{Payment} "
        total_line = f"R{total_cost:.2f}\n"
        f.write(status_line)

        f.write(total_line)

    print(f"Total cost: {total_cost:.2f}")


# 2()

def cancel_order():
    
    onumber = input("Plesae give us an order number")
    conumber = onumber +  'cancel'
    # Read in the file
    with open('order.txt', 'r') as file :
        filedata = file.read()
    

    # Replace the target string
    filedata = filedata.replace(onumber,conumber )
    

    # Write the file out again
    with open('order.txt', 'w') as file:
        file.write(filedata)


def view_cancelled_orders():
    with open(r'order.txt', 'r') as fp:
        # read all lines in a list
        lines = fp.readlines()
        for line in lines:
            # check if string present on a current line
            if 'cancel' in line[0:10] :
                print(line)


   


# # ask the user if they want to edit their order
def edit_order():
    # Define the menu
    menu = {
        'Burger': 40.00,
        'Drink': 15.00,
        'Fries': 20.00,
        'Wraps': 32.00,
        'Wings': 43.00,
        'Lamb Chops': 76.00,
    }

    # Prompt the user to enter their order number
    onum = input("Please enter your order number: ")

    # Ask the user whether they want to edit their order
    answer = input("Would you like to edit your order? (Y/N): ")
    if answer.upper() == "Y":
        # Ask the user whether they want to add or remove an item
        edit_answer = input("What would you like to do? Add or Remove an item? (Add/Remove): ")
        if edit_answer.lower() == "add":
            # Prompt the user to enter the item they want to add
            item_to_add = input("Please enter the item you would like to add: ")

            # Check if the item is in the menu
            if item_to_add in menu:
                # Read the order file and update the order
                with open('order.txt', 'r') as f:
                    newlines = []
                    item_added = False
                    for line in f:
                        if onum in line and item_to_add in line:
                            # Update the quantity of the item
                            parts = line.split(',')
                            old_quantity = int(parts[-2])
                            new_quantity = old_quantity + 1
                            parts[-2] = str(new_quantity)

                            # Update the price of the order
                            old_price = float(parts[-3][1:])
                            item_price = menu[item_to_add]
                            new_price = old_price + item_price
                            parts[-3] = f" ${new_price:.2f}"

                            # Concatenate the updated line
                            updated_line = ",".join(parts)
                            newlines.append(updated_line)
                            item_added = True
                        else:
                            newlines.append(line)

                    # If the item was not already in the order, add it
                    if not item_added:
                        new_item = f",{item_to_add},1,${menu[item_to_add]:.2f}\n"
                        newlines.append(f"{onum}{new_item}")

                # Write the updated order to the file
                with open('order.txt', 'w') as f:
                    for line in newlines:
                        f.write(line)

                print(f"{item_to_add} has been added to your order.")
            else:
                print(f"{item_to_add} is not in the menu.")
        else:
            print("Sorry, only adding items is supported at the moment.")
    else:
        print("Order not modified.")


# Cancel Order
 
def view_cancelled_orders():
    print("\nHere is a list of all cancelled orders:")
    with open('order.txt', 'r') as fp:
        for line in fp:
            # check if string present on a current line
            if 'cancelled' in line :
                print(line)
                
                
def cancel_order():
    newlines = []

    onumber = input("Plesae give us an order number")
    # Read in the file
    with open('order.txt', 'r') as file :
        for line in file:
            if onumber in line:
               if "cancelled" in line:
                    print("Order already cancelled")
               elif "pending" in line:
                    print("Order cancelled successfully")
                    newlines.append(line.replace('pending', 'cancelled'))
               else:
                    print("cannot cancel,order already out")
                    newlines.append(line)
            else:
                newlines.append(line)


            with open('order.txt', 'w') as f:
                    for line in newlines:
                        f.write(line)
    # view_cancelled_orders()

def cash_payment(amount):

    print("You have chosen to pay by cash.")
    print(f"The total amount to be paid is R{amount:.2f}.")
    
    cash = float(input("Enter amount paid: "))
    onumber = input("Plesae give us an order number")

    while cash < amount:
        print(" Your money is short, please add more or cancel the order.")
        cash = float(input("Enter amount paid: "))
    change = cash - amount
    print(f"Amount paid is R{cash}. Your change is {change:.2f}.")
    print("Payment successful")
    print("Thank you for your payment!")
    
    with open('order.txt','r') as f:
        newlines = []
        for line in f:
            if onumber in line:
                newlines.append(line.replace('not paid', 'paid'))
            else:
                newlines.append(line)

    with open('order.txt', 'w') as f:
        for line in newlines:
            f.write(line)
    
    
# function for card payment
def card_payment(amount):
    print("You have chosen to pay by card.")
    onumber = input("Please give me your order number:")
    amount = float(input("Please enter the amount to be paid:"))
    acc_num = input("Please enter acc number : ")
    pin = input("Please enter your PIN: ")
  

    with open('bank.txt','r') as f:
        newlines_bank = []
        for line_bank in f:
            if acc_num and pin in line_bank:
                balance = line_bank[14:]
                new_balance = float(balance) -  amount
                newlines_bank.append(line_bank.replace(str(balance), str(new_balance)))
                newlines_bank.append("\n")
                
                with open('order.txt','r') as f:
                    newlines = []
                    for line in f:
                        if onumber in line:
                            newlines.append(line.replace('not paid', 'paid'))
                        else:
                            newlines.append(line)

                with open('order.txt', 'w') as f:
                    for line in newlines:
                        f.write(line)
                 
                
            else:
                newlines_bank.append(line_bank)

    with open('bank.txt', 'w') as f:
        for line in newlines_bank:
            f.write(line)
            
# main for payment functions
def payment_option():
    payment_option =  input("Please choose a payment option (cash or card): ")
    amount = float(input("Please enter the amount to be paid:"))

    if payment_option == "cash":
            cash_payment(amount)
    elif payment_option == "card":
            card_payment(amount)
    else:
            print("Error: Invalid payment option.")
            
def search():
    order_num = input("Please give me your order number:")
    with open('order.txt', 'r') as f:
        for line in f:
            if order_num in line:
                print(line)
            

def search_sales_list():
    total_items = 0
    total_sales = 0
    food_name = input("Please give me your food_name :")
    with open('order.txt', 'r') as f:
        for line in f:
            if food_name in line:
                item = (line.split(","))
                quantity = item[4]
                sales = item[5]
                total_items = total_items + int(quantity)
                total_sales = total_sales + int(sales)
    print(total_items)
    print("R " + str(total_sales))
     
            
def main():
    main_menu = ("take_order", "edit_order", "cancel_order", "search_order")
    # while True:
    print()
    print('choose an option')
    print('1-Order_food')
    print('2-Edit_order')
    print('3-Cancel_order')
    print('4-Search_order')
    print('5-search_sales_list')

    print()
    user_option = int(input('option: '))

    if user_option == 1:
        take_order()
    elif user_option == 2:
         edit_order()
    elif user_option == 3:
        cancel_order()
    elif user_option == 4:
        search()
    elif user_option == 5:
        search_sales_list()
main()