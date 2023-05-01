import os
from src.item import Product

if __name__ == '__main__':
    item = Product('Телефон', 10000, 5)

    # длина наименования товара меньше 10 символов
    item.name = 'Смартфон'
    assert item.name == 'Смартфон'

    # длина наименования товара больше 10 символов
    item.name = 'СуперСмартфон'
    # Exception: Длина наименования товара превышает 10 символов.

    Product.instantiate_from_csv()  # создание объектов из данных файла
      # в файле 5 записей с данными по товарам