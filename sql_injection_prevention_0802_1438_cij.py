# 代码生成时间: 2025-08-02 14:38:10
import pandas as pd
from sqlalchemy import create_engine, text

# 定义一个函数来执行安全的数据库查询，防止SQL注入
def safe_query(connection_string, query, params=None):
    """
    安全执行SQL查询，防止SQL注入。

    参数:
    connection_string (str): 数据库连接字符串。
    query (str): SQL查询字符串。
    params (dict): 用于参数化查询的参数字典。

    返回值:
    pd.DataFrame: 包含查询结果的Pandas DataFrame。
    """
    try:
        # 创建数据库引擎
        engine = create_engine(connection_string)

        # 使用参数化查询
        with engine.connect() as conn:
            if params:
                result = pd.read_sql_query(text(query), conn, params=params)
            else:
                result = pd.read_sql_query(text(query), conn)

        return result
    except Exception as e:
        # 打印并返回错误信息
        print(f"An error occurred: {e}")
        return None

# 示例用法
if __name__ == "__main__":
    # 数据库连接字符串
    connection_string = "postgresql://username:password@host:port/dbname"

    # 示例SQL查询，使用参数化防止SQL注入
    query = "SELECT * FROM users WHERE username = :username AND password = :password"
    params = {"username": "example_user", "password": "example_pass"}

    # 安全执行查询
    result = safe_query(connection_string, query, params)

    # 打印结果
    if result is not None:
        print(result)