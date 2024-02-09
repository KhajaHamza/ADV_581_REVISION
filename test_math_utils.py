import pytest
from MathUtils import MathUtils
class TestMathUtils:
    def test_add(self):
        utils = MathUtils()
        assert utils.add(2, 3) == 5
        assert utils.add(-5, 10) == 5

    def test_subtract(self):
        utils = MathUtils()
        assert utils.subtract(10, 5) == 5
        assert utils.subtract(-2, 4) == -6

    def test_multiply(self):
        utils = MathUtils()
        assert utils.multiply(4, 5) == 20
        assert utils.multiply(-3, 6) == -18

    def test_divide(self):
        utils = MathUtils()
        assert utils.divide(10, 2) == 5.0
        assert utils.divide(4, -2) == -2.0
        assert utils.divide(5, 0) == -1.0  # Test for division by zero