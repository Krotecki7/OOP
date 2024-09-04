class Product:
    """Описание продукта"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_dict):
        cls.name = product_dict["name"]
        cls.description = product_dict["description"]
        cls.__price = product_dict["price"]
        cls.quantity = product_dict["quantity"]
        return cls(name=cls.name, description=cls.description, price=cls.__price, quantity=cls.quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price: int):
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        self.__price = new_price
