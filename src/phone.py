from src.item import Product

class Phone(Product):
    def __init__(self, name, price, quantity, num_sim):
        super().__init__(name, price, quantity)
        self.num_sim = num_sim

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.num_sim})"
