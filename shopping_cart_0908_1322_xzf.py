# 代码生成时间: 2025-09-08 13:22:31
import pandas as pd

"""
Shopping Cart class implementation using Python and pandas framework.
This class allows users to add items to a shopping cart, remove items,
and calculate the total cost of items in the cart.
"""
class ShoppingCart:
    def __init__(self):
        # Initialize an empty DataFrame to store items in the shopping cart
        self.cart = pd.DataFrame(columns=['item_id', 'item_name', 'quantity', 'price_per_unit'])

    def add_item(self, item_id, item_name, quantity, price_per_unit):
        """Add an item to the shopping cart."""
        try:
            # Check if the item already exists in the cart
            if self.cart.loc[self.cart['item_id'] == item_id, 'quantity'].any():
                # If the item exists, increment the quantity
                self.cart.loc[self.cart['item_id'] == item_id, 'quantity'] += quantity
            else:
                # If the item does not exist, add it to the cart
                self.cart = pd.concat([self.cart,
                                    pd.DataFrame({'item_id': [item_id],
                                                'item_name': [item_name],
                                                'quantity': [quantity],
                                                'price_per_unit': [price_per_unit]})],
                                    ignore_index=True)
        except Exception as e:
            print(f"Error adding item to cart: {e}")

    def remove_item(self, item_id, quantity):
        """Remove items from the shopping cart."""
        try:
            # Check if the item exists in the cart
            if self.cart.loc[self.cart['item_id'] == item_id, 'quantity'].any():
                # If the item exists, decrement the quantity or remove the item
                if self.cart.loc[self.cart['item_id'] == item_id, 'quantity'].iloc[0] <= quantity:
                    self.cart = self.cart[self.cart['item_id'] != item_id]
                else:
                    self.cart.loc[self.cart['item_id'] == item_id, 'quantity'] -= quantity
            else:
                print("Item not found in the cart.")
        except Exception as e:
            print(f"Error removing item from cart: {e}")

    def calculate_total(self):
        """Calculate the total cost of items in the cart."""
        try:
            # Calculate the total cost by multiplying quantity and price per unit
            total_cost = (self.cart['quantity'] * self.cart['price_per_unit']).sum()
            return total_cost
        except Exception as e:
            print(f"Error calculating total cost: {e}")
            return None

    def display_cart(self):
        """Display the contents of the shopping cart."""
        try:
            print(self.cart)
        except Exception as e:
            print(f"Error displaying cart: {e}")

# Example usage
if __name__ == '__main__':
    cart = ShoppingCart()
    cart.add_item('item1', 'Apple', 2, 0.50)
    cart.add_item('item2', 'Banana', 3, 0.20)
    cart.add_item('item3', 'Cherry', 1, 1.00)
    cart.display_cart()
    total = cart.calculate_total()
    print(f"Total cost: {total}")
    cart.remove_item('item2', 1)
    cart.display_cart()
    total = cart.calculate_total()
    print(f"Total cost after removing item: {total}")
