def swMenu(question1):
    if int(question1) == 1:
        return "Affogato"
    elif int(question1) == 2:
        return "Espresso"
    elif int(question1) == 3:
        return "Americano"
    elif int(question1) == 4:
        return "Cappuccino"
    elif int(question1) == 5:
        return "Mocha"
    elif int(question1) == 6:
        return "Latte"


print(">>>>> Hello, Sir Welcome to PAP Coffee. My name is Pape robot. <<<<<")
name = input("Enter your name: ")

menu = ["Affogato", "Espresso", "Americano", "Cappuccino", "Mocha", "Latte"]

count_menu = 0
for num in menu:
    count_menu = count_menu + 1
    print(f"{count_menu} : {num}")

print("What would you like to drink? {name}")
question1 = input("Press number of menu: ")
print("Okay ", swMenu(question1))

# print(type(menu))



    # print(type(count_menu))
    # print(type(num))
    # print(int(count_menu) + " : " + int(num))


