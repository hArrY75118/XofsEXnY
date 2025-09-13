# 代码生成时间: 2025-09-13 14:46:09
import pandas as pd
import re
from datetime import datetime

"""
日志文件解析工具
该工具用于解析具有特定格式的日志文件，并提取相关信息。
日志文件的每一行应包含日期、时间、日志级别和消息。
例如：2023-03-01 12:00:00 INFO Some log message
"""


class LogParser:
    def __init__(self, log_file_path: str):
        """
        日志解析器初始化函数
        :param log_file_path: 日志文件的路径
        """
        self.log_file_path = log_file_path
        self.pattern = r'^(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) (\w+) (.*)$'
        self.data = []

    def parse_log(self) -> pd.DataFrame:
        """
        解析日志文件并返回Pandas DataFrame
        """
        try:
            # 打开日志文件并逐行读取
            with open(self.log_file_path, 'r') as file:
                for line in file:
                    # 使用正则表达式匹配日志行
                    match = re.match(self.pattern, line)
                    if match:
                        # 提取日期、时间、日志级别和消息
                        date, time, level, message = match.groups()
                        # 将提取的信息添加到数据列表
                        self.data.append({
                            'Date': date,
                            'Time': time,
                            'Level': level,
                            'Message': message.strip()
                        })
        except FileNotFoundError:
            print(f"Error: 文件 {self.log_file_path} 未找到。")
        except Exception as e:
            print(f"Error: 发生未知错误：{e}")

        # 将数据列表转换为Pandas DataFrame
        df = pd.DataFrame(self.data)
        return df

    def save_to_csv(self, output_file_path: str) -> None:
        """
        将解析后的日志数据保存为CSV文件
        :param output_file_path: 输出CSV文件的路径
        """
        df = self.parse_log()
        df.to_csv(output_file_path, index=False)
        print(f"日志数据已保存到 {output_file_path}。")

# 示例用法
if __name__ == '__main__':
    log_parser = LogParser('log.txt')
    log_parser.save_to_csv('log_parsed.csv')
