# 代码生成时间: 2025-09-15 12:30:09
import pandas as pd
from cryptography.fernet import Fernet

"""
密码加密解密工具
"""

# 密钥生成
def generate_key():
    key = Fernet.generate_key()
    return key

# 加密密码
def encrypt_password(password, key):
    try:
        f = Fernet(key)
        encrypted_password = f.encrypt(password.encode())
        return encrypted_password
    except Exception as e:
        print(f"加密错误: {e}")

# 解密密码
def decrypt_password(encrypted_password, key):
    try:
        f = Fernet(key)
        decrypted_password = f.decrypt(encrypted_password)
        return decrypted_password.decode()
    except Exception as e:
        print(f"解密错误: {e}")

# 主函数
def main():
    # 用户输入
    raw_password = input("请输入密码: ")
    key = generate_key()
    print(f"生成的密钥: {key.decode()}")

    # 加密
    encrypted = encrypt_password(raw_password, key)
    print(f"加密后的密码: {encrypted}")

    # 解密
    decrypted = decrypt_password(encrypted, key)
    print(f"解密后的密码: {decrypted}")

if __name__ == '__main__':
    main()