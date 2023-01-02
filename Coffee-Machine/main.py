from menu import MENU
from menu import resources
from replit import clear
from art import logo

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
    coffee_type = MENU[coffee]['ingredients']
    needed_resources = [coffee_type['water'], coffee_type['milk'], coffee_type['coffee'], MENU[coffee]['cost']]

    remaining_resources= [resources['water'], resources['milk'], resources['coffee'], resources['money']]
   
    key_list = list(resources.keys())[list(resources.values()).index(remaining_resources[0])]
    key_list1 = list(resources.keys())[list(resources.values()).index(remaining_resources[1])]
    key_list2 = list(resources.keys())[list(resources.values()).index(remaining_resources[2])]
 

    if remaining_resources[0]>= needed_resources[0]:
        if remaining_resources[1]>= needed_resources[1]:
            if remaining_resources[2]>= needed_resources[2]:
                if money_transact(coffee)==1:
                    x = f"Here is your {coffee}☕. Have a good day! \n"
                    return print(x)
                else:
                    x = "Sorry that's not enough money. Money refunded.\n"
                    return print(x)
            else:
                x = f"There is no {key_list2}\n"
                return print(x)
        else:
            x = f"There is no {key_list1}\n"
            return print(x)
    else:
        x = f"There is no {key_list}\n"
        return print(x)

def deduct_resources():
    coffee = 'cappuccino'
    coffee_type = MENU[coffee]['ingredients']
    for i in coffee_type:
        print(f"{i.capitalize()}: {coffee_type[i]}")


def machine():
    if 1 == 1:
        counter = 12
        while counter>=1:
            # clear()
            print(logo)
            coffee = input("What would you like? (espresso/latte/cappuccino): ")

            if coffee == 'espresso' or coffee == 'latte' or coffee == 'cappuccino':
                get_resources(coffee)
                counter-=1
                continue

            elif coffee == 'report':
                for i in resources:
                    print(f"{i.capitalize()}: {resources[i]}")
                counter-=1
                continue
                
            elif coffee == "off":
                print("Shutting Down.....")
                break

            else:
                print("Not Available")
                break

machine()        