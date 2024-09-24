class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        """Returns True if there are enough ingredients to make the sandwich."""
        for item, amount_required in ingredients.items():
            if self.machine_resources[item] < amount_required:
                print(f"Sorry, not enough {item}.")
                return False
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from resources and print success message."""
        for item, amount_required in order_ingredients.items():
            self.machine_resources[item] -= amount_required
        print(f"Here is your {sandwich_size} sandwich. Enjoy!")
