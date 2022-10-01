import day15_coffeemachinefiles as files

MENU = files.MENU

# Returns the user input for coffee type or other commands such as report and off
def order_coffee():
    valid_cmds = ["espresso", "latte", "cappuccino", "report", "off"]
    while True:
        cmd = input("What would you like? (espresso/latte/cappuccino)\n").lower()
        if cmd in valid_cmds:
            return cmd
        else:
            print("Please enter one of the drinks listed below:")

# Prints out the report
def print_report(resources_available, money_in_machine):
    for i in resources_available:
        print(f"{i.title()}: {resources_available[i]}")
    print(f"Money: ${money_in_machine}")

# Checks if there is enough resources to make the drink
def check_resources(order, resources_available):
    ingredient = MENU[order]["ingredients"]
    for i in MENU[order]["ingredients"]:
        if resources_available[i] >= ingredient[i]:
            return True
    else:
        print("Sorry, we don't have enough ingredients to make this drink.")
        return False

# Asks for user input on number of coins and returns it in a dictionary
def receive_coins():
    coins = {"penny": "", "nickel": "", "dime": "", "quarter": ""}
    for i in coins:
        while coins[i] == "":
            n = input(f"{i.title()}: ")
            try:
                int(n)
                if int(n) >= 0:
                    coins[i] = int(n)
                else:
                    print("Please enter a valid number")
            except ValueError:
                print("Please enter a valid number")
    return coins

# Takes the dictionary containing the number of coins and tabulates it to return the total value
def check_total(coins_received):
    total = 0
    for coin in coins_received:
        n = coins_received[coin]
        if coin == "penny":
            total += n
        elif coin == "nickel":
            total += n * 0.5
        elif coin == "dime":
            total += n * 0.10
        elif coin == "quarter":
            total += n * 0.25
    return total

# Checks if the value that the user gave is enough to pay for the drink
def check_cost(total_coins, order):
    order_cost = MENU[order]["cost"]
    if total_coins >= order_cost:
        return True
    else:
        print(f"Sorry, the drink costs ${order_cost} but you only gave ${total_coins}. Money refunded.")
        return False

# Reduces the resources after each order is made
def reduce_resources(resources_available, order):
    ingredient = MENU[order]["ingredients"]
    for i in MENU[order]["ingredients"]:
        resources_available[i] -= ingredient[i]
    return resources_available

def coffee_machine():
    resources_available = files.resources
    money_in_machine = 0
    end = False
    while end == False:
        order = order_coffee()
        if order == "report":
            print_report(resources_available, money_in_machine)
        elif order == "off":
            return
        else:
            enough_resources = check_resources(order, resources_available)
            if enough_resources:
                coins_received = receive_coins()
                total_coins = check_total(coins_received)
                enough_coins = check_cost(total_coins, order)
                if enough_coins:
                    order_cost = MENU[order]["cost"]
                    resources_available = reduce_resources(resources_available, order)
                    money_in_machine += order_cost
                    change = total_coins - order_cost
                    print(f"Here is ${change} in change.")
                    print(f"Here is your {order}. Enjoy!")
        
coffee_machine()