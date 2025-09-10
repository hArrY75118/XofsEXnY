# 代码生成时间: 2025-09-10 12:03:06
import pandas as pd
import os
import glob

"""
CSV文件批量处理器

这个程序可以处理指定目录下所有的CSV文件，并将处理结果存储到一个新的文件中。
"""

def process_csv_files(directory: str, output_file: str):
    """
    处理指定目录下的所有CSV文件并将结果存储到一个输出文件中。

    参数:
    directory: str - 包含CSV文件的目录路径
    output_file: str - 输出文件的路径
    """
    # 初始化一个空的DataFrame用于存储所有CSV文件的数据
    aggregated_data = pd.DataFrame()

    # 遍历指定目录下的所有CSV文件
    for file_path in glob.glob(os.path.join(directory, '*.csv')):
        try:
            # 读取CSV文件
            data = pd.read_csv(file_path)
            # 将读取的数据添加到聚合DataFrame中
            aggregated_data = pd.concat([aggregated_data, data], ignore_index=True)
        except Exception as e:
            # 处理可能的读取或合并错误
            print(f"Error processing file {file_path}: {e}")

    # 将聚合后的数据存储到输出文件中
    try:
        aggregated_data.to_csv(output_file, index=False)
        print(f"Processed data successfully written to {output_file}")
    except Exception as e:
        print(f"Error writing to output file {output_file}: {e}")

# 示例用法
if __name__ == '__main__':
    directory_path = 'path/to/csv/files'  # 替换为你的CSV文件目录路径
    output_file_path = 'path/to/output/file.csv'  # 替换为你的输出文件路径
    process_csv_files(directory_path, output_file_path)