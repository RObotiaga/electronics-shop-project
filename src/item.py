import csv
import os


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса Item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self._name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self._name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self._name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if len(value) <= 10:
            self._name = value
        else:
            raise ValueError("Длина наименования товара превышает 10 символов.")

    def __add__(self, other):
        """
        Реализует операцию сложения экземпляров классов Item и Phone.

        :param other: Другой объект для сложения.
        :return: Объект с обновленным количеством товара в магазине.
        """
        if isinstance(other, Item):
            self.quantity += other.quantity
            return self
        else:
            raise TypeError("Можно сложить только экземпляры классов Item и Phone.")
    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * Item.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        """
        Инициализирует экземпляры класса Item данными из файла src/items.csv.
        """
        Item.all = []
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'items.csv'), 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row['name']
                price = float(row['price'])
                quantity = int(row['quantity'])
                cls(name, price, quantity)

    @staticmethod
    def string_to_number(value):
        """
        Возвращает число из числа-строки.

        :param value: Число-строка.
        :return: int Преобразованное число.
        """
        return int(value)
