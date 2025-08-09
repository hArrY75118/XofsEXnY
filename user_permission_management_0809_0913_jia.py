# 代码生成时间: 2025-08-09 09:13:09
import pandas as pd

# 用户权限管理系统
class UserPermissionManager:
    def __init__(self):
        # 初始化权限数据
        self.permissions = pd.DataFrame(columns=['user_id', 'permission'])

    def add_user_permission(self, user_id, permission):
        """ 添加用户权限
        
        :param user_id: 用户ID
        :param permission: 用户权限
        """
        # 检查权限是否已经存在
        if self.check_permission(user_id, permission):
            print(f"Permission '{permission}' already exists for user {user_id}.")
        else:
            new_permission = {'user_id': user_id, 'permission': permission}
            self.permissions = self.permissions.append(new_permission, ignore_index=True)
            print(f"Permission '{permission}' added for user {user_id}.")

    def remove_user_permission(self, user_id, permission):
        """ 移除用户权限
        
        :param user_id: 用户ID
        :param permission: 用户权限
        """
        # 检查权限是否存在
        if self.check_permission(user_id, permission):
            self.permissions = self.permissions[self.permissions['permission'] != permission]
            print(f"Permission '{permission}' removed for user {user_id}.")
        else:
            print(f"Permission '{permission}' does not exist for user {user_id}.")

    def check_permission(self, user_id, permission):
        """ 检查用户是否具有特定权限
        
        :param user_id: 用户ID
        :param permission: 用户权限
        :return: 布尔值，表示权限是否存在
        """
        return not self.permissions[(self.permissions['user_id'] == user_id) & (self.permissions['permission'] == permission)].empty

    def list_permissions(self, user_id=None):
        """ 列出用户的所有权限
        
        :param user_id: 用户ID，如果为None，则列出所有用户的权限
        :return: 权限列表
        """
        if user_id:
            return self.permissions[self.permissions['user_id'] == user_id]
        return self.permissions

# 示例用法
if __name__ == '__main__':
    manager = UserPermissionManager()
    
    # 添加权限
    manager.add_user_permission('user1', 'read')
    manager.add_user_permission('user1', 'write')
    manager.add_user_permission('user2', 'read')
    
    # 移除权限
    manager.remove_user_permission('user1', 'read')
    
    # 检查权限
    if manager.check_permission('user1', 'write'):
        print("User1 has write permission.")
    
    # 列出权限
    permissions = manager.list_permissions('user1')
    print("Permissions for user1:", permissions)
    print("All permissions:", manager.list_permissions())
