from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

print(logo)

first_input = float(input("What's the first number?: "))

chosen_operation = input("+\n-\n*\n/\nPick an operation: ")

# Loop until the player choose a correct operation
while chosen_operation not in operations:
    chosen_operation = input("+\n-\n*\n/\nPick a correct operation: ")

second_input = float(input("What's the next number?: "))

def calculate(n1, n2, symbol):
    """Takes two number and perform the operation chosen.
    It prints the result"""
    result = operations[symbol](n1, n2)
    print(f"{n1} {symbol} {n2} = {result}")
    return result

last_result = calculate(first_input, second_input, chosen_operation)

# Ask the player if they want to continue with the last result, start a new calculation or end the program
want_to_continue = input(f"Type 'y' to continue calculating with {last_result}, type 'n' to start a new calculation or type 'exit to end the program': ")

while want_to_continue != "exit":

    if want_to_continue == "y":
        chosen_operation = input("+\n-\n*\n/\nPick an operation: ")
        while chosen_operation not in operations:
            chosen_operation = input("+\n-\n*\n/\nPick a correct operation: ")
        second_input = float(input("What's the next number?: "))

        last_result = calculate(last_result, second_input, chosen_operation)
    else:
        print(logo)
        first_input = float(input("What's the first number?: "))
        chosen_operation = input("+\n-\n*\n/\nPick an operation: ")
        while chosen_operation not in operations:
            chosen_operation = input("+\n-\n*\n/\nPick a correct operation: ")
        second_input = float(input("What's the next number?: "))

        last_result = calculate(first_input, second_input, chosen_operation)

    # Update the want to continue so we can exit the program
    want_to_continue = input(f"Type 'y' to continue calculating with {last_result}, type 'n' to start a new calculation or type 'exit to end the program': ")

print("End of the program. Good day!")