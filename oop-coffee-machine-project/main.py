from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_menu = Menu()
my_coffee_machine = CoffeeMaker()
my_money_machine = MoneyMachine()
is_on = True



while is_on:
	options = my_menu.get_items()

	user_choice = input(f"What would you like? ({options}): ")

	if user_choice == "off":
		is_on = False
	elif user_choice == "report":
		my_coffee_machine.report()
		my_money_machine.report()
	else:
		drink = my_menu.find_drink(user_choice)

		# TODO: If resource is sufficient continue with the sale my_coffee_machine.is_resource_sufficient(user_drink)
		if my_coffee_machine.is_resource_sufficient(drink):
			# TODO: check if the transaction was succesfull

			if my_money_machine.make_payment(drink.cost):

				my_coffee_machine.make_coffee(drink)
