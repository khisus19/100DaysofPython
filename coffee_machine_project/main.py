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

def calc_input_money(coin_1, coin_2, coin_3, coin_4):
    return (coin_1 * 0.25) + (coin_2 * 0.1) + (coin_3 * 0.05) + (coin_4 * 0.01)


# funcion que calcule el dinero que ingresó
# funcion que verifique si el dinero ingresado es suficiente
# función que actualizar el inventario (restar recursos y guardar el dinero)
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