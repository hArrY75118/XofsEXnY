# 代码生成时间: 2025-10-10 01:49:23
import pandas as pd
import requests
from requests.exceptions import ConnectionError
import time

"""
网络连接状态检查器

这个程序用于检查网络连接状态，能够检测到指定的网址是否能够成功连接。
如果连接成功，程序将返回HTTP响应信息。如果连接失败，程序将记录错误并重试。
"""

class NetworkConnectionChecker:
    def __init__(self, url, max_retries=3, retry_delay=2):
        """
        初始化网络连接检查器
        :param url: 需要检查的URL字符串
        :param max_retries: 最大重试次数
        :param retry_delay: 重试前等待的秒数
        """
        self.url = url
        self.max_retries = max_retries
        self.retry_delay = retry_delay

    def check_connection(self):
        """
        检查网络连接状态
        :return: HTTP响应信息或错误信息
        """
        for attempt in range(self.max_retries + 1):
            try:
                response = requests.get(self.url)
                response.raise_for_status()  # 检查HTTP响应状态码是否为200
                return response.json()  # 返回JSON响应内容
            except ConnectionError as e:
                print(f"连接尝试 {attempt + 1} 失败：{e}")
                time.sleep(self.retry_delay)  # 等待一段时间后重试
            except Exception as e:
                print(f"未知错误：{e}")
                break
        return {"error": f"连接失败，重试 {self.max_retries} 次后放弃"}

    def to_dataframe(self, response):
        """
        将响应数据转换为Pandas DataFrame
        :param response: HTTP响应JSON数据
        :return: Pandas DataFrame对象
        """
        if isinstance(response, dict) and 'error' not in response:
            return pd.DataFrame(response)
        else:
            return pd.DataFrame({})

    def run(self):
        """
        运行网络连接检查器
        :return: Pandas DataFrame对象
        """
        response = self.check_connection()
        return self.to_dataframe(response)

# 示例用法
if __name__ == '__main__':
    url = "http://example.com/api/data"
    checker = NetworkConnectionChecker(url)
    df = checker.run()
    print(df)