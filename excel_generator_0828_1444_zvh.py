# 代码生成时间: 2025-08-28 14:44:00
import pandas as pd

"""
Excel表格自动生成器，使用Pandas框架从给定的字典数据生成Excel文件。
"""

def create_excel(data: dict, filename: str) -> None:
    """
    根据给定的字典数据创建Excel文件。

    参数:
    data (dict): 包含列名和数据的字典。
    filename (str): 要生成的Excel文件名。
    """
    # 检查数据是否是字典
    if not isinstance(data, dict):
        raise ValueError("数据必须是字典类型")

    # 检查文件名是否以.xlsx结尾
    if not filename.endswith(".xlsx"):
        raise ValueError("文件名必须以.xlsx结尾")

    # 将字典转换为DataFrame
    try:
        df = pd.DataFrame(data)
    except Exception as e:
        raise ValueError("数据转换失败: " + str(e))

    # 保存DataFrame到Excel文件
    try:
        df.to_excel(filename, index=False)
        print(f"Excel文件 '{filename}' 生成成功。")
    except Exception as e:
        raise Exception("保存Excel文件失败: 