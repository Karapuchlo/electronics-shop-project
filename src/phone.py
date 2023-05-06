from src.item import Product

class Phone(Product):
    def __init__(self, name, price, quantity, num_sim):
        super().__init__(name, price, quantity)
        self.num_sim = num_sim

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.num_sim})"

    def __add__(self, other):
        if isinstance(other, Phone):
            return Phone(self.name, self.price, self.quantity + other.quantity, self.num_sim)
        elif isinstance(other, Product):
            return Product(self.name, self.price, self.quantity + other.quantity)
        else:
            raise TypeError("Unsupported operand type(s) for +: 'Phone' and '{}'".format(type(other).__name__))