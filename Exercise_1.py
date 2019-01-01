#Making an online shopping list app

groceries = []

def show_help():
        print("""type HELP for help options
         type DONE to finish the list
         type SHOW to display the current list
        """)

while True:
    new_item = (input("Item: "))
    if new_item.upper() == "DONE":
        print(f"Your final list is {groceries}")
        break
    elif new_item.upper() == "HELP":
        show_help()
        continue
    elif new_item.upper() == "SHOW":
        print(groceries)
        continue
    else:
        groceries.append(new_item)
        if len(groceries) == 1:
            print(f"Your list now has {len(groceries)} item in it.")
        elif len(groceries) >= 2:
            print(f"Your list now has {len(groceries)} items in it.")

