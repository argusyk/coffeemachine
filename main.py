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


# TODO 2: Define check_resources()


def check_resources(water, milk, coffee):
    not_enough_water = False
    not_enough_coffee = False
    not_enough_milk = False

    if resources["water"] < water:
        print("There is not enough water!")
        not_enough_water = True
    if resources["milk"] < milk:
        print("There is not enough milk!")
        not_enough_milk = True
    if resources["coffee"] < coffee:
        print("There is not enough coffee!")
        not_enough_coffee = True
    if not_enough_coffee or not_enough_milk or not_enough_water:
        return False
    else:
        return True


# TODO 8. Define input_money()


def input_money():
    guess = input("Do you want to add some money (Y) or (N)? ")
    if guess.lower() == "y":
        try:
            quarters = int(input("Input number of quarters:"))
            dimes = int(input("Input number of dimes:"))
            nickles = int(input("Input number of nickles:"))
            pennies = int(input("Input number of pennies:"))
            resources["money"] += quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
            return True
        except TypeError:
            return False
    else:
        return False


# TODO 3. Define check_money()


def check_money(coffee):
    if resources["money"] < MENU[coffee]["cost"]:
        print(f"Not enough money to make a {coffee}!")
        return False
    return True


# TODO 9. Define update_resources()


def update_resources(coffee):
    resources["water"] -= MENU[coffee]["ingredients"]["water"]
    resources["coffee"] -= MENU[coffee]["ingredients"]["coffee"]
    if coffee != "espresso":
        resources["milk"] -= MENU[coffee]["ingredients"]["milk"]
    resources["money"] -= MENU[coffee]["cost"]


# TODO 4. Define make_espresso()


def make_espresso():
    if check_resources(water=MENU["espresso"]["ingredients"]["water"],
                       coffee=MENU["espresso"]["ingredients"]["coffee"],
                       milk=0) and check_money("espresso"):
        update_resources("espresso")


# TODO 5. Define make_latte()


def make_latte():
    if check_resources(water=MENU["latte"]["ingredients"]["water"],
                       coffee=MENU["latte"]["ingredients"]["coffee"],
                       milk=MENU["latte"]["ingredients"]["milk"]) and check_money("latte"):
        update_resources("latte")


# TODO 6. Define make_cappuccino()


def make_cappuccino():
    if check_resources(water=MENU["cappuccino"]["ingredients"]["water"],
                       coffee=MENU["cappuccino"]["ingredients"]["coffee"],
                       milk=MENU["cappuccino"]["ingredients"]["milk"]) and check_money("cappuccino"):
        update_resources("cappuccino")


# TODO 7. Define print_report()


def print_report():
    print("There is {}ml of water.".format(resources["water"]))
    print("There is {}mg of coffee.".format(resources["coffee"]))
    print("There is {}ml of milk.".format(resources["milk"]))
    print("There is {}$ of charge.".format(resources["money"]))


online = True

# TODO 1.  “What would you like? (espresso/latte/cappuccino):”

while online:
    input_money()
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "espresso":
        make_espresso()
    if choice == "latte":
        make_latte()
    if choice == "cappuccino":
        make_cappuccino()
    if choice == "report":
        print_report()
    if choice == "off":
        online = False
