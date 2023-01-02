from menu import MENU
from menu import resources


# 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
def type():
    coffee = input("What would you like? (espresso/latte/cappuccino): ")

    if coffee == 'espresso' or coffee == 'latte' or coffee == 'cappuccino':
        "Turn off the Coffee Machine by entering “off” to the prompt."
        

    elif coffee == 'report':
        def resource():
            """Returns resources available"""
            for i in resources:
                print(f"{i.capitalize()}: {resources[i]}")
        return resource()

# 2. Turn off the Coffee Machine by entering “off” to the prompt.
    elif coffee == "off":
        print("Shutting Down.....")
        exit()

    else:
        print("Not Available")

def get_resources():
    coffee = 'cappuccino'
    
    coffee_type = MENU[coffee]['ingredients']
    needed_resources = [coffee_type['water'], coffee_type['milk'], coffee_type['coffee'], MENU[coffee]['cost']]

    remaining_resources= [resources['water'], resources['milk'], resources['coffee'], resources['money']]
 
   
    key_list = list(resources.keys())[list(resources.values()).index(remaining_resources[0])]
    key_list1 = list(resources.keys())[list(resources.values()).index(remaining_resources[1])]
    key_list2 = list(resources.keys())[list(resources.values()).index(remaining_resources[2])]
 

    if remaining_resources[0]> needed_resources[0]:
        if remaining_resources[1]> needed_resources[1]:
            if remaining_resources[2]> needed_resources[2]:
                x = f"Here is your {coffee}☕. Have a good day! \n"
                return print(x)
            elif remaining_resources[2]== needed_resources[2]:
                x = f"Here is your {coffee}☕. Have a good day! \n"
                return print(x)
            else:
                x=f"There is no enough {key_list2}\n"
                return print(x)

        elif remaining_resources[1] == needed_resources[1]:
            if remaining_resources[2]> needed_resources[2]:
                x = f"Here is your {coffee}☕. Have a good day! \n"
                return print(x)
            elif remaining_resources[2]== needed_resources[2]:
                x = f"Here is your {coffee}☕. Have a good day! \n"
                return print(x)
            else:
                x=f"There is no enough {key_list2}\n"
                return print(x)

        elif remaining_resources[0] == needed_resources[0]:
            if remaining_resources[1]> needed_resources[1]:
                if remaining_resources[2]> needed_resources[2]:
                    x = f"Here is your {coffee}☕. Have a good! day \n"
                    return print(x)
                elif remaining_resources[2]== needed_resources[2]:
                    x = f"Here is your {coffee}☕. Have a good! day \n"
                    return print(x)
                else:
                    x=f"There is no enough {key_list2}\n"
                    return print(x)
            elif remaining_resources[1] == needed_resources[1]:
                if remaining_resources[2]> needed_resources[2]:
                    x = f"Here is your {coffee}☕. Have a good! day \n"
                    return print(x)
                elif remaining_resources[2]== needed_resources[2]:
                    x = f"Here is your {coffee}☕. Have a good! day \n"
                    return print(x)
                else:
                    x=f"There is no enough {key_list2}\n"
                    return print(x)
        else:
                x=f"There is no enough {key_list1}\n"
                return print(x)
    else:
        x=f"There is no enough {key_list}\n"
        return print(x)

def get_menu():
    coffee = 'cappuccino'
    coffee_type = MENU[coffee]['ingredients']
    for i in coffee_type:
        print(f"{i.capitalize()}: {coffee_type[i]}")
