# 代码生成时间: 2025-08-06 09:30:48
import pandas as pd

"""
数据清洗和预处理工具
该工具用于加载数据集，执行数据清洗和预处理操作，并保存处理后的数据
"""

class DataCleaningPreprocessing:
    def __init__(self, file_path: str, encoding: str = 'utf-8', engine: str = 'c'):
        self.file_path = file_path
        self.encoding = encoding
        self.engine = engine
        self.dataframe = None

    def load_data(self):
        """
        加载数据集
        """
        try:
            self.dataframe = pd.read_csv(self.file_path, encoding=self.encoding, engine=self.engine)
        except FileNotFoundError:
            print(f"File {self.file_path} not found.")
        except pd.errors.EmptyDataError:
            print(f"File {self.file_path} is empty.")
        except Exception as e:
            print(f"An error occurred while loading data: {e}")

    def drop_missing_values(self, threshold: int = None, subset: list = None):
        """
        删除缺失值
        :param threshold: 删除缺失值的阈值，如果小于该阈值则删除
        :param subset: 子集列
        """
        if self.dataframe is None:
            print("Data not loaded. Please load data first.")
            return

        if threshold is not None:
            self.dataframe = self.dataframe.dropna(thresh=threshold)
        elif subset is not None:
            self.dataframe = self.dataframe.dropna(subset=subset)
        else:
            self.dataframe = self.dataframe.dropna()

    def fill_missing_values(self, method: str = 'ffill', subset: list = None):
        """
        填充缺失值
        :param method: 填充方法（向前填充、向后填充等）
        :param subset: 子集列
        """
        if self.dataframe is None:
            print("Data not loaded. Please load data first.")
            return

        if subset is not None:
            for column in subset:
                if method == 'ffill':
                    self.dataframe[column] = self.dataframe[column].fillna(method='ffill')
                elif method == 'bfill':
                    self.dataframe[column] = self.dataframe[column].fillna(method='bfill')
                else:
                    print(f"Invalid fill method: {method}")
        else:
            if method == 'ffill':
                self.dataframe = self.dataframe.fillna(method='ffill')
            elif method == 'bfill':
                self.dataframe = self.dataframe.fillna(method='bfill')
            else:
                print(f"Invalid fill method: {method}")

    def drop_duplicates(self, subset: list = None, keep: str = 'first'):
        """
        删除重复值
        :param subset: 子集列
        :param keep: 保留第一个或最后一个重复值
        """
        if self.dataframe is None:
            print("Data not loaded. Please load data first.")
            return

        if subset is not None:
            self.dataframe = self.dataframe.drop_duplicates(subset=subset, keep=keep)
        else:
            self.dataframe = self.dataframe.drop_duplicates(keep=keep)

    def save_data(self, output_file_path: str, index: bool = False):
        """
        保存处理后的数据
        :param output_file_path: 输出文件路径
        :param index: 是否保存索引
        """
        if self.dataframe is None:
            print("Data not loaded. Please load data first.")
            return

        try:
            self.dataframe.to_csv(output_file_path, index=index)
        except Exception as e:
            print(f"An error occurred while saving data: {e}")

# 示例用法
if __name__ == '__main__':
    dc = DataCleaningPreprocessing('data.csv')
    dc.load_data()
    dc.drop_missing_values(threshold=10)
    dc.fill_missing_values(method='ffill')
    dc.drop_duplicates(subset=['column1', 'column2'], keep='first')
    dc.save_data('output.csv')
