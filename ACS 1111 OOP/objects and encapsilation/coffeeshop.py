

class CoffeeOrder():
    def __init__(self, customer_name, size, espresso_shots, milk, flavor):
        self.customer_name = customer_name
        self.size = size
        self.espresso_shots = espresso_shots
        self.milk = milk
        self.flavor = flavor

    def display_order(self):
        print(f'Customer {self.customer_name} ordered a {self.size} coffee with {self.espresso_shots} espresso shots with {self.milk} milk and {self.flavor} for flavor')


louisa_order = CoffeeOrder('louisa', 'large', '3', 'almond', 'mint')
louisa_order.display_order()