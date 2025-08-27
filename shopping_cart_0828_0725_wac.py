# 代码生成时间: 2025-08-28 07:25:31
import pandas as pd

"""
Shopping Cart Implementation using Python and Pandas.

This script is designed to simulate a shopping cart functionality, allowing
users to add and remove items, and to view the contents of their cart.
"""

class ShoppingCart:
    """
    Shopping Cart class to handle cart operations.
    """
    def __init__(self):
        # Initialize the cart with an empty DataFrame
        self.cart = pd.DataFrame(columns=['item_id', 'name', 'quantity', 'price'])

    def add_item(self, item_id, name, quantity, price):
        """
        Add an item to the shopping cart.
        
        Parameters:
        item_id (int): Unique identifier for the item.
        name (str): Name of the item.
        quantity (int): Quantity of the item to add.
        price (float): Price of the item.
        """
        try:
            # Check if the item already exists in the cart
            if self.cart.loc[self.cart['item_id'] == item_id].empty:
                # Add new item to the cart
                self.cart = pd.concat([self.cart, pd.DataFrame({
                    'item_id': [item_id],
                    'name': [name],
                    'quantity': [quantity],
                    'price': [price]
                })], ignore_index=True)
            else:
                # Update quantity if item already exists
                self.cart.loc[self.cart['item_id'] == item_id, 'quantity'] += quantity
        except Exception as e:
            print(f"An error occurred: {e}")

    def remove_item(self, item_id):
        """
        Remove an item from the shopping cart.
        
        Parameters:
        item_id (int): Unique identifier for the item.
        """
        try:
            # Remove item from the cart
            self.cart = self.cart[self.cart['item_id'] != item_id]
        except Exception as e:
            print(f"An error occurred: {e}")

    def view_cart(self):
        """
        View the contents of the shopping cart.
        """
        return self.cart

    def calculate_total(self):
        """
        Calculate the total cost of the items in the shopping cart.
        """
        try:
            total = self.cart['quantity'] * self.cart['price']
            return total.sum()
        except Exception as e:
            print(f"An error occurred: {e}")
            return 0

# Example usage
if __name__ == '__main__':
    cart = ShoppingCart()
    cart.add_item(1, 'Apple', 2, 0.50)
    cart.add_item(2, 'Banana', 3, 0.30)
    cart.add_item(3, 'Cherry', 1, 2.00)
    print(cart.view_cart())
    print(f"Total cost: ${cart.calculate_total():.2f}")
    cart.remove_item(2)
    print(cart.view_cart())
    print(f"Total cost after removal: ${cart.calculate_total():.2f}")
