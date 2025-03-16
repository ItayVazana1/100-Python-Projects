from menu_and_resources import MENU, MACHINE_COINS, INGREDIENTS, ADVANCED_OPS
import machine_functions

machine_flag = True
order_flag = True


machine_functions.start_the_machine()

while machine_flag:
    machine_functions.show_menu(MENU)
    order = input("Type your command or order:\n").lower()
    if order == 'sys':
        machine_functions.advanced_mode(ADVANCED_OPS)
        op = input("Type your command:\n").lower()
        if op == '1':
            machine_functions.machine_report(INGREDIENTS, MACHINE_COINS)
        elif op == '2':
            print("refill")
        elif op == '3':
            print("collect")
        elif op == '4':
            machine_functions.reboot()
        elif op == '5':
            machine_functions.turn_off()
        else:
            print("Not a valid command code! back to menu..")
            order_flag = True


    if order_flag and machine_functions.take_an_order(order, menu=MENU, ingredients=INGREDIENTS, coins=MACHINE_COINS):
        machine_functions.make_order(order, menu=MENU, ingredients=INGREDIENTS, coins=MACHINE_COINS)


