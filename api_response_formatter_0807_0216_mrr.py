# 代码生成时间: 2025-08-07 02:16:45
import pandas as pd

"""
API响应格式化工具
用于将API响应数据格式化为Pandas DataFrame，并提供错误处理。
"""


def format_api_response(data, error_message="An error occurred while processing the API response."):
    """
    将API响应数据格式化为Pandas DataFrame。
    
    参数:
    data (dict or list): API响应数据。
    error_message (str): 错误消息，默认为"An error occurred while processing the API response."。
    
    返回:
    pd.DataFrame: 格式化后的DataFrame。
    
    抛出:
    ValueError: 如果输入数据不是字典或列表。
    """
    
    # 检查输入数据类型
    if not isinstance(data, (dict, list)):
        raise ValueError(f"Invalid data type: {type(data)} is not supported.")
    
    # 如果数据是字典，则转换为列表
    if isinstance(data, dict):
        data = [data]
    
    # 将数据转换为Pandas DataFrame
    try:
        df = pd.DataFrame(data)
    except Exception as e:
        # 如果转换失败，则抛出异常
        raise ValueError(error_message) from e
    
    return df


def main():
    """
    主函数，演示API响应格式化工具的使用。
    """
    
    # 示例API响应数据
    api_response = {
        "user": {
            "id": 1,
            "name": "John Doe",
            "email": "john.doe@example.com"
        }
    }
    
    # 格式化API响应数据
    try:
        df = format_api_response(api_response)
        print(df)
    except ValueError as e:
        print(e)
        
    # 示例错误处理
    invalid_response = "Invalid JSON"
    try:
        df = format_api_response(invalid_response)
        print(df)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()