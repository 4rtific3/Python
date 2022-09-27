import day10_calculatorart as art

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

# asking for number inputs
# checks if using previous value, reduces input to 1 if true
# repositions operation input depending on whether previous value is being used
def num_input(bool):
    num_list = []
    if bool == True:
        x = 2
    else:
        x = 1
        symbol = operation(operations)
    for i in range(x):
        while True:
            num = input("Input a number: ")
            try:
                float(num)
                num_list.append(float(num))
                break
            except ValueError:
                print("Please input a number.")
        if i == 0 and x == 2:
            symbol = operation(operations)
    if x == 2:
        return num_list[0], num_list[1], symbol
    else:
        return num_list[0], symbol

def operation(dict):
    for i in dict:
        print(i)
    while True:
        symbol = input("Select an operation from above: ")
        if symbol in dict:
            return symbol
        else:
            print("Please choose a valid symbol.")

def cont_calc():
    while True:
        cont = input("Would you like to continue calculating with the previous value? Y/N: ").lower()
        if cont == "y":
            return True
        elif cont == "n":
            return False
        else:
            print('Please type "Y" or "N"')

# Recursion to restart calculator from the beginning to start a new calculation
# instead of closing the calculator
def repeat():
    first_calc = True
    cont = True
    while cont:
        if first_calc == True:
            a,b,symbol = num_input(first_calc)
        else:
            b,symbol = num_input(first_calc)
        result = round(operations[symbol](a,b), 2)
        print(f"{a} {symbol} {b} = {result}")
        cont = cont_calc()
        if cont == True:
            a = result
            first_calc = False
        else:
            repeat()

def run():
    print(art.logo)
    repeat()

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    }

run()