from src.item import Product
# миксин, содержащий логику для работы с языком
class KeyboardMixin:
    LANGUAGES = ['EN', 'RU']

    def __init__(self, name, price, language='EN'):
        self._language = language
        super().__init__(name)
        self.price = price

    def change_lang(self, lang):
        if lang in self.LANGUAGES:
            self._language = lang
        else:
            raise ValueError(f"Language {lang} is not supported")

class KeyBoard(Product, KeyboardMixin):
    def __init__(self, name, price, language='EN'):
        self.price = price
        super().__init__(name=name, language=language)