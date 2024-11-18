import pytest

def test_addition_pass():
    result = 2 + 3
    assert result == 5  # Passes

def test_addition_fail():
    result = 2 + 3
    assert result == 6  # Fails

def test_subtraction_pass():
    result = 10 - 4
    assert result == 6  # Passes

def test_subtraction_fail():
    result = 10 - 4
    assert result == 5  # Fails

def test_multiplication_pass():
    result = 7 * 3
    assert result == 21  # Passes

def test_multiplication_fail():
    result = 7 * 3
    assert result == 20  # Fails

def test_division_pass():
    result = 8 / 2
    assert result == 4.0  # Passes

def test_division_fail():
    result = 8 / 2
    assert result == 5.0  # Fails

def test_string_concatenation_pass():
    result = "Hello" + " " + "World"
    assert result == "Hello World"  # Passes

def test_string_concatenation_fail():
    result = "Hello" + " " + "World"
    assert result == "HelloWorld"  # Fails

def test_list_contains_element_pass():
    lst = [10, 20, 30, 40]
    assert 20 in lst  # Passes

def test_list_contains_element_fail():
    lst = [10, 20, 30, 40]
    assert 50 in lst  # Fails

def test_dict_key_presence_pass():
    dictionary = {"name": "John", "age": 25}
    assert "name" in dictionary  # Passes

def test_dict_key_presence_fail():
    dictionary = {"name": "John", "age": 25}
    assert "address" in dictionary  # Fails