# 代码生成时间: 2025-08-26 13:45:10
import os
import pandas as pd
from pathlib import Path

# 定义函数来重命名文件
def rename_files(input_directory, rename_pattern, output_directory):
    """
    批量重命名工具。
# 添加错误处理

    参数:
    input_directory (str): 待重命名文件的目录。
    rename_pattern (str): 文件重命名模式，例如'{index}_{original_name}'。
    output_directory (str): 重命名后文件存放的目录。

    返回:
    None
    """
    # 检查输入目录是否存在
    if not os.path.exists(input_directory):
        raise FileNotFoundError(f"目录 {input_directory} 不存在。")

    # 创建输出目录
    Path(output_directory).mkdir(parents=True, exist_ok=True)

    # 列出所有待重命名的文件
# 扩展功能模块
    files = [f for f in os.listdir(input_directory) if os.path.isfile(os.path.join(input_directory, f))]

    # 记录重命名后文件的位置
    renamed_files = []

    # 遍历文件并重命名
    for index, file in enumerate(files, start=1):
        # 构建新的文件名
        original_file_path = os.path.join(input_directory, file)
        new_file_name = rename_pattern.format(index=index, original_name=file)
        new_file_path = os.path.join(output_directory, new_file_name)

        # 重命名文件
        try:
            os.rename(original_file_path, new_file_path)
            renamed_files.append(new_file_path)
        except Exception as e:
            print(f"重命名文件 {file} 时发生错误: {e}")

    # 返回重命名后的文件列表
    return renamed_files

# 以下代码为测试代码，不在函数中
if __name__ == '__main__':
    input_dir = 'path/to/input/directory'
# 优化算法效率
    output_dir = 'path/to/output/directory'
    pattern = '{index}_{original_name}'

    # 调用重命名函数
    renamed = rename_files(input_dir, pattern, output_dir)
    print('重命名完成。')
    print('重命名后的文件列表:', renamed)