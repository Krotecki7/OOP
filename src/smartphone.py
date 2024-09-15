from src.product import Product


class Smartphone(Product):
    def __init__(
        self, name, description, price, quantity, efficiency, model, memory, color
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        if type(other) is Smartphone:
            value_1 = self.price * self.quantity
            value_2 = other.price * other.quantity
            return value_1 + value_2
        raise TypeError
