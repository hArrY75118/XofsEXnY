# 代码生成时间: 2025-09-08 04:17:59
import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

"""
Test Data Generator
Generates synthetic data for testing purposes.

Attributes:
    - None

Methods:
    - generate_users: Generates a DataFrame with user data.
    - generate_orders: Generates a DataFrame with order data.
"""

class TestDataGenerator:
    def __init__(self):
        # Initialize any necessary variables or settings.
        pass

    def generate_users(self, num_users=100):
        """
        Generates a DataFrame with user data.

        Args:
            num_users (int): The number of users to generate. Defaults to 100.

        Returns:
            pd.DataFrame: A DataFrame containing the generated user data.
        """
        # Define the columns for the user DataFrame.
        user_columns = ['user_id', 'username', 'email', 'signup_date']

        # Generate the user data.
        users = pd.DataFrame({
            'user_id': range(1, num_users + 1),
            'username': [f'user{i}' for i in range(1, num_users + 1)],
            'email': [f'user{i}@example.com' for i in range(1, num_users + 1)],
            'signup_date': [datetime.now() - timedelta(days=random.randint(1, 365)) for _ in range(num_users)]
        }, columns=user_columns)

        return users

    def generate_orders(self, num_orders=100, num_users=100):
        """
        Generates a DataFrame with order data.

        Args:
            num_orders (int): The number of orders to generate. Defaults to 100.
            num_users (int): The number of users to reference. Defaults to 100.

        Returns:
            pd.DataFrame: A DataFrame containing the generated order data.
        """
        # Define the columns for the order DataFrame.
        order_columns = ['order_id', 'user_id', 'order_date', 'order_total', 'status']

        # Generate the order data.
        orders = pd.DataFrame({
            'order_id': range(1, num_orders + 1),
            'user_id': np.random.choice(range(1, num_users + 1), num_orders),
            'order_date': [datetime.now() - timedelta(days=random.randint(1, 365)) for _ in range(num_orders)],
            'order_total': np.random.uniform(10.0, 1000.0, num_orders),
            'status': np.random.choice(['pending', 'shipped', 'delivered', 'cancelled'], num_orders)
        }, columns=order_columns)

        return orders

# Example usage:
if __name__ == '__main__':
    generator = TestDataGenerator()
    users_df = generator.generate_users(num_users=50)
    orders_df = generator.generate_orders(num_orders=200, num_users=50)

    print(users_df.head())
    print(orders_df.head())
