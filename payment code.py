food =["Burger","Drink","Fries","Wraps","Wings","Lamb Chops"]
prices =[40,15,20,32,43,76]

Myorderfood=[]
MyorderCost=[]
Counter=0

print("welcome to wrap it fast food joint". upper())


Order = input("Can I Take Your Order?")
if Order =="No":
 exit()
else:
 print ("Thank you")
        
nextOrder = True

while nextOrder==True:
 FoodOrder = input("Please enter your item")

 if FoodOrder =="Burger":
 Myorderfood.append(Food[0])
 MyorderCost.append(prices[0])
 Counter=Counter+1

 elif FoodOrder =="Drink":
 Myorderfood.append(Food[1])
 MyorderCost.append(prices[1])
 Counter=Counter+1

 elif FoodOrder =="Fries":
 Myorderfood.append(Food[2])
 MyorderCost.append(prices[2])
 Counter=Counter+1

 elif FoodOrder =="Wrap":
 Myorderfood.append(Food[3])
 MyorderCost.append(prices[3])
 Counter=Counter+1

 elif FoodOrder =="Wings":
 Myorderfood.append(Food[4])
 MyorderCost.append(prices[4])
 Counter=Counter+1

 elif FoodOrder =="Lamb Chops":
 Myorderfood.append(Food[5])
 MyorderCost.append(prices[5])
 Counter=Counter+1

else:
 print ("Not on Menu")
 finished = input("Have you finished ordering Y/N")
if finished =="N":
 nextOrder=True
else:
 nextOrder = False
print (Myorderfood)
print (MyorderCost)

Y=0
while Y <Counter:
 print ("here is your Order")
 print (" ")
 print ("******")
 print (Myorderfood[Y])
 Y=Y+1


# Define function for cash payment
def process_cash_payment(amount):
    print(f"Please pay R{amount} in cash.")
    cash = float(input("Enter amount paid: "))
    while cash < amount:
        print("Insufficient cash, please try again.")
        cash = float(input("Enter amount paid: "))
    change = cash - amount
    print(f"Amount paid is R{cash}. Your change is {change:.2f}.")
    print("Payment successful")
    
    
       # Define function for card payment
   
   
def process_card_payment(amount):
    
    user_pin = "1234"
    user_balance = 1000
    card_pin_number = input("Enter card pin number: ")
    
     # Verify PIN
    if card_pin_number == user_pin and amount <= user_balance:
        # Update user's balance
        user_balance -= amount
        # Send message of remaining balance
        print("Payment successful. Remaining balance: R{}".format(user_balance))
        print(f"Processing payment of R{amount:.2f} with card ")
        print("Payment successful.")
    else:
        print("Incorrect PIN or insufficient funds . Payment failed.")
        print(f"Processing payment of R{amount:.2f} with card ")
        print("Payment not successful.")
        
        # Main payment program
        def payments():
            amount = float(input("Enter amount to be paid: "))
            payment_method = input("Enter payment method (cash or card): ")
            if payment_method.lower() == "cash":
                process_cash_payment(amount)
            elif payment_method.lower() == "card":
                process_card_payment(amount)
            else:
                print("Invalid payment method. Please try again.")
                payments()

     #Run the program
    payments()