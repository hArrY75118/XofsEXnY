# 代码生成时间: 2025-09-03 05:08:16
import pandas as pd
import numpy as np

"""
Random Number Generator using Python and Pandas"""


class RandomNumberGenerator:
    """
    A class to generate random numbers using Python and Pandas.
    
    Attributes:
    - lower (int): The lower limit of the random number range (inclusive).
    - upper (int): The upper limit of the random number range (exclusive).
    - size (int): The number of random numbers to generate.
    """
    def __init__(self, lower, upper, size):
        self.lower = lower
        self.upper = upper
        self.size = size
        
        if self.lower >= self.upper:
            raise ValueError("Lower limit must be less than upper limit.")
        if self.size <= 0:
            raise ValueError("Size must be a positive integer.")

    def generate(self):
        """
        Generate random numbers within the specified range.
        
        Returns:
        - pd.DataFrame: A DataFrame containing the generated random numbers.
        """
        try:
            # Generate random numbers using NumPy
            random_numbers = np.random.randint(self.lower, self.upper, self.size)
            
            # Create a DataFrame to store the random numbers
            random_numbers_df = pd.DataFrame(random_numbers, columns=['Random Numbers'])
            
            return random_numbers_df
        except Exception as e:
            # Handle any unexpected errors
            print(f"An error occurred: {e}")
            return None


# Example usage
if __name__ == '__main__':
    lower_limit = 1
    upper_limit = 100
    number_of_numbers = 10
    
    generator = RandomNumberGenerator(lower_limit, upper_limit, number_of_numbers)
    random_numbers_df = generator.generate()
    
    if random_numbers_df is not None:
        print(random_numbers_df)