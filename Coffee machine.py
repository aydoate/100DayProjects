##List of Menu items
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
        },
        "cost": 1.50,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.50,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.00,
    }
}
##Resources
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_resources(drink):
    """Takes input drink and returns yes if there are enough resources, or no if not"""
    if resources["water"]>MENU[drink]["ingredients"]["water"] and resources["coffee"]>MENU[drink]["ingredients"]["coffee"] and resources["milk"]>MENU[drink]["ingredients"]["milk"]:
        return "yes"
    else:
        return "no"


def coins(drink):
    """takes input drink and asks user for coins. If enough coins for cost, dispenses drink and returns "drink", otherwise returns "no drink" """
    print(f"Your {drink} costs ${MENU[drink]["cost"]}. Please insert coins\n")
    quarters=int(input("how many quarters?"))
    dimes=int(input("how many dimes?"))
    nickels=int(input("how many nickels"))
    pennies=int(input("how many pennies?"))
    total= round(float((quarters*.25)+(dimes*.10)+(nickels*.05)+(pennies*.01)),2)
    print(f"${total}")
    if total>= MENU[drink]["cost"]:
        change=round(float(total-MENU[drink]["cost"]),2)
        print(f"Here is your ${change} in change.")
        print(f"Here is your {drink}. Enjoy!")
        return "drink"

    else:
        print("Sorry that's not enough money. Money refunded")
        return "no drink"



## Prompt user for inputs
machine_on="yes"
while machine_on=="yes":
    print(f"Current machine levels:")
    print(f"Water: {resources["water"]}")
    print(f"Milk: {resources["milk"]}")
    print(f"Coffee: {resources["coffee"]}")
    user_drink=input("What would you like? (espresso/latte/cappuccino)").lower()
    if user_drink=="off":
        machine_on="no"
        print("Have a nice day.")
    if user_drink=="report":
        print(f"Water: {resources["water"]}")
        print(f"Milk: {resources["milk"]}")
        print(f"Coffee: {resources["coffee"]}")
    elif user_drink=="espresso" or "latte" or "cappuccino":
        if check_resources(user_drink)=="yes" and coins(user_drink)=="drink":
            resources["water"]-=MENU[user_drink]["ingredients"]["water"]
            resources["milk"] -= MENU[user_drink]["ingredients"]["milk"]
            resources["coffee"] -= MENU[user_drink]["ingredients"]["coffee"]
        elif check_resources(user_drink)=="no":
            print("We're sorry, the machine needs to be restocked at this moment.")
            machine_on="no"


