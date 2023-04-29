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
      with open('src/item.csv', 'r') as f:
          for line in f:
              name, price, quantity = line.strip().split(',')
              item = cls(name, price, quantity)

  @staticmethod
  def string_to_number(string):
      return float(string)
  def get_total_price(self):
    return self.quantity * self.price * self.price_level

  def apply_discount(self):
      self.price * self.quantity * self.price_level

  @classmethod
  def get_total_inventory_value(self):
     return sum([product.quantity * product.price * self.price_level for product in self.products])

if __name__ == "__main__":
# Создаем экземпляры товаров
    product1 = Product("Телевизор", 30000, 10)
    product2 = Product("Холод", 25000, 5)

# Получаем общую стоимость конкретного товара
    print(product1.get_total_price())
    product1.price_level = 0.8
# Применяем скидку

    product1.apply_discount()
# Проверяем, что скидка была применена
    print(product1.get_total_price())

# Получаем общую стоимость всего запаса товаров в магазине
    print(Product.get_total_inventory_value())

    item = Product('Телефон', 10000, 5)

    # длина наименования товара меньше 10 символов
    item.name = 'Смартфон'
    assert item.name == 'Смартфон'

    # длина наименования товара больше 10 символов
    item.name = 'СуперСмартфон'
    # Exception: Длина наименования товара превышает 10 символов.

    Product.instantiate_from_csv()  # создание объектов из данных файла

    assert len(Product.products) == 9  # в файле 9 записей с данными по товарам