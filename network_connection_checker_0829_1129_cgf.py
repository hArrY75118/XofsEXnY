# 代码生成时间: 2025-08-29 11:29:08
import requests
import pandas as pd
import time
from datetime import datetime

"""
网络连接状态检查器
本程序使用requests库检查特定URL的网络连接状态，并使用Pandas将结果保存为CSV文件。
"""

# 定义待检查的URL列表
urls_to_check = [
    "http://www.google.com",
    "http://www.bing.com",
    "http://www.yahoo.com",
]

# 定义网络连接状态检查的函数
def check_network_connection(url):
    """
    检查给定URL的网络连接状态，并返回一个包含URL和状态的字典
    :param url: 待检查的URL
    :return: 一个包含URL和状态的字典
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # 检查HTTP响应状态码
        return {
            'url': url,
            'status_code': response.status_code,
            'status': 'Connected',
            'checked_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
    except requests.RequestException as e:
        # 处理请求异常
        return {
            'url': url,
            'status_code': None,
            'status': 'Disconnected',
            'checked_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'error': str(e)
        }

# 检查每个URL的网络连接状态
results = []
for url in urls_to_check:
    result = check_network_connection(url)
    results.append(result)

# 将结果转换为Pandas DataFrame
df = pd.DataFrame(results)

# 保存结果到CSV文件
df.to_csv('network_connection_status.csv', index=False)

print("网络连接状态检查完成，结果已保存到network_connection_status.csv")