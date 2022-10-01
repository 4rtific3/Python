from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

def coffee_machine():
    exit = False
    while not exit:
        drinks = menu.get_items()
        cmd = input(f"What would you like? ({drinks}): ")
        if cmd == "off":
            return
        elif cmd == "report":
            coffee_maker.report()
            money_machine.report()
        else:
            order = menu.find_drink(cmd)
            if coffee_maker.is_resource_sufficient(order):
                if money_machine.make_payment(order.cost):
                    coffee_maker.make_coffee(order)

coffee_machine()