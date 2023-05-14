from src.item import Product
# миксин, содержащий логику для работы с языком
class LanguageMixin:
    layouts = ['EN', 'RU']
    current_layout = 0
    def __init__(self):
        self.language = 'EN'

    def change_lang(self):
        if self.current_layout >= 1:
            self.current_layout = (self.current_layout - 1)
        else:
            self.current_layout = (self.current_layout + 1)
        self.language = self.layouts[self.current_layout]
        print(f'Keyboard language changed to {self.layouts[self.current_layout]}')

    #@layouts.setter
    #def language(self,value):
        #raise AttributeError("AttributeError: property 'language' of 'KeyBoard' object has no setter")


class KeyBoard(Product, LanguageMixin):
    def __init__(self, _name, price, quantity):
        super().__init__(_name, price, quantity)
        LanguageMixin.__init__(self)
    def get_description(self):
        return f'{self._name}'
