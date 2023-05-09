from src.item import Product
# миксин, содержащий логику для работы с языком
class LanguageMixin:
    def __init__(self):
        self._language = 'EN'

    def change_lang(self, new_lang):
        if new_lang in ('EN', 'RU'):
            self._language = new_lang
            print(f'Keyboard language changed to {new_lang}.')
        else:
            print(f'Unsupported language {new_lang}.')

class KeyBoard(Product, LanguageMixin):
    def __init__(self, _name, price, quantity):
        super().__init__(_name, price, quantity)

    def get_description(self):
        return f'{self._name}'
