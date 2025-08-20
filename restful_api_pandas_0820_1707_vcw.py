# 代码生成时间: 2025-08-20 17:07:22
import pandas as pd
from flask import Flask, request, jsonify
from flask_restful import Resource, Api

# 初始化Flask应用和API
app = Flask(__name__)
api = Api(app)

# 定义数据存储
# 在真实应用中，这些数据应该存储在数据库中
DATA = {'users': [{'id': 1, 'name': 'Alice', 'email': 'alice@example.com'},
               {'id': 2, 'name': 'Bob', 'email': 'bob@example.com'}]}

class UserList(Resource):
    """
    GET /users - 返回用户列表
    POST /users - 创建新用户
    """
    def get(self):
        # 返回所有用户的列表
        return jsonify(DATA['users'])

    def post(self):
        # 创建新用户
        user_data = request.get_json()
        if 'name' not in user_data or 'email' not in user_data:
            return {'message': 'Missing name or email'}, 400

        # 验证是否已存在具有相同电子邮件的用户
        for user in DATA['users']:
            if user['email'] == user_data['email']:
                return {'message': 'Email already exists'}, 400

        # 添加新用户
        new_user_id = max(user['id'] for user in DATA['users']) + 1
        DATA['users'].append({'id': new_user_id, 'name': user_data['name'], 'email': user_data['email']})
        return {'id': new_user_id, 'name': user_data['name'], 'email': user_data['email']}, 201

class User(Resource):
    """
    GET /users/<id> - 返回指定ID的用户信息
    PUT /users/<id> - 更新指定ID的用户信息
    DELETE /users/<id> - 删除指定ID的用户
    """
    def get(self, user_id):
        # 返回指定ID的用户信息
        for user in DATA['users']:
            if user['id'] == user_id:
                return jsonify(user)
        return {'message': 'User not found'}, 404

    def put(self, user_id):
        # 更新指定ID的用户信息
        user_data = request.get_json()
        for user in DATA['users']:
            if user['id'] == user_id:
                if 'name' in user_data:
                    user['name'] = user_data['name']
                if 'email' in user_data:
                    user['email'] = user_data['email']
                return jsonify(user)
        return {'message': 'User not found'}, 404

    def delete(self, user_id):
        # 删除指定ID的用户
        global DATA
        DATA['users'] = [user for user in DATA['users'] if user['id'] != user_id]
        return {'message': 'User deleted'}, 200

# 将资源添加到API
api.add_resource(UserList, '/users')
api.add_resource(User, '/users/<int:user_id>')

# 运行Flask应用
if __name__ == '__main__':
    app.run(debug=True)