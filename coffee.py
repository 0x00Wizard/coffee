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
}

profit = 0


def is_resource_sufficient(order_ingredient):
    for item in order_ingredient:
        if order_ingredient[item] > resources[item]:
            print(f"Sorry not enough {item}")
            return False

    return True


def insert_coin():
    print("Please insert coin: ")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def is_transaction_successful(drink_cost, money_received):
    """Check that the user has inserted enough money to purchase the drink they selected."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True

    else:
        return "Sorry that's not enough money. Money refunded."


def make_coffee(order_ingredient, drink_name):
    for item in order_ingredient:
        resources[item] -= order_ingredient[item]
    print(f"Here is your {drink_name}. Enjoy!")


is_on = True

while is_on:
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if order == "off":
        is_on = False

    elif order == "report":
        print(
            f"Water: {resources['water']}ml\n"
            f"Milk: {resources['milk']}ml\n"
            f"Coffee: {resources['coffee']}g\n"
            f"Money: ${profit}\n"
        )
    else:
        drink = MENU[order]
        if is_resource_sufficient(drink["ingredients"]):
            payment = insert_coin()
            is_transaction_successful(drink["cost"], payment)
            make_coffee(drink["ingredients"], order)

