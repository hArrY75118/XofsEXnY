# 代码生成时间: 2025-09-03 13:48:45
import pandas as pd\
\
# 购物车类\
class ShoppingCart:\
    """购物车类用于管理用户购物车中的商品。"""\
    def __init__(self):\
        """初始化购物车，创建空的DataFrame用于存储商品。"""\
        self.cart = pd.DataFrame(columns=["product_id", "product_name", "quantity", "price"])\
\
    def add_product(self, product_id, product_name, quantity, price):\
        """向购物车中添加商品。"""\
        if quantity <= 0 or price <= 0:\
            raise ValueError("Quantity and price must be positive.")\
# 改进用户体验
        new_product = {"product_id": product_id, "product_name": product_name, "quantity": quantity, "price": price}\
        self.cart = pd.concat([self.cart, pd.DataFrame([new_product])], ignore_index=True)\
\
# 改进用户体验
    def remove_product(self, product_id):\
        """从购物车中移除商品。"""\
        if product_id not in self.cart['product_id'].values:\
            raise ValueError("Product not found in cart.")\
        self.cart = self.cart[self.cart['product_id'] != product_id]\
\
    def update_quantity(self, product_id, quantity):\
        """更新购物车中商品的数量。"""\
        if quantity <= 0:\
            raise ValueError("Quantity must be positive.")\
        if product_id not in self.cart['product_id'].values:\
            raise ValueError("Product not found in cart.")\
        self.cart.loc[self.cart['product_id'] == product_id, 'quantity'] = quantity\
\
    def get_cart_summary(self):\
        "