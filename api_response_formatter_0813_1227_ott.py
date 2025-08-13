# 代码生成时间: 2025-08-13 12:27:11
import pandas as pd

"""
API响应格式化工具
这个工具用于将API响应数据格式化为JSON格式，并提供错误处理功能。
"""

class ApiResponseFormatter:
    """API响应格式化类"""

    def __init__(self, data, status_code):
        """初始化函数

        :param data: API响应数据
        :param status_code: HTTP状态码
        """
        self.data = data
        self.status_code = status_code

    def validate_data(self):
        """验证数据是否有效

        :return: 验证结果
        """
        if not isinstance(self.data, (dict, pd.DataFrame)):
            raise ValueError("数据类型无效，必须是字典或Pandas DataFrame")

    def format_response(self):
        """格式化API响应

        :return: 格式化后的响应数据
        """
        try:
            self.validate_data()
            if isinstance(self.data, pd.DataFrame):
                # 将Pandas DataFrame转换为字典
                formatted_data = self.data.to_dict(orient='records')
            else:
                # 直接返回字典数据
                formatted_data = self.data

            # 构建响应数据
            response_data = {
                "status_code": self.status_code,
                "data": formatted_data
            }

            return response_data
        except Exception as e:
            # 处理异常情况
            return {
                "status_code": 500,
                "error": str(e)
            }

# 示例用法
if __name__ == '__main__':
    # 创建API响应格式化工具实例
    formatter = ApiResponseFormatter({"message": "Hello, World!"}, 200)

    # 格式化API响应
    response = formatter.format_response()

    # 打印格式化后的响应数据
    print(response)