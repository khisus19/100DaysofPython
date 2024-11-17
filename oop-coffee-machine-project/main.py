from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_menu = Menu()
my_machine = CoffeeMaker()

def calculate_total_money(qu, di, ni, pe):
	return round((qu * 0.25) + (di * 0.1) + (ni * 0.05) + (pe * 0.01), 2)

user_choice = input("What would you like? (espresso/latte/cappuccino/): ")

while user_choice != "off":

	if user_choice == "report":
		my_machine.report()

	user_choice = "latte"

	user_drink = my_menu.find_drink(user_choice)

	# TODO: If resource is sufficient continue with the sale my_machine.is_resource_sufficient(user_drink)
	if my_machine.is_resource_sufficient(user_drink):
		print("Please insert the coins")
		user_quarters = int(input("How many quarters?: "))
		user_dimes = int(input("How many dimes?: "))
		user_nickels = int(input("How many nickels?: "))
		user_pennies = int(input("How many pennies?: "))
		user_money = calculate_total_money(user_quarters, user_dimes, user_nickels, user_pennies)

		print(user_money)
		

	print()

	# print(my_machine.is_resource_sufficient(user_drink))

	
	user_choice = input("What would you like? (espresso/latte/cappuccino/): ")