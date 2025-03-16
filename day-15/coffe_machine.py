from menu_and_resources import MENU, MACHINE_COINS, INGREDIENTS, ADVANCED_OPS
import machine_functions


machine_functions.start_the_machine()
machine_functions.machine_report(INGREDIENTS, MACHINE_COINS)
machine_functions.show_menu(MENU)
#machine_functions.advanced_mode(ADVANCED_OPS)

machine_functions.take_an_order("latte", MENU, INGREDIENTS, MACHINE_COINS)

