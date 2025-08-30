# 代码生成时间: 2025-08-30 22:56:42
import pandas as pd

"""
API响应格式化工具

该工具用于格式化API响应数据，使其更加易于阅读和处理。
支持将原始响应数据转换成Pandas DataFrame，并提供标准化的输出格式。
"""

class ApiResponseFormatter:
    """API响应格式化类"""

    def __init__(self, response_data):
        """初始化方法

        Args:
            response_data (dict): API响应数据
        """
        self.response_data = response_data

    def to_dataframe(self):
        """将响应数据转换为Pandas DataFrame

        Returns:
            pd.DataFrame: 转换后的DataFrame
        """
        try:
            # 检查响应数据是否包含必要字段
            if 'data' not in self.response_data:
                raise ValueError("响应数据缺少'data'字段")

            # 将响应数据转换为DataFrame
            df = pd.DataFrame(self.response_data['data'])
            return df
        except Exception as e:
            # 处理转换过程中的异常
            print(f"转换为DataFrame时发生错误：{e}")
            return None

    def format_response(self, output_format='json'):
        """格式化响应数据

        Args:
            output_format (str): 输出格式，默认为'json'

        Returns:
            str: 格式化后的响应数据
        """
        try:
            # 将DataFrame转换为指定格式
            if output_format == 'json':
                df = self.to_dataframe()
                if df is not None:
                    return df.to_json(orient='records')
                else:
                    return ''
            elif output_format == 'csv':
                df = self.to_dataframe()
                if df is not None:
                    return df.to_csv(index=False)
                else:
                    return ''
            else:
                raise ValueError("不支持的输出格式")
        except Exception as e:
            # 处理格式化过程中的异常
            print(f"格式化响应时发生错误：{e}")
            return ''

# 示例用法
if __name__ == '__main__':
    response_data = {
        'status': 'success',
        'data': [
            {'id': 1, 'name': 'John', 'age': 30},
            {'id': 2, 'name': 'Jane', 'age': 25}
        ]
    }

    formatter = ApiResponseFormatter(response_data)
    formatted_json = formatter.format_response('json')
    formatted_csv = formatter.format_response('csv')

    print('格式化后的JSON：')
    print(formatted_json)

    print('
格式化后的CSV：')
    print(formatted_csv)