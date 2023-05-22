def main():
    main_menu = input("Choose option")
    print()
    print("1. Place order")
    print("2. Edit order")
    print("3. Remove item")
    print("4. Cancel order")
    
    output = int(input("Option: "))
    if output == 1:
        take_order()
    elif output == 2: 
        edit_order()
    elif output == 3:
        remove_item()
    else
        cancel_order()
        
        
        def take_order():
            menu = {'chips': 15,
                    'burger': 40,
                    'drink': 10,
                    'pie': 20}
            
        food_name = input("Enter the food you wanna order or n to finish ")
        if food_name == 'n':
            status = 'Preparing'
        