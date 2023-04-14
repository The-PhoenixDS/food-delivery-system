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

        total_line = f"R{total_cost:.2f}\n"

        f.write(total_line)

    print(f"Total cost: {total_cost:.2f}")


take_order()


 
    
def cancel_order():
    
    onumber = input("Plesae give us an order number")
    conumber = onumber +  'cancel'
    # Read in the file
    with open('/Users/damacm182_/Desktop/orders.csv', 'r') as file :
        filedata = file.read()
    

    # Replace the target string
    filedata = filedata.replace(onumber,conumber )
    

    # Write the file out again
    with open('/Users/damacm182_/Desktop/orders.csv', 'w') as file:
        file.write(filedata)


def view_cancelled_orders():
    with open(r'/Users/damacm182_/Desktop/orders.csv', 'r') as fp:
        # read all lines in a list
        lines = fp.readlines()
        for line in lines:
            # check if string present on a current line
            if 'cancel' in line[0:10] :
                print(line)


orderc = input("Please select an option: 1- Cancelling Order, 2- View Cancelled orders")

if orderc == "1":
    cancel_order()
    print("Order cancelled succesfully")
elif orderc == "2":
    view_cancelled_orders()
else:
    print("Invalid selection")
    exit()
   


# ask the user if they want to edit their order
while True:
    answer = input("Would you like to edit your order? (Y/N): ")
    if answer == "Y":
        
# give the user options to add or remove an item
        while True:
            edit_answer = input("What would you like to do? Add or Remove an item? (Add/Remove): ")
            if edit_answer == "Add":
                item_to_add = input("Please enter the item you would like to Add: ")
                if item_to_add == "Burger":  
                    burger_counter=burger_counter+1
                print(f"{item_to_add} has been added to your order.")
                
                break
# remove the item from the order list
            elif edit_answer == "Remove":
                item_to_remove = input("Please enter the item you would like to remove: ")
                if item_to_remove == "Burger":
                    burger_counter=burger_counter-1
                print(f"{item_to_remove} has been removed from your order.")
                break
            else:
                print(f"Sorry, {Myorderfood} is not in your order.")
        else:
                print("Invalid input. Please enter 'Add' or 'Remove'.")
    
    elif answer == "N":
        print("Thank you for your order.")
        break
    else:
        print("Invalid input. Please enter 'Y' or 'N'.")
        
        
        
        
# Marcus cancel
# here is the code for the search function
        

def search():
    order_num = input("Please give me your order number:")
    with open('order.txt', 'r') as f:
        for line in f:
            if order_num in line:
                print(line)

search()



def cash_payment(amount):
    print("You have chosen to pay by cash.")
    print(f"The total amount to be paid is R{amount:.2f}.")
    cash = float(input("Enter amount paid: "))
    while cash < amount:
        print(" Your money is short, please add more or cancel the order.")
        cash = float(input("Enter amount paid: "))
    change = cash - amount
    print(f"Amount paid is R{cash}. Your change is {change:.2f}.")
    print("Payment successful")
    print("Thank you for your payment!")
    
    
# function for card payment
def card_payment(amount):
    print("You have chosen to pay by card.")
    pin = input("Please enter your PIN: ")

    with open("/Users/damacm187/Documents/user.txt", "r") as f:
        lines = f.readlines()
        user_pin = lines[1][:4]   # extract the first 4 characters of the second line
        balance = float(lines[1][4:13])   # extract characters 5-13 of the second line and convert to float
        card_id = lines[1][6:].strip()  

    if pin == user_pin:
        print("PIN verification successful.")
        if amount <= balance:
            # update user balance in file
            with open("/Users/damacm187/Documents/user.txt", "w") as f:
                f.write(str(balance - amount))
            print(f"Payment successful. Your remaining balance is R{balance - amount:.2f}.")
        else:
            print("Error: Insufficient balance.")
    else:
        print("Error: Incorrect PIN.")



# main program
amount = float(input("Please enter the amount to be paid: "))

payment_option = input("Please choose a payment option (cash or card): ")

if payment_option == "cash":
    cash_payment(amount)
elif payment_option == "card":
    card_payment(amount)
else:
    print("Error: Invalid payment option.")
