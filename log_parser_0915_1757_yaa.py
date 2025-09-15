# 代码生成时间: 2025-09-15 17:57:38
import pandas as pd
import re
import logging

# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class LogParser:
    """
    日志文件解析工具类
    """

    def __init__(self, log_file_path):
        """
        初始化方法
        :param log_file_path: 日志文件路径
        """
        self.log_file_path = log_file_path
        self.log_pattern = r'\[(.*?)\] (.*)'  # 假设日志格式为 [时间戳] 信息

    def parse_log_file(self):
        """
        解析日志文件
        :return: pandas DataFrame
        """
        try:
            with open(self.log_file_path, 'r') as file:
                logs = file.readlines()
            # 使用正则表达式解析日志行
            df = self._parse_logs(logs)
            return df
        except FileNotFoundError:
            logging.error(f'文件 {self.log_file_path} 不存在')
            return None
        except Exception as e:
            logging.error(f'解析日志文件时出现错误: {e}')
            return None

    def _parse_logs(self, logs):
        """
        使用正则表达式解析日志行
        :param logs: 日志行列表
        :return: pandas DataFrame
        """
        columns = ['timestamp', 'message']
        data = []
        for log in logs:
            match = re.match(self.log_pattern, log)
            if match:
                data.append(match.groups())
        df = pd.DataFrame(data, columns=columns)
        return df

    def save_parsed_log(self, df, output_file):
        """
        保存解析后的日志到文件
        :param df: pandas DataFrame
        :param output_file: 输出文件路径
        """
        if df is not None:
            try:
                df.to_csv(output_file, index=False)
                logging.info(f'解析后的日志已保存到 {output_file}')
            except Exception as e:
                logging.error(f'保存解析后的日志时出现错误: {e}')
        else:
            logging.error('解析后的日志为空')

# 示例用法
if __name__ == '__main__':
    log_file_path = 'example.log'  # 日志文件路径
    output_file = 'parsed_log.csv'  # 输出文件路径
    
    log_parser = LogParser(log_file_path)
    df = log_parser.parse_log_file()
    if df is not None:
        log_parser.save_parsed_log(df, output_file)