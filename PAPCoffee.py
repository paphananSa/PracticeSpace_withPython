def swMenu(orderNum):
    global countPay
    countPay = 0
    if int(orderNum) == 1:
        countPay = countPay + 50
        return "Affogato"
    elif int(orderNum) == 2:
        countPay = countPay + 50
        return "Espresso"
    elif int(orderNum) == 3:
        countPay = countPay + 45
        return "Americano"
    elif int(orderNum) == 4:
        countPay = countPay + 50
        return "Cappuccino"
    elif int(orderNum) == 5:
        countPay = countPay + 55
        return "Mocha"
    elif int(orderNum) == 6:
        countPay = countPay + 55
        return "Latte"

def sweetLevel(levelNum):
    if int(levelNum) == 1:
        return "0%"
    elif int(levelNum) == 2:
        return "50%"
    elif int(levelNum) == 3:
        return "100%"
    elif int(levelNum) == 4:
        return "120%"

def typeSe(typeNum):
    global count_typeSe
    count_typeSe = 0
    if int(typeNum) == 1:
        return "Hot"
    elif int(typeNum) == 2:
        count_typeSe = count_typeSe + 10
        return "Ice"

def SelectOrder():
    # ....... Select menu .......
    menu = ["Affogato", "Espresso", "Americano", "Cappuccino", "Mocha", "Latte"]
    count_menu = 0
    for num in menu:
        count_menu = count_menu + 1
        print(f"{count_menu} : {num}")

    print(f"What would you like to drink? {name}")
    global orderIs
    orderIs = input("Press number of menu: ")
    
    # ....... Select Type .......
    type = ["Hot", "Ice"]
    count_type = 0
    for num in type:
        count_type = count_type + 1
        print(f"{count_type} : {num}")
    global typeOf
    typeOf = input("Do you want to Hot or Ice? press number: ")
    
    # ....... Sweet Level .......
    level = ["(0%) No sugar", "(50%) Less sugar", "(100%) Normal sugar", "(120%) Over sugar"]
    count_level = 0
    for num in level:
        count_level = count_level + 1
        print(f"{count_level} : {num}")
    global sweetLe
    sweetLe = input("Do you want to add sugar? press number: ")


print(">>>>> Hello, Sir Welcome to PAP Coffee. My name is Pape robot. <<<<<")
require = input("Do you want to order coffe? press y or n: ")
name = input("Enter your name: ")

if require == "y":
    for item in range(10):
        item = item+1
        SelectOrder()
        dataOrder = "(" + str(item) + ") " + typeSe(typeOf) + " " + swMenu(orderIs) + " sweet level " + sweetLevel(sweetLe)
        if item > 1:
            dataOrder_new = dataOrder_tem + " and \n" + dataOrder
            print(dataOrder_new)
            dataOrder_tem = dataOrder_new
            # price
            price_new = priceOrder_tem + countPay + count_typeSe
            priceOrder_tem = price_new
        else:
            print(dataOrder)
            dataOrder_tem = dataOrder
            priceOrder_tem = countPay + count_typeSe

        otherMenu = input("Anything else? press y or n: ")
        if otherMenu == "n":
            print("Price amount total =", priceOrder_tem)
            # telNum = input("Fill in the Telephone number: ")
            # print(telNum)
            break
        