import random
import datetime
now = datetime.datetime.now()
with open('Menu_Description.txt', 'r') as f:
        menu = {}
        for line in f:
            values = line.strip().split(',')
            if len(values) == 2:
                food_name = values[0].strip()
                v = values[1].strip('\\')
                v =v.strip('R')
                v =v.strip('}')
                price = float(v.strip('\\'))
                menu[food_name] = price
        for food_name, price in menu.items():
            print(f'{food_name}  R{price:.2f}')


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
   