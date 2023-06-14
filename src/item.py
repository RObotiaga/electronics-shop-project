import csv

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self._name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if len(value) <= 10:
            self._name = value
        else:
            raise ValueError("The name should not exceed 10 characters.")

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
        with open('src/items.csv', 'r') as file:
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
        :return: Преобразованное число.
        """
        return float(value)
