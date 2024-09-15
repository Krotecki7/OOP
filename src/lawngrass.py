from src.product import Product


class LawnGrass(Product):
    def __init__(
        self, name, description, price, quantity, country, germination_period, color
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        if type(other) is LawnGrass:
            value_1 = self.price * self.quantity
            value_2 = other.price * other.quantity
            return value_1 + value_2
        raise TypeError
