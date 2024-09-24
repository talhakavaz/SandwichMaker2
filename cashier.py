class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        """Returns the total calculated from coins inserted."""
        print("Please insert coins.")
        total = int(input("How many dollars? ")) * 100
        total += int(input("How many quarters? ")) * 25
        total += int(input("How many dimes? ")) * 10
        total += int(input("How many nickels? ")) * 5
        total += int(input("How many pennies? ")) * 1
        return total / 100  # Return the total in dollars

    def transaction_result(self, coins, cost):
        """Return True if payment is sufficient, False otherwise."""
        if coins >= cost:
            change = coins - cost
            print(f"Transaction successful. Here is ${change:.2f} in change.")
            return True
        else:
            print("Sorry, that's not enough money.")
            return False
