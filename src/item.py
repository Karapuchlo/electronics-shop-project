import csv
class Product:
  price_level = 1.0
  products = []

  def __init__(self, name, price, quantity):
    self.name = name
    self.price = price
    self.quantity = quantity
    self.__class__.products.append(self)

  def __str__(self):
    return f"{self.name}: {self.price} x {self.quantity}"

  def __repr__(self):
    return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

  @property
  def name(self):
      return self.__name

  @name.setter
  def name(self, value):
    if len(value) <= 10:
      self.__name = value
    else:
      print('Длина наименования товара превышает 10 символов.')

  @classmethod
  def instantiate_from_csv(cls):
    cls.products = []
    with open('../src/items.csv', 'r') as csvfile:
      reader = csv.reader(csvfile)
      next(reader)  # пропускаем заголовок
      for row in reader:
        name, price, quantity = row
        item = Product(name, price, quantity)
        #cls.products.append(item)

  @staticmethod
  def string_to_number(string):
    if '.' in string:
      return int(float(string))
    else:
      return int(string)

  @classmethod
  def get_total_inventory_value(self):
    return sum([product.quantity * product.price for product in self.products])
  def get_total_price(self):
    return self.quantity * self.price

  def apply_discount(self):
     self.price *= self.price_level

  def __add__(self, other):
    if type(other) == type(self):
      return Product(self.name, self.price, self.quantity + other.quantity)
    elif isinstance(other, Product):
      return Product(other.name, other.price, self.quantity + other.quantity)
    else:
      raise TypeError(f"unsupported operand type(s) for +: '{type(self)}' and '{type(other)}'")
