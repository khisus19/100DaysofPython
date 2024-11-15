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

# Function to calculate money entered by usser
def calc_input_money(coin_1, coin_2, coin_3, coin_4):
    '''Takes the quantity of each coin and returns the total value'''
    return (coin_1 * 0.25) + (coin_2 * 0.1) + (coin_3 * 0.05) + (coin_4 * 0.01)


# Function to check if the user has sufficient money to buy the chosen drink
def check_for_sufficient_money(user_money, chosen_drink):
    if user_money < MENU[chosen_drink]["cost"]:
        # print("You don't have enough money")
        return True
    else:
        return False
    
# function to check if there is enough resources in inventory
def is_sufficient_water(chosen_drink, resource_left):
    if resource_left["water"] > MENU[chosen_drink]["ingredients"]["water"]:
        return True
    else:
        return False

def is_sufficient_milk(chosen_drink, resource_left):
    if resource_left["milk"] > MENU[chosen_drink]["ingredients"]["milk"]:
        return True
    else:
        return False
    
def is_sufficient_coffee(chosen_drink, resource_left):
    if resource_left["coffee"] > MENU[chosen_drink]["ingredients"]["coffee"]:
        return True
    else:
        return False


def check_resources(chosen_drink, resource_left):
    if not is_sufficient_water(chosen_drink, resource_left):
        return "Sorry there is not enough water."
    elif not is_sufficient_milk(chosen_drink, resource_left):
        return "Sorry there is not enough milk."
    elif not is_sufficient_coffee(chosen_drink, resource_left):
        return "Sorry there is not enough coffee."

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

def purchase():
    selected_drink = input("What would you like? (espresso/latte/cappuccino): ")
    selected_drink = "latte"

    if (is_sufficient_water(selected_drink, resources) or is_sufficient_milk(selected_drink, resources) or is_sufficient_coffee(selected_drink, resources)):
        print(check_resources(selected_drink, resources))

purchase()