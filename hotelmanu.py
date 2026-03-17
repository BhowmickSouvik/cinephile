menu = {
    "pizza" : 50,
    "burger" : 45,
    "coffie" : 60,
    "salad" : 30,
    "pasta" : 55,
    "water" : 20
}

print("WELCOME TO PYTHON RESTRUDENT")
print("pizza : 50\nburger : 45\ncoffie : 60\nsalad : 30\npasta : 55\nwater : 20")

total = 0

item1 = input("ENTER WHAT DO YOU WENT TO ODER = ")
if item1 in menu:
    total += menu[item1]
    print(f"YOUR ITEM {item1} HAS BEEM ADDED TO YOUR ODER")
else:
    print("PLISE ORDER UNDER THE MENU")


another = input("HAVE YOU ORDER MORE ITEM? (yes/no) =")
if another == "yes":
    item2 = input("ENTER WHAT DO YOU WENT TO ODER =")
    if item2 in menu:
        total += menu[item2]
        print(f"YOUR ITEM {item2} HAS BEEM ADDED TO YOUR ODER")
        print("YOUR TOTAL BILL IS",(total))
    else:
        print("PLESE ORDER UNDER THE MENU")

else:
    another == "no"
    print("YOUR TOTAL BILL IS",(total))