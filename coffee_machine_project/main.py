MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

coin_values = {
    "quarter": 0.25,
    "dime": 0.1,
    "nickel": 0.05,
    "penny": 0.01,
}

machine_on = True

# Function to calculate money entered by usser
def calc_input_money(coin_1, coin_2, coin_3, coin_4):
    '''Takes the quantity of each coin and returns the total value'''
    return (coin_1 * 0.25) + (coin_2 * 0.1) + (coin_3 * 0.05) + (coin_4 * 0.01)


# Function to check if the user has sufficient money to buy the chosen drink
def is_sufficient_money(user_money, chosen_drink):
    return user_money >= MENU[chosen_drink]["cost"]
    
# function to check if there is enough resources in inventory
def is_sufficient_water(chosen_drink, resource_left):
    return resource_left["water"] > MENU[chosen_drink]["ingredients"]["water"]

def is_sufficient_milk(chosen_drink, resource_left):
    return resource_left["milk"] > MENU[chosen_drink]["ingredients"]["milk"]
    
def is_sufficient_coffee(chosen_drink, resource_left):
    return resource_left["coffee"] > MENU[chosen_drink]["ingredients"]["coffee"]


def check_resources(chosen_drink, resource_left):
    return is_sufficient_water(chosen_drink, resource_left) and is_sufficient_milk(chosen_drink, resource_left) and is_sufficient_coffee(chosen_drink, resource_left)

# Function to update the inventory if the purchase is succesful (substract resources and save the money)


# funcion que muestre el reporte de los recursos restantes y el dinero obtenido

# funcion de compra
''' Debe preguntar qué bebida quiere
    Debe preguntar el dinero
    Debe calcular cuánto dinero es
    Debe chequear que sea suficiente
    Si no es suficiente informar y devolver el dinero
    Si es suficiente debe actualizar el inventario
    Mostrar el output (cafe y cambio)
'''

while machine_on:
    selected_drink = input("What would you like? (espresso/latte/cappuccino): ")

    # Turn off the machine functionality
    if selected_drink == "off":
        break


    selected_drink = "latte"
    print("Please insert coins.")
    quaters = int(input("How many quaters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))

    user_current_money = calc_input_money(quaters, dimes, nickels, pennies)
    print(user_current_money)

    if not is_sufficient_money(user_current_money, selected_drink):
        print("Sorry that's not enough money. Money refunded.")

    if not is_sufficient_water(selected_drink, resources):
        print("Sorry there is not enough water.")
    if not is_sufficient_milk(selected_drink, resources):
        print("Sorry there is not enough milk.")
    if not is_sufficient_coffee(selected_drink, resources):
        print("Sorry there is not enough coffee.")



# TODO: Make sure the user types a correct input