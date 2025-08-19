# 代码生成时间: 2025-08-20 05:59:52
import pandas as pd
import hashlib
from pathlib import Path
import sys

"""
哈希值计算工具

该程序使用PANDAS框架，读取文件列表，计算并显示哈希值。
支持md5, sha1, sha256, sha512等哈希算法。
"""

def file_hash(file_path, algorithm='md5'):
    """
    计算单个文件的哈希值
    
    参数：
        file_path (str): 文件的路径
        algorithm (str): 哈希算法名称，默认为'md5'
    
    返回：
        str: 文件的哈希值
    
    异常：
        FileNotFoundError: 文件不存在时抛出
        ValueError: 不支持的哈希算法时抛出
    """
    if not Path(file_path).exists():
        raise FileNotFoundError(f"文件 {file_path} 不存在")

    try:
        hash_obj = getattr(hashlib, algorithm)()
    except AttributeError:
        raise ValueError(f"不支持的哈希算法：{algorithm}")

    with open(file_path, 'rb') as file:
        while chunk := file.read(8192):
            hash_obj.update(chunk)

    return hash_obj.hexdigest()

def calculate_hash(file_list, algorithm='md5'):
    """
    计算文件列表中所有文件的哈希值，并生成Pandas DataFrame
    
    参数：
        file_list (list): 包含文件路径的列表
        algorithm (str): 哈希算法名称，默认为'md5'
    
    返回：
        pd.DataFrame: 包含文件路径和对应哈希值的DataFrame
    """
    hash_results = []
    for file_path in file_list:
        try:
            hash_value = file_hash(file_path, algorithm)
            hash_results.append((file_path, hash_value))
        except Exception as e:
            hash_results.append((file_path, str(e)))

    return pd.DataFrame(hash_results, columns=['文件路径', '哈希值'])

def main():
    """
    主函数，从命令行参数读取文件列表，计算并显示哈希值
    """
    if len(sys.argv) < 2:
        print("使用方法: python hash_calculator.py [文件路径1] [文件路径2] ... [文件路径n] [Optional: 哈希算法]')
        return

    file_list = sys.argv[1:-1]
    algorithm = sys.argv[-1] if len(sys.argv) > 2 else 'md5'
    try:
        hash_df = calculate_hash(file_list, algorithm)
        print(hash_df)
    except Exception as e:
        print(f"发生错误：{e}")

if __name__ == '__main__':
    main()