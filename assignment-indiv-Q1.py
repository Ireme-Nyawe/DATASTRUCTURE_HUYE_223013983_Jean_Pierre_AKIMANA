# here is Restaurant Order Management .
from collections import deque
menu = []
placed_orders =deque()

def addMenuItem(item):
    menu.append(item)
    print(f"{item} added.")

def removeMenuItem(item):
    if item in menu:
        menu.remove(item)
        -print(f"{item} removed.")
    else:
        print("No Item Found!")

def placeOrder(item):
    if item in menu:
        placed_orders.append(item)
        print(f"order for {item} made.")
        return "Y"
    else:
        print(f"Item ordered not found. here is our menu {menu} or  Enter S , to skip this order! ")
        return "N"

def processOrder():
    if placed_orders:
        item = placed_orders.popleft()
        print(f"{item} order processed.")
    else:
        print("No order found for processing!")

def undoOrder():
    if placed_orders:
        item=placed_orders.pop()
        print(f"{item} undone.")
    else:
        print("No order found, no need for undoing!")


#test progrm functionality
numberItems=int(input("enter number of Items to add on menu: "))
for i in range(numberItems):
    item = input(f"Enter Item {i+1} : ")
    addMenuItem(item)
    if i==numberItems-1:
        print("your items Added, continue with other operations! \n ----------------------")


removingNumber=int(input("enter number of Items to remove on menu if any : "))
for i in range(removingNumber):
    item = input(f"Enter Item {i+1} : ")
    removeMenuItem(item)
    if i==numberItems-1:
        print("your items removed, continue with other operations! \n ----------------------")

ordersNum=int(input("enter number of orders to place if any: "))
i=1
while i<=ordersNum:
    item = input(f"Enter your order {i} : ")
    if item=="S" or item=="s" :
        i=i+1
    else:
        place=placeOrder(item)
        if place=="N":
            i=i
        else:
            i=i+1
    if i== ordersNum+1:
        print("your orders Placed, continue with other operations! \n ----------------------")

undoingNumber = int(input("Enter number of orders to undo if any : "))
for i in range(undoingNumber):
    undoOrder()
    if i==undoingNumber-1:
        print("your orders undone, continue with other operations! \n ----------------------")

proccessNumber = int(input("Enter number of orders to Process if any: "))
for i in range(proccessNumber):
    processOrder()
    if i==proccessNumber-1:
        print("your orders processed, continue with other operations! \n ----------------------")

print(f"here is our menu: {menu}")
print(f"Here is placed orders: {list(placed_orders)}")
