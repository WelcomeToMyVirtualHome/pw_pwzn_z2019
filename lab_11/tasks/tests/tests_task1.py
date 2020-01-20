import pytest

from lab_11.tasks.tools.calculator import (
    Calculator,
    CalculatorError,
    EmptyMemory,
    NotNumberArgument,
    WrongOperation,
)


test_valid = [
    ("+", 1, 2, 3),
    ("-", 1, 2, -1),
    ("*", 1, 2, 2),
    ("/", 1, 2, 0.5),
]

test_invalid = [
    ("*", 1, "x", NotNumberArgument),
    ("-", "x", 2, NotNumberArgument),
    ("^", 1, 2, WrongOperation),
    ("/", 1, 0, CalculatorError),
    ("/", 1, None, EmptyMemory),
]


@pytest.fixture(scope="function")
def calculator():
    print("\nNew calculator...")
    return Calculator()


@pytest.mark.parametrize("operator,arg1,arg2,expected", test_valid)
def test_run_valid(operator, arg1, arg2, expected, calculator):
    result = calculator.run(operator, arg1, arg2)
    assert result == expected


@pytest.mark.parametrize("operator,arg1,arg2,expected", test_invalid)
def test_run_invalid(operator, arg1, arg2, expected, calculator):
    with pytest.raises(expected):
        calculator.run(operator, arg1, arg2)


def test_memory(calculator):
    calculator.run("+", 1, 2)
    assert calculator._short_memory == 3
    calculator.memorize()
    assert calculator.memory == 3
    calculator.clean_memory()
    with pytest.raises(EmptyMemory):
        calculator.in_memory()
    with pytest.raises(EmptyMemory):
        calculator.memory