# 代码生成时间: 2025-08-27 03:02:48
import pandas as pd
from typing import List, Dict
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

"""
消息通知系统
"""

class MessageNotificationSystem:
    def __init__(self, email_config: Dict):
        """
        初始化邮件配置
        :param email_config: 邮件服务器配置
        """
        self.email_config = email_config

    def send_email(self, recipient: str, subject: str, message: str) -> bool:
        """
        发送邮件
        :param recipient: 收件人邮箱
        :param subject: 邮件主题
        :param message: 邮件内容
        :return: 发送成功返回True，否则返回False
        """
        try:
            # 创建邮件对象
            msg = MIMEMultipart()
            msg['From'] = self.email_config['from_email']
            msg['To'] = recipient
            msg['Subject'] = subject
            msg.attach(MIMEText(message, 'plain'))

            # 发送邮件
            with smtplib.SMTP(self.email_config['host'], self.email_config['port']) as server:
                server.starttls()
                server.login(self.email_config['username'], self.email_config['password'])
                server.sendmail(self.email_config['from_email'], recipient, msg.as_string())
                return True
        except Exception as e:
            print(f"Error sending email: {e}")
            return False

    def notify_users(self, users: List[Dict], subject: str, message: str) -> None:
        """
        通知多个用户
        :param users: 用户列表，每个用户包含邮箱信息
        :param subject: 邮件主题
        :param message: 邮件内容
        """
        for user in users:
            self.send_email(user['email'], subject, message)

# 示例用法
if __name__ == '__main__':
    email_config = {
        'host': 'smtp.example.com',
        'port': 587,
        'from_email': 'your_email@example.com',
        'username': 'your_email@example.com',
        'password': 'your_password'
    }
    notification_system = MessageNotificationSystem(email_config)

    users = [
        {'email': 'user1@example.com'},
        {'email': 'user2@example.com'}
    ]
    subject = "Test Notification"
    message = "This is a test notification message."

    notification_system.notify_users(users, subject, message)