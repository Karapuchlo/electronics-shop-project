class Product:
  price_level = 1.0
  products = []

  def __init__(self, name, price, quantity):
    self.name = name
    self.price = price
    self.quantity = quantity
    self.__class__.products.append(self)

  @property
  def name(self):
      return self._name

  @name.setter
  def name(self, value):
    if len(value) <= 10:
      self._name = value
    else:
      print('Длина наименования товара превышает 10 символов.')

  @classmethod
  def instantiate_from_csv(cls):
    with open('/src/item.csv', 'r') as f:
      for line in f:
        name, price, quantity = line.strip().split(',')
        item = cls(name, price, quantity)

  @staticmethod
  def string_to_number(string):
    return float(string)

  @classmethod
  def get_total_inventory_value(self):
    return sum([product.quantity * product.price * self.price_level for product in self.products])
  def get_total_price(self):
      return self.quantity * self.price * self.price_level

  def apply_discount(self):
     self.price *= self.price_level
