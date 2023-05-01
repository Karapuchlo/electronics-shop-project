import pytest
from src.item import Product

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
    assert Product.string_to_number('5.5') == 5.5
