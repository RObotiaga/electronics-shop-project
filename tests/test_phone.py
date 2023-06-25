from src.item import Item
from src.phone import Phone
import pytest
def test_phone_initialization():
    phone = Phone("iPhone X", 999, 1, 2)
    assert phone.name == "iPhone X"
    assert phone.price == 999
    assert phone.quantity == 1
    assert phone.sim_count == 2

def test_phone_addition():
    phone1 = Phone("iPhone X", 999, 1, 2)
    phone2 = Phone("Samsung Galaxy S9", 799, 1, 1)
    phone1 += phone2
    assert phone1.quantity == 2

def test_phone_addition_invalid_type():
    phone = Phone("iPhone X", 999, 1, 2)
    item = Item("Headphones", 99, 1)
    with pytest.raises(TypeError):
        phone += item

def test_phone_representation():
    phone = Phone("iPhone X", 999, 1, 2)
    assert repr(phone) == "Phone('iPhone X', 999, 1, 2)"