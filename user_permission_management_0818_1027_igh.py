# 代码生成时间: 2025-08-18 10:27:44
import pandas as pd

"""
用户权限管理系统

该系统使用Pandas框架来管理用户的权限。
系统提供添加用户、删除用户、更新用户权限和查询用户权限的功能。
"""

class UserPermissionManagement:
    """用户权限管理系统类"""

    def __init__(self, filename):
        """初始化方法"""
        self.filename = filename
        self.users = pd.DataFrame(columns=['username', 'permissions'])
        self.load_users()

    def load_users(self):
        """从文件加载用户数据"""
        try:
            self.users = pd.read_csv(self.filename)
        except FileNotFoundError:
            print(f"文件{self.filename}不存在，将创建新文件。")
        except Exception as e:
            print(f"加载文件时发生错误：{e}")

    def save_users(self):
        """保存用户数据到文件"""
        try:
            self.users.to_csv(self.filename, index=False)
        except Exception as e:
            print(f"保存文件时发生错误：{e}")

    def add_user(self, username, permissions):
        """添加用户"""
        try:
            self.users = self.users.append({'username': username, 'permissions': permissions}, ignore_index=True)
            self.save_users()
            print(f"用户{username}已添加。")
        except Exception as e:
            print(f"添加用户时发生错误：{e}")

    def delete_user(self, username):
        """删除用户"""
        try:
            self.users = self.users[self.users['username'] != username]
            self.save_users()
            print(f"用户{username}已删除。")
        except Exception as e:
            print(f"删除用户时发生错误：{e}")

    def update_user(self, username, new_permissions):
        """更新用户权限"""
        try:
            self.users.loc[self.users['username'] == username, 'permissions'] = new_permissions
            self.save_users()
            print(f"用户{username}的权限已更新。")
        except Exception as e:
            print(f"更新用户时发生错误：{e}")

    def query_user(self, username):
        """查询用户权限"""
        try:
            user = self.users[self.users['username'] == username]
            if user.empty:
                print(f"用户{username}不存在。")
            else:
                print(f"用户{username}的权限：{user['permissions'].values[0]}")
        except Exception as e:
            print(f"查询用户时发生错误：{e}")


def main():
    """主函数"""
    filename = 'users.csv'
    upm = UserPermissionManagement(filename)

    while True:
        print("
用户权限管理系统")
        print("1. 添加用户")
        print("2. 删除用户")
        print("3. 更新用户权限")
        print("4. 查询用户权限")
        print("5. 退出")
        choice = input("请选择操作：")

        if choice == '1':
            username = input("请输入用户名：")
            permissions = input("请输入权限：")
            upm.add_user(username, permissions)
        elif choice == '2':
            username = input("请输入要删除的用户名：")
            upm.delete_user(username)
        elif choice == '3':
            username = input("请输入要更新权限的用户名：")
            new_permissions = input("请输入新的权限：")
            upm.update_user(username, new_permissions)
        elif choice == '4':
            username = input("请输入要查询的用户名：")
            upm.query_user(username)
        elif choice == '5':
            break
        else:
            print("无效输入，请重新选择。")

if __name__ == '__main__':
    main()