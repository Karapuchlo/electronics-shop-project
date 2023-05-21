import pytest
from src.item import Product
from src.phone import Phone
from src.keyboard import KeyBoard
def test_name():
    item1 = Product('Смартфон', 10000, 1)
    assert item1.name == 'Смартфон'

def test_get_total_price():
    product1 = Product("Телевизор", 30000, 10)
    assert product1.get_total_price() == 300000


def test_apply_discount():
    product2 = Product("Холодильник", 25000, 5)
    product2.price_level = 0.8
    product2.apply_discount()
    assert product2.get_total_price() == 100000

def test_get_total_inventory_value():
    assert Product.get_total_inventory_value() == 410000

def test_instantiate_from_csv():
    assert len(Product.products) == 3

def test_string_to_number():
    assert Product.string_to_number('5') == 5
    assert Product.string_to_number('5.0') == 5
    assert Product.string_to_number('5.5') == 5

def test_phone():
    # создаем экземпляр класса
    iphone = Phone("iPhone", 1000, 10, 2)
    # проверяем, что атрибуты экземпляра класса инициализируются корректно
    assert iphone.name == "iPhone"
    assert iphone.price == 1000
    assert iphone.quantity == 10
    assert iphone.num_sim == 2
    # проверяем, что __str__ возвращает корректное представление экземпляра класса
    assert str(iphone) == "iPhone"
    # проверяем, что __repr__ возвращает корректное представление экземпляра класса
    assert repr(iphone) == "Phone('iPhone', 1000, 10, 2)"
    # пытаемся создать экземпляр класса с некорректными данными
    android = Phone("Android", "ten dollars", "five", 1)
    # проверяем, что экземпляр класса не создался, атрибуты равны None

    assert android.price == None
    assert android.quantity == None
    assert android.num_sim == None
    # проверяем, что __str__ и __repr__ не вызывают ошибок
    assert str(android) == "None"
    assert repr(android) == "Phone(None, None, None, None)"

def test_keyboard():
    # создаем экземпляр класса
    keyboard = KeyBoard("Logitech", 50, 5)
    # проверяем, что получить описание экземпляра класса можно
    assert str(keyboard) == "Logitech"
    # проверяем, что вызвать метод change_lang() можно
    keyboard.change_lang()
    # проверяем, что свойство language поменялось
    assert keyboard.language == "RU"

