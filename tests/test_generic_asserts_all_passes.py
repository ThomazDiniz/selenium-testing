import pytest

def test_addition():
    result = 2 + 3
    assert result == 5

def test_subtraction():
    result = 10 - 4
    assert result == 6

def test_multiplication():
    result = 7 * 3
    assert result == 21

def test_division():
    result = 8 / 2
    assert result == 4.0

def test_string_concatenation():
    result = "Hello" + " " + "World"
    assert result == "Hello World"

def test_string_length():
    text = "Python"
    assert len(text) == 6

def test_substring_presence():
    text = "Pytest is fun"
    assert "fun" in text

def test_list_length():
    lst = [1, 2, 3, 4]
    assert len(lst) == 4

def test_list_contains_element():
    lst = [10, 20, 30, 40]
    assert 20 in lst

def test_dict_key_presence():
    dictionary = {"name": "John", "age": 25}
    assert "name" in dictionary

def test_boolean_value():
    value = 5 > 3
    assert value is True

def test_negative_number():
    number = -10
    assert number < 0

def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        result = 1 / 0