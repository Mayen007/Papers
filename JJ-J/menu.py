# QUESTION 3(a)

print("WELCOME TO VAMAIKOS")
print("HOTEL")
print("*"*30)
print("*"*30)
print("*"*30)

# Define the menu as a dictionary with item numbers as keys and (item, price) as values.
menu = {
    1: ("Tilapia", 500),
    2: ("Matumbo", 200),
    3: ("Chai/Matumbo", 100),
    4: ("Mbuzi", 400),
    5: ("Githeri", 50),
}

# Display the menu to the client.
print("MENU")
for item_number, (item, price) in menu.items():
    print(f"{item_number}. {item} ------------------------------------- Kshs {price}")

# Get the client's selection.
while True:
    try:
        choice = int(input("Choose your food by typing a number (0 to quit): "))
        if choice == 0:
            break
        elif choice in menu:
            item, price = menu[choice]
            print(f"You chose {item} costing {price} Kenyan shillings")
            input("Press any key to continue...")
        else:
            print("Invalid item number. Please choose from the menu.")
    except ValueError:
        print("Invalid input. Please enter a valid item number.")
