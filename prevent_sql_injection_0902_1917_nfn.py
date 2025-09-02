# 代码生成时间: 2025-09-02 19:17:31
import pandas as pd
from sqlalchemy import create_engine

# 数据库配置信息，应从环境变量或安全的地方获取
DB_CONFIG = {
    "username": "your_username",
    "password": "your_password",
    "host": "your_host",
    "port": "your_port",
    "database": "your_database"
}

# 创建数据库引擎
engine = create_engine(
    f"mysql+pymysql://{DB_CONFIG['username']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
)

# 函数：防止SQL注入的安全查询
def safe_query(query, params):
    """
    执行一个防止SQL注入的安全查询。
    
    参数:
    query (str): SQL查询语句。
    params (dict): 用于SQL查询的参数字典。
    
    返回:
    pd.DataFrame: 查询结果。
    
    异常:
    Exception: 处理查询过程中出现的任何异常。
    """
    try:
        # 使用pandas的read_sql_query函数执行查询，并传递参数
        return pd.read_sql_query(query, engine, params=params)
    except Exception as e:
        # 打印异常信息，可根据需要进行日志记录
        print(f"An error occurred: {e}")
        raise

# 示例查询
if __name__ == "__main__":
    # 示例SQL查询，使用参数化查询防止SQL注入
    query = "SELECT * FROM users WHERE username = :username"
    params = {"username": "example_user"}
    try:
        # 执行安全查询
        result = safe_query(query, params)
        # 打印查询结果
        print(result)
    except Exception as e:
        # 处理异常
        print(f"Failed to execute query: {e}")