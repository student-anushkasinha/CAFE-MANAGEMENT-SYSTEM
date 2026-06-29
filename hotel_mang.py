menu={
    'Pizza':80,
    'Pasta':50,
    'Burger':60,
    'Salad':60,
    'Coldrink':20
}
print("WELOCME TO OUR CAFE :)")
print(" Pizza: Rs80\n Pasta: Rs50\n Burger: Rs60\n Salad: Rs60\n Coldrink: Rs20")
total_bill = 0
item1 = input("Enter the selected item from the menu you want us to serve you :) : ")
if item1 in menu:
    total_bill = total_bill + menu[item1]
    print(f"Your item {item1} has been successfully added to your order ")
else:
    print("Sorry, please select from the menu only ")
another_item = input("Your order has been added do you want something else from the menu(Yes/No)?")
if another_item =="Yes":
    item2 = input("Enter another item to be added : ")
    if item2 in menu:
        total_bill += menu[item2]
    else:
        print("Sorry, please select from the menu only ")
print(f" HOPE YOU ENJOYED :), Your Total Payable Amount is {total_bill}")


