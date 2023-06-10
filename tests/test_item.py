from src.item import Item

def test_init():
    fish = Item('fish', 100, 5)
    assert fish.name == 'fish'
    assert fish.price == 100
    assert fish.quantity == 5

def test_calculate_total_price():
    Item.all = []  # Сброс списка всех товаров перед каждым тестом
    fish1 = Item('fish1', 100, 5)
    fish2 = Item('fish2', 200, 3)
    assert fish1.calculate_total_price() == 1100

def test_apply_discount():
    Item.pay_rate = 0.9
    fish = Item('fish', 100, 5)
    fish.apply_discount()
    assert fish.price == 90  # 100 * 0.9
