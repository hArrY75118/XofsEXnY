# 代码生成时间: 2025-09-19 18:01:40
import pandas as pd
import matplotlib.pyplot as plt
def load_data(file_path):
    """
    加载数据文件

    参数:
    file_path (str): 文件路径

    返回:
    pd.DataFrame: 数据框架
    """
    try:
        # 尝试加载数据文件
        return pd.read_csv(file_path)
    except FileNotFoundError:
        print("文件未找到，请检查文件路径是否正确。")
        return None
def plot_data(df):
    """
    绘制数据图表

    参数:
    df (pd.DataFrame): 数据框架
    """
    if df is None:
        print("数据为空，无法绘制图表。")
        return

    # 获取列名作为x轴和y轴选项
    x_options = df.columns.tolist()
    y_options = df.columns.tolist()

    # 获取用户输入
    x_axis = input("请输入x轴变量名（从以下选项中选择）：" + "\
".join(x_options))
    y_axis = input("请输入y轴变量名（从以下选项中选择）：" + "\
".join(y_options))

    # 检查输入是否有效
    if x_axis not in x_options or y_axis not in y_options:
        print("输入的变量名无效，请重新输入。")
        return

    # 绘制图表
    plt.figure(figsize=(10, 6))
    plt.scatter(df[x_axis], df[y_axis])
    plt.title('Interactive Chart')
    plt.xlabel(x_axis)
    plt.ylabel(y_axis)
    plt.grid(True)
    plt.show()def main():
    "