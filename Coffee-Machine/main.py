from menu import MENU
from menu import resources


# 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
def money_transact(coffee):
    print("Please insert coins.")
    quarter = int(input("How many quarters?: "))*0.25
    dime = int(input("How many dimes?: "))*0.1
    nickle = int(input("How many nickles?: "))*0.05
    penny = int(input("How many pennies?: "))*0.01


    total_money_given = quarter + dime + nickle + penny
    needed_money = MENU[coffee]['cost']

    if total_money_given < needed_money:
        print("Sorry that's not enough money. Money refunded.")
        return 0

    elif total_money_given == needed_money:
        resources['money']+= needed_money
        return 1

    else:
        change = round(total_money_given - needed_money, 2)
        print(f"Here is ${change} in change.")  

        resources['money']+= needed_money
        return 1

def get_resources(coffee):
    # coffee = 'latte'
    
    coffee_type = MENU[coffee]['ingredients']
    needed_resources = [coffee_type['water'], coffee_type['milk'], coffee_type['coffee'], MENU[coffee]['cost']]

    remaining_resources= [resources['water'], resources['milk'], resources['coffee'], resources['money']]
 
   
    key_list = list(resources.keys())[list(resources.values()).index(remaining_resources[0])]
    key_list1 = list(resources.keys())[list(resources.values()).index(remaining_resources[1])]
    key_list2 = list(resources.keys())[list(resources.values()).index(remaining_resources[2])]
 

    if remaining_resources[0]>= needed_resources[0]:
        if remaining_resources[1]>= needed_resources[1]:
            if remaining_resources[2]> needed_resources[2]:
                if money_transact(coffee)==1:
                    x = f"Here is your {coffee}☕. Have a good day! \n"
                    return print(x)
            elif remaining_resources[2]== needed_resources[2]:
                if money_transact(coffee)==1:
                    x = f"Here is your {coffee}☕. Have a good day! \n"
                    return print(x)
            else:
                if money_transact(coffee)==0:
                    x=f"There is no enough {key_list2}\n"
                    return print(x)
        else:
            if money_transact(coffee)==0:
                x=f"There is no enough {key_list1}\n"
                return print(x)
    else:
        if money_transact(coffee)==0:
            x=f"There is no enough {key_list}\n"
            return print(x)

def get_menu():
    coffee = 'cappuccino'
    coffee_type = MENU[coffee]['ingredients']
    for i in coffee_type:
        print(f"{i.capitalize()}: {coffee_type[i]}")



def machine():
    coffee = input("What would you like? (espresso/latte/cappuccino): ")

    if coffee == 'espresso' or coffee == 'latte' or coffee == 'cappuccino':
        "Turn off the Coffee Machine by entering “off” to the prompt."
        get_resources(coffee)

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

machine()        