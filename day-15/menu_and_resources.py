

MENU = {
    "espresso": {
        "ingredients": {
            "water": 47,
            "coffe": 18
        },
        "cost": 1.5
    },
    "latte": {
        "ingredients": {
            "water": 180,
            "milk": 140,
            "coffe": 24

        },
        "cost": 2.5
    },
    "cappuccino": {
        "ingredients": {
            "water": 220,
            "milk": 110,
            "coffe": 24

        },
        "cost": 3.0
    }
}


MACHINE_COINS = {
    "Penny": {
        "value": 0.01,
        "count": 0
    },
    "Nickel": {
        "value": 0.05,
        "count": 0
    },
    "Dime": {
        "value": 0.1,
        "count": 0
    },
    "Quarter": {
        "value": 0.25,
        "count": 0
    }
}

# NTR = Need to refill

INGREDIENTS = {
    "water": {
        "amount": 350,
        "unit": "ml",
        "NTR": False,
        "max": 1250,
        "min": 50
    },
    "milk": {
        "amount": 330,
        "unit": "ml",
        "NTR": False,
        "max": 500,
        "min": 50
    },
    "coffe": {
        "amount": 75,
        "unit": "ml",
        "NTR": False,
        "max": 125,
        "min": 50
    }
}


ADVANCED_OPS = {
    1: "View Machine Report",
    2: "Refill Ingredients",
    3: "Collect Money",
    4: "Reboot Machine",
    5: "Turn off Machine"
}
