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
        print("You don't have enough money")
    
# function to check if there is enough resources in inventory
def check_resources(chosen_drink, resource_left):
    if resource_left["water"] < MENU[chosen_drink]["ingredients"]["water"]:
        return "Sorry there is not enough water."
    elif resource_left["milk"] < MENU[chosen_drink]["ingredients"]["milk"]:
        return "Sorry there is not enough milk."
    elif resource_left["coffe"] < MENU[chosen_drink]["ingredients"]["coffe"]:
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