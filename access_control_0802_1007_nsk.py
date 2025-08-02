# 代码生成时间: 2025-08-02 10:07:46
import pandas as pd

"""
访问权限控制模块
提供基于用户名和角色的访问权限控制功能。
"""


# 定义用户和角色数据结构
class User:
    def __init__(self, username, roles):
        self.username = username  # 用户名
        self.roles = roles  # 用户角色列表


# 权限控制类
class AccessControl:
    def __init__(self):
        self.permissions = {
            'read': ['admin', 'user'],
            'write': ['admin'],
            'delete': ['admin']
        }  # 权限和对应角色映射

    def check_access(self, user, action):
        '''
        检查用户是否有执行指定动作的权限。
        
        Args:
            user (User): 用户对象
            action (str): 需要检查的动作（如'read', 'write', 'delete'）
        Returns:
            bool: 是否有权限
        '''
        if action not in self.permissions:
            raise ValueError(f"Invalid action '{action}'")

        roles_with_access = self.permissions[action]
        return any(role in user.roles for role in roles_with_access)


def main():
    # 测试数据
    users = [
        User('alice', ['user']),
        User('bob', ['admin']),
        User('charlie', ['admin', 'user'])
    ]

    # 权限控制实例
    access_control = AccessControl()

    # 测试权限控制
    for user in users:
        try:
            if access_control.check_access(user, 'read'):
                print(f"{user.username} has read access.")
            else:
                print(f"{user.username} does not have read access.")
        except ValueError as e:
            print(e)

if __name__ == '__main__':
    main()