# 代码生成时间: 2025-09-19 07:10:03
import pandas as pd

"""
表单数据验证器

该程序用于验证表单数据的有效性。
使用Pandas框架，对表单数据进行验证。
"""

class FormValidator:
    """
    表单数据验证器类
    """
    def __init__(self, data):
        """
        初始化验证器
        :param data: 表单数据，Pandas DataFrame格式
        """
        self.data = data

    def validate(self):
        """
        验证表单数据
        :return: 验证结果，True表示验证通过，False表示验证失败
        """
        try:
            # 检查数据是否为空
            if self.data.empty:
                raise ValueError("数据为空")

            # 验证字段是否存在
            required_fields = ["name", "email", "age"]
            if not all(field in self.data.columns for field in required_fields):
                raise ValueError("缺少必需字段")

            # 验证字段类型
            self._validate_field_types()

            # 验证字段值
            self._validate_field_values()

            return True
        except Exception as e:
            print(f"验证失败: {e}")
            return False

    def _validate_field_types(self):
        """
        验证字段类型
        """
        type_mapping = {
            "name": str,
            "email": str,
            "age": int,
        }

        for field, field_type in type_mapping.items():
            if not all(isinstance(value, field_type) for value in self.data[field]):
                raise ValueError(f"字段 {field} 类型不正确")

    def _validate_field_values(self):
        """
        验证字段值
        """
        # 验证年龄是否在合理范围内
        if (self.data["age"] < 0).any() or (self.data["age"] > 100).any():
            raise ValueError("年龄不在合理范围内")

        # 验证邮箱格式是否正确
        import re
        email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        if not all(re.match(email_pattern, email) for email in self.data["email"]):
            raise ValueError("邮箱格式不正确")

# 示例用法
if __name__ == "__main__":
    # 创建示例数据
    data = pd.DataFrame({
        "name": ["John", "Jane"],
        "email": ["john@example.com", "jane@example.com"],
        "age": [25, 30]
    })

    # 创建验证器实例
    validator = FormValidator(data)

    # 验证数据
    if validator.validate():
        print("数据验证通过")
    else:
        print("数据验证失败")
        