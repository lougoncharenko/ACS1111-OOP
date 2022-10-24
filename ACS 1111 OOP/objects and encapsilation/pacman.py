class PacMan():
    __init__(self):
        pass 


class Pellet:
    __init__(self, x, y):
        self.x = x
        self.y = y
    
    def is_eaten(self):
        print('eaten')



class CoffeeOrder():
    __init__(self, size, espresso, milk, flavor):
        self.size = size
        self.espresso = espresso
        self.milk = milk
        self.flavor = flavor


class CoffeeOrder():
    __init__(self, customer_name, menu_item, has_milk):
        self.customer_name = customer_name
        self.menu_item = menu_item
        self.has_milk = has_milk


adriana_order = CoffeeOrder('adriana', 'latte', true)
louisa_order = CoffeeOrder('louisa', 'cold brew', false)
