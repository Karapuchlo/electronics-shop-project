from src.item import Product

if __name__ == '__main__':
    # Файл items.csv отсутствует.
    Product.instantiate_from_csv()
    # FileNotFoundError: Отсутствует файл item.csv

    # В файле items.csv удалена последняя колонка.
    Product.instantiate_from_csv()
    # InstantiateCSVError: Файл item.csv поврежден
