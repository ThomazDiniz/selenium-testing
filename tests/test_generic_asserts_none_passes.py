import pytest

def test_addition_fail():
    result = 2 + 3
    assert result == 6  # Fails

def test_subtraction_fail():
    result = 10 - 4
    assert result == 5  # Fails

def test_multiplication_fail():
    result = 7 * 3
    assert result == 20  # Fails

def test_division_by_zero_fail():
    with pytest.raises(ValueError):  # Incorrect exception
        result = 1 / 0
