import data
from sandwich_maker import SandwichMaker
from cashier import Cashier

# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()


def main():
    is_on = True

    while is_on:
        choice = input("What size sandwich would you like? (small/medium/large): ").lower()
        if choice == "off":
            is_on = False
        elif choice in recipes:
            sandwich_cost = recipes[choice]["cost"]
            print(f"Your sandwich costs ${sandwich_cost}.")

            # Process coins
            payment = cashier_instance.process_coins()

            # Check if the transaction is successful
            if cashier_instance.transaction_result(payment, sandwich_cost):
                ingredients = recipes[choice]["ingredients"]

                # Check if resources are enough and make the sandwich
                if sandwich_maker_instance.check_resources(ingredients):
                    sandwich_maker_instance.make_sandwich(choice, ingredients)
        else:
            print("Sorry, we don't have that option.")


if __name__ == "__main__":
    main()
