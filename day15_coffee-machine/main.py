from data import MENU, COINS

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
is_on = True


def print_report():
    print("Water: {}ml".format(resources["water"]))
    print("Milk: {}ml".format(resources["milk"]))
    print("Coffee: {}g".format(resources["coffee"]))
    print(f"Money: {profit}$")


def get_coins(order):
    order_cost = MENU[order]["cost"]
    print(f"{order} costs {order_cost}$")

    total_coins_value = 0
    for coin_name in COINS:
        how_many_coins = int(input(f"How many {coin_name}s? "))
        total_coins_value += COINS[coin_name] * how_many_coins
    return total_coins_value


def make_coffee(order):
    required_resources = MENU[order]["ingredients"]
    for resource_name in required_resources:
        resources[resource_name] -= required_resources[resource_name]
    print(f"Here's your ☕{order}. Enjoy!")


def handle_order_payment(user_order):
    inserted_coins_value = get_coins(user_order)
    change = 0

    order = MENU[user_order]

    if inserted_coins_value < order["cost"]:
        print(f"Sorry that's not enough money. Money refunded.")
        return
    elif inserted_coins_value > order["cost"]:
        change = inserted_coins_value - order["cost"]
        print(f"Here is ${change} dollars in change.")

    global profit
    profit += inserted_coins_value - change


def check_resources_sufficiency(user_order):
    required_resources = MENU[user_order]["ingredients"]
    for resource_name in required_resources:
        if required_resources[resource_name] > resources[resource_name]:
            print(f"Sorry there is not enough {resource_name}.")
            return False
    return True


def take_order():
    menu_items = "/".join(list(MENU.keys()))
    user_order = input(f"What would you like? ({menu_items}): ").lower()

    if user_order == "off":
        print("Coffee machine turned off")
        global is_on
        is_on = False
    elif user_order == "report":
        print_report()
    elif user_order in MENU:
        result = check_resources_sufficiency(user_order)
        if not result:
            return

        handle_order_payment(user_order)
        make_coffee(user_order)
    else:
        print("NOT IN MENU")


while is_on:
    take_order()
