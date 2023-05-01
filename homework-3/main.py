from src.item import Product

if __name__ == '__main__':
    item1 = Product("Смартфон", 10000, 20)
    assert repr(item1) == "Product('Смартфон', 10000, 20)"
    assert str(item1) == 'Смартфон'
