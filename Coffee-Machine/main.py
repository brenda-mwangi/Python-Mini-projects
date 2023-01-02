from menu import MENU
from menu import resources


# 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
def type():
    coffee = input("What would you like? (espresso/latte/cappuccino): ")
    # coffee = 'latte'
    if coffee == 'espresso' or coffee == 'latte' or coffee == 'cappuccino':
        def get_menu():
            coffee_type = MENU[coffee]['ingredients']
            for i in coffee_type:
                print(f"{i.capitalize()}: {coffee_type[i]}")
        return get_menu()
    elif coffee == 'report':
        def resource():
            """Returns resources available"""
            for i in resources:
                print(f"{i.capitalize()}: {resources[i]}")
        return resource()

# 2. Turn off the Coffee Machine by entering “off” to the prompt.
    elif coffee == "off":
        "Turn off the Coffee Machine by entering “off” to the prompt."
        print("Shutting Down.....")
        exit()

    else:
        print("Not Available")

type()    