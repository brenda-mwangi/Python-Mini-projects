from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from art import logo
drinks = Menu()


def machine():
    is_on = True

    while is_on:
        print(logo)
        user_input = input(f"What would you like? ({drinks.get_items()}): ")

        if user_input == 'off':
            print("Shutting down....")
            is_on = False
            
        elif user_input == 'report':
            CoffeeMaker().report()
            MoneyMachine().report()

        elif user_input == 'espresso' or user_input == 'latte' or user_input == 'cappuccino':
            user_drink = Menu().find_drink(user_input)
            is_resource_sufficient = CoffeeMaker().is_resource_sufficient(user_drink)

            if is_resource_sufficient and MoneyMachine().make_payment(user_drink.cost):
                CoffeeMaker().make_coffee(user_drink)
        
        else:
            user_drink = drinks.find_drink(user_input)
            continue

machine() 
