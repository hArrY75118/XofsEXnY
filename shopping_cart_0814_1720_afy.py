# 代码生成时间: 2025-08-14 17:20:23
import pandas as pd

"""
购物车功能实现
"""

class ShoppingCart:
    def __init__(self):
        # 初始化空购物车
        self.cart = pd.DataFrame(columns=['item_id', 'item_name', 'quantity', 'price'])

    def add_item(self, item_id, item_name, quantity, price):
        """
        向购物车添加商品
        :param item_id: 商品ID
        :param item_name: 商品名称
        :param quantity: 商品数量
        :param price: 商品价格
        """
        try:
            # 检查商品数量和价格是否为正数
            if quantity <= 0 or price <= 0:
                raise ValueError('商品数量和价格必须为正数')

            # 将商品添加到购物车
            self.cart = self.cart.append({'item_id': item_id, 'item_name': item_name, 'quantity': quantity, 'price': price}, ignore_index=True)
        except Exception as e:
            print(f'添加商品失败：{e}')

    def remove_item(self, item_id):
        """
        从购物车移除商品
        :param item_id: 商品ID
        """
        try:
            # 查找购物车中的商品
            items = self.cart[self.cart['item_id'] == item_id]
            if items.empty:
                raise ValueError('商品不存在')

            # 从购物车移除商品
            self.cart = self.cart.drop(items.index)
        except Exception as e:
            print(f'移除商品失败：{e}')

    def update_item_quantity(self, item_id, quantity):
        """
        更新购物车中商品的数量
        :param item_id: 商品ID
        :param quantity: 新的商品数量
        """
        try:
            # 检查商品数量是否为正数
            if quantity <= 0:
                raise ValueError('商品数量必须为正数')

            # 查找购物车中的商品
            items = self.cart[self.cart['item_id'] == item_id]
            if items.empty:
                raise ValueError('商品不存在')

            # 更新商品数量
            self.cart.loc[items.index, 'quantity'] = quantity
        except Exception as e:
            print(f'更新商品数量失败：{e}')

    def calculate_total_price(self):
        """
        计算购物车中商品的总价格
        :return: 总价格
        """
        try:
            # 计算总价格
            total_price = self.cart['quantity'] * self.cart['price']
            return total_price.sum()
        except Exception as e:
            print(f'计算总价格失败：{e}')
            return 0

    def show_cart_items(self):
        """
        显示购物车中的商品
        """
        try:
            # 显示购物车中的商品
            print(self.cart)
        except Exception as e:
            print(f'显示购物车商品失败：{e}')

# 示例用法
if __name__ == '__main__':
    cart = ShoppingCart()
    cart.add_item('001', '商品1', 2, 100.0)
    cart.add_item('002', '商品2', 3, 200.0)
    cart.show_cart_items()
    cart.update_item_quantity('001', 4)
    cart.show_cart_items()
    cart.remove_item('002')
    cart.show_cart_items()
    print(f'总价格：{cart.calculate_total_price()}')
