from src.item import Item
class Phone(Item):
    def __init__(self,name,price,quantity, sim_count):
        super().__init__(name, price, quantity)
        self.sim_count = sim_count

    def __add__(self, other):
        if isinstance(other, Phone):
            self.quantity += other.quantity
            return self
        else:
            raise TypeError("Можно сложить только экземпляры классов Item и Phone.")
    def __repr__(self):
        return f"{self.__class__.__name__}('{self._name}', {self.price}, {self.quantity}, {self.sim_count})"

phone = Phone("iPhone X", 999, 1, 2)
repr(phone)