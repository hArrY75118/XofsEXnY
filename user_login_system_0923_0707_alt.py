# 代码生成时间: 2025-09-23 07:07:59
import pandas as pd
from getpass import getpass

"""用户登录验证系统"""

# 假设有一个用户信息的CSV文件，包含用户名和密码
USER_DATA_FILE = 'users.csv'

def load_user_data(file_path):
    """从CSV文件加载用户数据"""
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
        return None
    except pd.errors.EmptyDataError:
        print(f"Error: The file {file_path} is empty.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

def authenticate_user(user_data, username, password):
    """验证用户凭证"""
    try:
        user = user_data[user_data['username'] == username]
        if not user.empty and user['password'].values[0] == password:
            return True
        else:
            return False
    except Exception as e:
        print(f"An error occurred during authentication: {e}")
        return False

def main():
    """主函数，处理用户登录"""
    user_data = load_user_data(USER_DATA_FILE)
    if user_data is None:
        return

    username = input("Enter your username: ")
    password = getpass("Enter your password: ")

    if authenticate_user(user_data, username, password):
        print("Login successful!")
    else:
        print("Invalid username or password.")

if __name__ == '__main__':
    main()