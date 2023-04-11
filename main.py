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
 print ("Thank You")

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
 Y=Y+1\huhbu

 
 hiughiukj
 joiuhoiu
