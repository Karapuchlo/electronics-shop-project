def test_name():
    assert False
import pytest
from main import Product
def test_get_total_price():
    product1 = Product("Телевизор", 30000, 10)
    assert product1.get_total_price() == 300000


def test_apply_discount():
    product2 = Product("Холодильник", 25000, 5)
    product2.price_level = 0.8
    product2.apply_discount()
    assert product2.get_total_price() == 100000



def test_get_total_inventory_value():
    assert Product.get_total_inventory_value() == 425000
