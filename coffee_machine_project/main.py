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
    "money": 0,
}

machine_on = True

# Function to calculate money entered by usser
def calc_input_money(coin_1, coin_2, coin_3, coin_4):
    '''Takes the quantity of each coin and returns the total value'''
    return round(((coin_1 * 0.25) + (coin_2 * 0.1) + (coin_3 * 0.05) + (coin_4 * 0.01)), 2)


# Function to check if the user has sufficient money to buy the chosen drink
def is_sufficient_money(user_money, chosen_drink):
    return user_money >= MENU[chosen_drink]["cost"]
    
# functions to check if there is enough resources in inventory
def is_sufficient_water(chosen_drink, resource_left):
    return resource_left["water"] >= MENU[chosen_drink]["ingredients"]["water"]

def is_sufficient_milk(chosen_drink, resource_left):
    return resource_left["milk"] >= MENU[chosen_drink]["ingredients"]["milk"]
    
def is_sufficient_coffee(chosen_drink, resource_left):
    return resource_left["coffee"] >= MENU[chosen_drink]["ingredients"]["coffee"]

def check_resources(chosen_drink, resource_left):
    return is_sufficient_water(chosen_drink, resource_left) and is_sufficient_milk(chosen_drink, resource_left) and is_sufficient_coffee(chosen_drink, resource_left)

# Function to update the inventory if the purchase is succesful (substract resources and save the money)
def update_inventory(chosen_drink, resource_left):
    resource_left["water"] -= MENU[chosen_drink]["ingredients"]["water"]
    resource_left["milk"] -= MENU[chosen_drink]["ingredients"]["milk"]
    resource_left["coffee"] -= MENU[chosen_drink]["ingredients"]["coffee"]
    resource_left["money"] = MENU[chosen_drink]["cost"]
    return resource_left

# Function that shows the report with the inventory
def show_report(resources_left):
    print(f"Water: {resources_left['water']}ml")
    print(f"Milk: {resources_left['milk']}ml")
    print(f"Coffee: {resources_left['coffee']}g")
    print(f"Money: ${resources_left['money']}")


while machine_on:
    selected_drink = input("What would you like? (espresso/latte/cappuccino): ")

    # Turn off the machine functionality
    if selected_drink == "off":
        break

    if selected_drink in MENU.keys():

        # Check if there is enough ingredients to continue
        if not is_sufficient_water(selected_drink, resources):
            print("Sorry there is not enough water.")
        elif not is_sufficient_milk(selected_drink, resources):
            print("Sorry there is not enough milk.")
        elif not is_sufficient_coffee(selected_drink, resources):
            print("Sorry there is not enough coffee.")
        else:
            # Continue with the purchase
            print("Please insert coins.")
            quaters = int(input("How many quaters?: "))
            dimes = int(input("How many dimes?: "))
            nickels = int(input("How many nickels?: "))
            pennies = int(input("How many pennies?: "))

            user_current_money = calc_input_money(quaters, dimes, nickels, pennies)
            user_change = round(user_current_money - MENU[selected_drink]['cost'], 2)

            if not is_sufficient_money(user_current_money, selected_drink):
                print("Sorry that's not enough money. Money refunded.")
            else:
                resources = update_inventory(selected_drink, resources)
                print(f"Here is ${user_change} in change.")
                print(f"Here is your {selected_drink} ☕️ . Enjoy!")

    else:
        show_report(resources)