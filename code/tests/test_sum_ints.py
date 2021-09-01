from arithmetic_functions import ArithmeticFunctions

import pytest
def test_get_correct_positive_sum():
        af = ArithmeticFunctions(2,3)
        assert af.sum_ints() == 5

def test_get_correct_negative_sum():
    af = ArithmeticFunctions(-2,3)
    assert af.sum_ints() == 1

def test_str_input_returns_str():
    af = ArithmeticFunctions("a", "b")
    assert isinstance(af.sum_ints(),  str)

def test_none_raise_error():
    with pytest.raises(TypeError):
        af = ArithmeticFunctions(None, 1)
        af.multiply_ints()

# import unittest
# class TestSumInts(unittest.TestCase): 
#     def test_get_correct_positive_sum(self):
#         af = ArithmeticFunctions(2,3)
#         self.assertEqual(af.sum_ints(), 5)

#     def test_get_correct_negative_sum(self):
#         af = ArithmeticFunctions(-2,3)
#         self.assertEqual(af.sum_ints(), 1)

#     def test_str_raise_error(self):
#         af = ArithmeticFunctions("a", "b")
#         self.assertEqual(type(af.sum_ints()), str)

# if __name__ == "__main__":
#     unittest.main()