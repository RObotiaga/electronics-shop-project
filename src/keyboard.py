from src.item import Item


class ChangeLang:
    def __init__(self):
        self.language = 'EN'

    @property
    def language(self):
        return self._language

    @language.setter
    def language(self, value):
        if value not in ['RU', 'EN']:
            raise AttributeError("property 'language' of 'Keyboard' object has no setter")
        self._language = value

    def change_lang(self):
        if self.language == 'EN':
            self.language = 'RU'
        else:
            self.language = 'EN'
        return self


class Keyboard(Item, ChangeLang):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)

    def __str__(self):
        return self.name
