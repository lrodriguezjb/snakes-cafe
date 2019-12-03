import sys


# Created Introduction Layout
print("*" * 38)
print("**    Welcome to the Snakes Cafe!   **")
print("**    Please see our menu below.    **")
print("**                                  **")
print('** To quit at any time, type "quit" **')
print("*" * 38)

# Menu Dictionaries ----------------------

appetizers = {"wings": 0, "cookies": 0, "spring rolls": 0}

entrees = {
    "salmon": 0,
    "steak": 0,
    "meat tornado": 0,
    "a literal garden": 0,
}

desserts = {"ice cream": 0, "cake": 0, "pie": 0}

drinks = {"coffee": 0, "tea": 0, "unicorn tears": 0}

# -------------------

# Menu Layout by Iterating through each key in dictionary and printing a formatted capitalized version of the key onto screen
print("Appetizers\n--------")
for key, value in appetizers.items():
    print(f"{key.capitalize()}")
print("")
print("Entrees\n--------")
for key, value in entrees.items():
    print(f"{key.capitalize()}")

print("")
print("Desserts\n--------")
for key, value in desserts.items():
    print(f"{key.capitalize()}")

print("")
print("Drinks\n--------")
for key, value in drinks.items():
    print(f"{key.capitalize()}")
print("")

# What would you like to order final layout
print("*" * 38)
print("**   What would you like to order?  **")
print("*" * 38)

# -----------------------------


def orderinput():
    """
    This Function initializes the order question prompts for User with a while loop..
    Takes an Input and if the Input is part of the menu it then prints it out with the amount for each item.
    To break out of loop User has to type "Quit"
    """
    while True:
        addmore = "**   Anything else?  **"
        answer = input()
        answer = answer.lower()
        if answer in appetizers:
            appetizers[answer] += 1
            print(
                f"** {appetizers[answer]} order of {answer} have been added to your meal**"
            )
            print(addmore)
        if answer in entrees:
            entrees[answer] += 1
            print(
                f"** {entrees[answer]} order of {answer} have been added to your meal**"
            )
            print(addmore)
        if answer in desserts:
            desserts[answer] += 1
            print(
                f"** {desserts[answer]} order of {answer} have been added to your meal**"
            )
            print(addmore)
        if answer in drinks:
            drinks[answer] += 1
            print(
                f"** {drinks[answer]} order of {answer} have been added to your meal**"
            )
            print(addmore)
        if answer == "quit":
            print(f"Thank you for ordering! Bye-Bye!")
            sys.exit()


# Calling the Order Function
orderinput()

