#Variable Declaration
inventory = {"A01":{"item":"Chocolate Bar","price":2,"stock":10},
         "A02":{"item":"Protein Bar","price":5,"stock":10},
         "A03":{"item":"Beef Jerky","price":5,"stock":10},
         "A04":{"item":"Candy Strips","price":2,"stock":10},
         "B01":{"item":"Assorted Nuts","price":3,"stock":10},
         "B02":{"item":"Cheesy Chips","price":3,"stock":10},
         "B03":{"item":"Pretzel Sticks","price":3,"stock":10},
         "B04":{"item":"Gummy Bears","price":3,"stock":10},
         "C01":{"item":"Water Bottle","price":1,"stock":10},
         "C02":{"item":"Soda Can","price":2,"stock":10},
         "C03":{"item":"Iced Tea","price":2,"stock":10},
         "C04":{"item":"Juice bag","price":2,"stock":10}
}
loop = True #Turns the program into an infinite loop
basket = [] #Stores the items that the user has purchased

#Greeting
print("Welcome to the Simple Vending Machine!\nMy job is to serve.\n\n")

#Menu Display
def menu():
    print("Wanna buy something?\nTIP: type 'basket' to see what you've bought, and 'quit' to exit the program.")
    #^Additional instructions for other features
    for code, info in inventory.items():
        print(f"{code} > Item: {info["item"]} | Price: {info["price"]} AED | {info["stock"]} in stock.")\
    #^Displays the menu

#Vending machine program
def vending():
    code = input(str("ENTER CODE: "))
    if code in inventory :
        item = inventory[code]["item"]
        price = inventory[code]["price"]
        quantity = inventory[code]["stock"]
        #^Assigning values from the dictionary to variables for convenience
        print(item.upper(),"\nPRICE:",price,"AED")
        payment = float(input("Please insert your money. AED "))
        #Asking the user for money as a float input
        if payment >= price and quantity > 0:
            change = payment - price
            print("\nDispensing the "+item+", please collect your change of",change,"AED.\n\n")
            inventory[code]['stock']-=1
            basket.insert(0,item)
        #^Calculating for change, stock changes, and adding items to the "basket"
        elif payment >= price and quantity == 0:
            print("Oops! We've run out of that item!\n")
        else:
            print("Oops! Insufficient Funds!\n")
    elif code == "quit":
        print("\nThank you for using the Simple Vending Machine!\nDuring this session, you bought: "
              +str(basket))
        exit()
        #^End message and breaking the loop by stopping the program
    elif code == "basket":
        print("\nHere's what you've bought so far:\n"+str(basket)+"\n")
        #^Displays the user's "basket"
    else:
        print("Oops! We've encountered an error!\n")



#MAIN LOOP
while loop == True:
 menu()
 vending()

