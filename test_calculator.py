import pytest
from calculator import Calculator


@pytest.fixture
def calc():
    return Calculator()


# --- Addition ---

def test_add_two_positives(calc):
    assert calc.add(2, 3) == 5

def test_add_negative(calc):
    assert calc.add(-1, 4) == 3

def test_add_two_negatives(calc):
    assert calc.add(-2, -3) == -5

def test_add_zero(calc):
    assert calc.add(7, 0) == 7


# --- Subtraction ---

def test_subtract_basic(calc):
    assert calc.subtract(10, 4) == 6

def test_subtract_negative_result(calc):
    assert calc.subtract(3, 7) == -4

def test_subtract_negative_number(calc):
    assert calc.subtract(5, -2) == 7

def test_subtract_zero(calc):
    assert calc.subtract(5, 0) == 5

# --- Multiplication ---

def test_multiply_basic(calc):
    assert calc.multiply(4, 5) == 20

def test_multiply_negative(calc):
    assert calc.multiply(-3, 6) == -18

def test_multiply_two_negatives(calc):
    assert calc.multiply(-2, -4) == 8

def test_multiply_by_zero(calc):
    assert calc.multiply(7, 0) == 0

# --- Division ---

def test_divide_basic(calc):
    assert calc.divide(10, 2) == 5

def test_divide_negative(calc):
    assert calc.divide(-12, 4) == -3

def test_divide_two_negatives(calc):
    assert calc.divide(-15, -3) == 5

def test_divide_by_zero(calc):
    with pytest.raises(ValueError, match="Cannot divide by zero, answer is undefined."):
        calc.divide(10, 0)