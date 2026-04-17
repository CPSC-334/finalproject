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

# --- Square ---
def test_square_basic(calc):
    assert calc.square(4) == 16

def test_square_negative(calc):
    assert calc.square(-3) == 9

# --- Power ---

def test_power_basic(calc):
    assert calc.power(2, 3) == 8

def test_power_zero_exponent(calc):
    assert calc.power(5, 0) == 1

def test_power_negative_base(calc):
    assert calc.power(-2, 3) == -8

# --- Square Root ---

def test_square_root_basic(calc):
    assert calc.square_root(16) == 4

def test_square_root_zero(calc):
    assert calc.square_root(0) == 0

def test_square_root_negative(calc):
    with pytest.raises(ValueError, match="Cannot take the square root of a negative number."):
        calc.square_root(-4)

# --- Root ---

def test_root_basic(calc):
    assert calc.root(27, 3) == 3

def test_root_even_root_of_negative(calc):
    with pytest.raises(ValueError, match="Cannot take an even root of a negative number."):
        calc.root(-8, 2)

def test_root_odd_root_of_negative(calc):
    assert calc.root(-8, 3) == -2


# --- Logarithm ---
def test_logarithm_basic(calc):
    assert calc.logarithm(100, 10) == 2

def test_logarithm_zero_or_negative(calc):
    with pytest.raises(ValueError, match="Logarithm is undefined for non-positive numbers."):
        calc.logarithm(0, 10)

def test_logarithm_invalid_base(calc):
    with pytest.raises(ValueError, match="Logarithm base must be greater than 1."):
        calc.logarithm(100, 1)

