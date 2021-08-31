class ArithmeticFunctions:

    def __init__(self, first_int: int, second_int: int):
        self.first_int = first_int
        self.second_int = second_int

    def sum_ints(self) -> int:
        """A sample function to sum two integers.
        
        Returns: 
            int, sum of the two integers
        """        
        return self.first_int + self.second_int

    def multiply_ints(self) -> int:
        """A sample function to multiply two integers.
        
        Returns:
            int, the product of the two integers
        """
        return self.first_int * self.second_int


def main():
    af = ArithmeticFunctions(2,3)
    print(f"Sum: {af.sum_ints()}")
    print(f"Product: {af.multiply_ints()}")

if __name__ == "__main__":
    main()