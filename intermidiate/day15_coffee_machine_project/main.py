MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

quarter = 0
dime = 0
nickel = 0
penny = 0
customer_money = quarter + dime + nickel + penny
def compare_resources(coffee):
    for ingredient in MENU[coffee]['ingredients']:
        if resources[ingredient] < MENU[coffee]['ingredients'][ingredient]:
            return "no"
    return "yes"
def print_resources():
    for item in resources:
        print(f"{item}: {resources[item]}")
def make_coffee(coffee, money):
    for ingredient in MENU[coffee]['ingredients']:
       resources[ingredient] -= MENU[coffee]['ingredients'][ingredient]
    resources['money'] += money


while True:
    decision = input("What would you like?(Espresso, Latte, Cappuccino?) or 'report' to see resources\n").lower()
    if decision == "report":
        print_resources()
    elif decision == "espresso":
        if compare_resources('espresso') == "yes":
            print("Please enter your coins\n")
            quarter = int(input("How many quarters?\n")) * 0.25
            dime = int(input("How many dimes?\n")) * 0.10
            nickel = int(input("How many nickels?\n")) * 0.05
            penny = int(input("How many pennies?\n")) * 0.01
            customer_money = quarter + dime + nickel + penny
            if customer_money >= MENU['espresso']["cost"]:
                make_coffee('espresso', customer_money)
                print_resources()
                print(f"Here is ${customer_money - MENU['espresso']['cost']} in change\n")
                print(f"Here is your {decision} ☕ Enjoy!")
            elif customer_money < MENU['espresso']["cost"]:
                print("Sorry you dont have enough money\n")
        elif compare_resources('espresso') == "no":
            print("Sorry, we dont have enough resources\n")
    elif decision == "latte":
        if compare_resources('latte') == "yes":
            print("Please enter coins\n")
            quarter = int(input("How many quarters?\n")) * 0.25
            dime = int(input("How many dimes?\n")) * 0.10
            nickel = int(input("How many nickels?\n")) * 0.05
            penny = int(input("How many pennies?\n")) * 0.01
            customer_money = quarter + dime + nickel + penny
            if customer_money >= MENU['latte']["cost"]:
                make_coffee('latte', customer_money)
                print_resources()
                print(f"Here is ${customer_money - MENU['latte']['cost']} in change\n")
                print(f"Here is your {decision} ☕ Enjoy!")
            elif customer_money < MENU['latte']["cost"]:
                print("Sorry you dont have enough money\n")
        elif compare_resources('latte') == "no":
            print("Sorry, we dont have enough resources\n")
    elif decision == "cappuccino":
        if compare_resources('cappuccino') == "yes":
            print("Please enter coins\n")
            quarter = int(input("How many quarters?\n")) * 0.25
            dime = int(input("How many dimes?\n")) * 0.10
            nickel = int(input("How many nickels?\n")) * 0.05
            penny = int(input("How many pennies?\n")) * 0.01
            customer_money = quarter + dime + nickel + penny
            if customer_money >= MENU['cappuccino']["cost"]:
                make_coffee('cappuccino', customer_money)
                print_resources()
                print(f"Here is ${customer_money - MENU['cappuccino']['cost']} in change\n")
                print(f"Here is your {decision} ☕ Enjoy!")
            elif customer_money < MENU['cappuccino']["cost"]:
                print("Sorry you dont have enough money\n")
        elif compare_resources('cappuccino') == "no":
            print("Sorry, we dont have enough resources\n")

