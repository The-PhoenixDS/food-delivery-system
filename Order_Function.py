
order = {}

def edit_order():
    # Prompt the user to enter their order number
    onum = input("Please enter your order number: ")

    while True:
        answer = input("Would you like to edit your order? (Y/N) ")
        if answer.lower() == "y":
            while True:
                edit_answer = input("Would you like to add or remove another item? (Add/Remove/Finish): ")
                if edit_answer.lower() == "add":
                    item_to_add = input("Please enter the item you would like to add: ")
                    quantity_to_add = None
                    while quantity_to_add is None or quantity_to_add <= 0:
                        try:
                            quantity_to_add = int(input("Please enter the quantity of the item you would like to add: "))
                            if quantity_to_add <= 0:
                                print("Invalid quantity. Please enter a positive integer.")
                        except ValueError:
                            print("Invalid quantity. Please enter a positive integer.")
                            quantity_to_add = None
    
                    # Use lower() method to convert the item to lowercase before checking if it's already in the order
                    if item_to_add.lower() in order:
                        order[item_to_add.lower()] += quantity_to_add
                    else:
                        order[item_to_add.lower()] = quantity_to_add
                    print(f"{quantity_to_add} {item_to_add}(s) have been added to your order.")
   
                elif edit_answer.lower() == "remove":
                    item_to_remove = input("Please enter the item you would like to remove: ")
                    if item_to_remove.lower() not in order:
                        print(f"Sorry, {item_to_remove} is not in your order.")
                    else:
                        quantity_to_remove = None
                        while quantity_to_remove is None or quantity_to_remove <= 0:
                            try:
                                quantity_to_remove = int(input("Please enter the quantity of the item you would like to remove: "))
                                if quantity_to_remove <= 0:
                                    print("Invalid quantity. Please enter a positive integer.")
                                elif quantity_to_remove > order[item_to_remove.lower()]:
                                    print(f"Sorry, you have only {order[item_to_remove.lower()]} {item_to_remove}(s) in your order.")
                                    quantity_to_remove = None
                            except ValueError:
                                print("Invalid quantity. Please enter a positive integer.")
                                quantity_to_remove = None
        # Use lower() method to convert the item to lowercase before checking if it's in the order
                        if order[item_to_remove.lower()] >= quantity_to_remove:
                            order[item_to_remove.lower()] -= quantity_to_remove
                            print(f"{quantity_to_remove} {item_to_remove}(s) have been removed from your order.")
                        else:
                            print(f"Sorry, {item_to_remove} is not in your order or has already been removed.")
                    continue    
                if edit_answer.lower() == "finish":
                        break
                else:
                        print("Invalid input. Please enter 'Add', 'Remove', or 'Finish'.")
        elif answer.lower() == "n":
            print("Thank you for your order.")
            break
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")
        
def main():
    while True:
        print()
        print('Choose an option:')
        print('1 - Order food')
        print('2 - Edit order')
        print('3 - Cancel order')
        print('4 - Search order')
        
        user_option = int(input('Option: '))
        
        if user_option == 1:
            take_order()
        elif user_option == 2:
            edit_order()
        elif user_option == 3:
            cancel_order()
        elif user_option == 4:
            search()
        else:
            print("Invalid input. Please enter a number from 1 to 4.")
            
main()




        
        


