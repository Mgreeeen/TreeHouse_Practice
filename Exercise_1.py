#Making an online shopping list app
import os
groceries = []

def clear_screen():
    os.system("cls")

def show_list():
    clear_screen()
    print("Here's your current list: ")
    for number, item in enumerate(groceries, start= 1):
        print(f"{number}. {item}. ")
    print("-" * 10)

def show_help():
    print("""type HELP for help options
type DONE to finish the list
type SHOW to display the current list
type REMOVE to remove an item from the list
""")

show_help()

def add_to_list(new_item):
    if len(groceries):
        position = input(f"""> Where should I add {new_item} to the list?\n
Press ENTER to add to the end of the list:  """)
    else:
        position = 0
    try:
        position = abs(int(position))
    except ValueError:
        position = None
    if position is not None:
        groceries.insert(position-1, new_item)
    show_list()
    if position is None:
        groceries.append(new_item)
        show_list()

def remove_item():
    show_list()
    removed = input("Which item would you like removed from the list?: ")
    try:
        print(f"{removed} has been removed from the list.")
        groceries.remove(removed)
    except ValueError:
        print("That item is not on the list.")


while True:
    new_item = (input("Item: "))
    if new_item.upper() == "DONE":
        clear_screen()
        print("Your final list is: ")
        for number, item in enumerate(groceries, start=1):
            print(f"{number}. {item}.")
        quit()

    elif new_item.upper() == "HELP":
        clear_screen()
        show_help()
        continue

    elif new_item.upper() == "SHOW":
        show_list()
        continue

    elif new_item.upper() == "REMOVE":
        remove_item()
        continue

    else:
        add_to_list(new_item)
