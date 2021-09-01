"""Simple class used for exploring / understanding CI piplines"""

class ArithmeticFunctions:
    """Demonstrator class whose methods perform some simple arithmetic functions.
    Minimal code with no error checking or handling.
    """

    def __init__(self, first_num, second_num):
        """Constructor for the class. Encapsulates the values to be operated on.

        Parameters:
            first_num (int or float): the first number that the methods are applied to
            second_num (int or float): the second number that the methods are applied to
        """
        self.first_num = first_num
        self.second_num = second_num

    def sum_ints(self):
        """A sample function to sum two integers.

        Returns:
            int, sum of the two integers
        """
        return self.first_num + self.second_num

    def multiply_ints(self):
        """A sample function to multiply two integers.

        Returns:
            int, the product of the two integers
        """
        return self.first_num * self.second_num


def main():
    """Driver function for ArithmeticFunctions class"""
    a_f = ArithmeticFunctions(2,3)
    print(f"Sum: {a_f.sum_ints()}")
    print(f"Product: {a_f.multiply_ints()}")

if __name__ == "__main__":
    main()
