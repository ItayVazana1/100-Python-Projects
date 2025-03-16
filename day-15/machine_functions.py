import os


def machine_report(current_ingredients, current_coins):
    print("***************")
    print("Machine Report")
    print("--------------")
    print("Ingredients:")
    for key in current_ingredients:
        print(f"{key} - {current_ingredients[key]['amount']}{current_ingredients[key]['unit']}")

    print("\nCoins:")
    total_value = 0
    for key in current_coins:
        print(f"{key} ({current_coins[key]['value']}$) :  {current_coins[key]['count']}")
        total_value += (current_coins[key]['count'] * current_coins[key]['value'])

    print(f"\nTotal value - {total_value}")
    print("--------------")
    print("***************")


def clear_screen():
    os.system('cls')
