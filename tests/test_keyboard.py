import pytest

from src.keyboard import Keyboard, ChangeLang


@pytest.fixture
def keyboard():
    return Keyboard('Keyboard', 10.0, 5)


def test_keyboard_initialization(keyboard):
    assert keyboard.name == 'Keyboard'
    assert keyboard.price == 10.0
    assert keyboard.quantity == 5


def test_keyboard_string_representation(keyboard):
    assert str(keyboard) == 'Keyboard'


def test_change_language_initialization():
    change_lang = ChangeLang()
    assert change_lang.language == 'EN'


def test_change_language_setting_valid_value():
    change_lang = ChangeLang()
    change_lang.language = 'RU'
    assert change_lang.language == 'RU'


def test_change_language_setting_invalid_value():
    change_lang = ChangeLang()
    with pytest.raises(AttributeError):
        change_lang.language = 'FR'


def test_change_language_toggle_from_en_to_ru():
    change_lang = ChangeLang()
    change_lang.language = 'EN'
    change_lang.change_lang()
    assert change_lang.language == 'RU'


def test_change_language_toggle_from_ru_to_en():
    change_lang = ChangeLang()
    change_lang.language = 'RU'
    change_lang.change_lang()
    assert change_lang.language == 'EN'


def test_change_language_toggle_twice():
    change_lang = ChangeLang()
    change_lang.change_lang()
    change_lang.change_lang()
    assert change_lang.language == 'EN'
