import pytest

from src.item import Item
from src.phone import Phone


def test_phone_initialization():
    phone = Phone("iPhone X", 999, 1, 2)
    assert phone.name == "iPhone X"
    assert phone.price == 999
    assert phone.quantity == 1
    assert phone.number_of_sim == 2


def test_phone_addition():
    phone1 = Phone("iPhone X", 999, 1, 2)
    phone2 = Phone("Samsung Galaxy S9", 799, 2, 1)
    item1 = Item('рыба', 100, 3)
    phone1 + phone2
    assert phone1.quantity == 3
    assert item1 + phone2 == 5


def test_phone_addition_invalid_type():
    phone = Phone("iPhone X", 999, 1, 2)
    item = Item("Headphones", 99, 1)
    with pytest.raises(TypeError):
        phone += item


def test_phone_representation():
    phone = Phone("iPhone X", 999, 1, 2)
    assert repr(phone) == "Phone('iPhone X', 999, 1, 2)"
