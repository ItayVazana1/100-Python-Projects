from CoffeeMachin_Package import coffee_maker
from CoffeeMachin_Package import menu
from CoffeeMachin_Package import money_machine

machine_flag = True

coffee_machine = coffee_maker.CoffeeMaker()
money_handler = money_machine.MoneyMachine()
machine_menu = menu.Menu()

def show_report():
    print("\n****** Report ******")
    coffee_machine.report()
    money_handler.report()
    print("******  END  ******\n")


while machine_flag:

    show_report()
    print("Hey , Welcome to the Coffee Machine")
    print("I can make for you one of this:")
    print(machine_menu.get_items())
    user_input = input("please type your order:\n")
    order = machine_menu.find_drink(user_input)
    if order is not None:
        if coffee_machine.is_resource_sufficient(order):
            if money_handler.make_payment(order.cost):
                coffee_machine.make_coffee(order)
                show_report()
                user_input = input("\nTo continue type 'c' , otherwise type any key..\n>> ").lower()
                if user_input != 'c':
                    machine_flag = False
