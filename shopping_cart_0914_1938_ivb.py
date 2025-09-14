# 代码生成时间: 2025-09-14 19:38:23
import pandas as pd

"""
购物车程序，使用Pandas框架实现商品的添加、删除和结算功能。
"""

class ShoppingCart:
    def __init__(self):
        """初始化购物车，创建空的DataFrame用于存放商品信息。"""
        self.cart = pd.DataFrame(columns=['Product', 'Price', 'Quantity'])

    def add_product(self, product, price, quantity):
        """向购物车添加商品。

        参数:
        product (str): 商品名称
        price (float): 商品单价
        quantity (int): 购买数量
        """
        if quantity <= 0:
            raise ValueError("数量必须大于0")
        new_product = {'Product': product, 'Price': price, 'Quantity': quantity}
        self.cart = self.cart.append(new_product, ignore_index=True)

    def remove_product(self, product):
        """从购物车移除商品。

        参数:
        product (str): 要移除的商品名称
        """
        if product in self.cart['Product'].values:
            self.cart = self.cart[self.cart['Product'] != product]
        else:
            raise ValueError("购物车中没有该商品")

    def calculate_total(self):
        """计算购物车中所有商品的总价格。

        返回:
        float: 购物车中商品的总价格
        """
        self.cart['Total'] = self.cart['Price'] * self.cart['Quantity']
        total = self.cart['Total'].sum()
        return total

    def show_cart(self):
        """显示购物车中的所有商品。"""
        print(self.cart)

# 示例用法
if __name__ == '__main__':
    cart = ShoppingCart()
    cart.add_product('Apple', 2.5, 3)
    cart.add_product('Banana', 1.2, 5)
    cart.show_cart()
    print("Total: \${:.2f}".format(cart.calculate_total()))
    cart.remove_product('Banana')
    cart.show_cart()
    print("Total: \${:.2f}".format(cart.calculate_total()))