from arithmetic_functions import ArithmeticFunctions

import pytest
def test_get_correct_positive_product():
    af = ArithmeticFunctions(2,3)
    assert af.multiply_ints() == 6

def test_get_correct_negative_sum():
    af = ArithmeticFunctions(-2,3)
    assert af.multiply_ints() == -6

def test_str_raise_error():
    with pytest.raises(TypeError):
        af = ArithmeticFunctions("a", "b")
        af.multiply_ints()

def test_none_raise_error():
    with pytest.raises(TypeError):
        af = ArithmeticFunctions(None, 1)
        af.multiply_ints()

def test_large_inputs_return_inf():
    af = ArithmeticFunctions(2e300,3e300)    
    assert af.multiply_ints() == float("inf")

# import unittest
# class TestSumInts(unittest.TestCase): 
#     def test_get_correct_positive_sum(self):
#         af = ArithmeticFunctions(2,3)
#         self.assertEqual(af.multiply_ints(), 6)

#     def test_get_correct_negative_sum(self):
#         af = ArithmeticFunctions(-2,3)
#         self.assertEqual(af.multiply_ints(), -6)

#     # def test_str_raise_error(self):
#     #     af = ArithmeticFunctions("a", "b")
#     #     self.assertEqual(type(af.sum_ints()), str)

# if __name__ == "__main__":
#     unittest.main()