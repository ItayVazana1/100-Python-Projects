from menu_and_resources import MENU, MACHINE_COINS, INGREDIENTS, ADVANCED_OPS
import machine_functions

machine_flag = True

machine_functions.start_the_machine()

while machine_flag:
    machine_functions.show_menu(MENU)
    order = input("Insert your order:\n")
    if machine_functions.take_an_order(order, menu=MENU, ingredients=INGREDIENTS, coins=MACHINE_COINS):
        machine_functions.make_order(order, menu=MENU, ingredients=INGREDIENTS, coins=MACHINE_COINS)
        machine_functions.machine_report(current_ingredients=INGREDIENTS,current_coins=MACHINE_COINS)


    test_stop = input("Do you want to order again? insert yes , otherwise something else..").lower()
    if test_stop != 'yes':
        machine_flag = machine_functions.turn_off()

