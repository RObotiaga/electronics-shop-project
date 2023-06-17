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
    assert fish1.calculate_total_price() == 500  # Измененное ожидаемое значение
    assert fish2.calculate_total_price() == 600

def test_apply_discount():
    Item.pay_rate = 0.9
    fish = Item('fish', 100, 5)
    fish.apply_discount()
    assert fish.price == 90  # 100 * 0.9

def test_name_setter():
    fish = Item('fish', 100, 5)
    assert fish.name == 'fish'
    fish.name = 'new_name'
    assert fish.name == 'new_name'
    try:
        fish.name = 'very_long_name'  # Должно выбросить ValueError
        assert False  # Если исключение не было выброшено, тест не пройден
    except ValueError:
        pass

def test_instantiate_from_csv():
    Item.all = []  # Сброс списка всех товаров перед каждым тестом
    Item.instantiate_from_csv()
    assert len(Item.all) == 5  # Проверяем, что экземпляры созданы
    assert Item.all[0].name == 'Смартфон'  # Проверяем значения атрибутов
    assert Item.all[0].price == 100
    assert Item.all[0].quantity == 1
    assert Item.all[1].name == 'Ноутбук'
    assert Item.all[1].price == 1000
    assert Item.all[1].quantity == 3

def test_string_to_number():
    assert Item.string_to_number('10') == 10
    assert Item.string_to_number('3') == 3
    assert Item.string_to_number('-2') == -2
    assert Item.string_to_number('100') == 100
    
def test_repr():
    item1 = Item("Смартфон", 10000, 20)
    assert  repr(item1) == "Item('Смартфон', 10000, 20)"
    
def test_str():
    item1 = Item("Смартфон", 10000, 20)
    assert  str(item1) == 'Смартфон'
