# 代码生成时间: 2025-10-11 19:41:57
import pandas as pd
from datetime import datetime
import json

"""
考勤打卡系统
"""

# 考勤记录数据结构
class AttendanceRecord:
    def __init__(self, employee_id, timestamp):
        self.employee_id = employee_id  # 员工ID
        self.timestamp = timestamp      # 打卡时间戳

# 考勤打卡系统
class AttendanceSystem:
    def __init__(self):
        self.records = []  # 存储考勤记录的列表

    def clock_in(self, employee_id):
        """员工打卡"""
        try:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 获取当前时间
            record = AttendanceRecord(employee_id, timestamp)
            self.records.append(record)
            print(f"员工 {employee_id} 打卡成功，时间：{timestamp}")
        except Exception as e:
            print(f"打卡失败：{e}")

    def clock_out(self, employee_id):
        """员工签退"""
        try:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 获取当前时间
            record = AttendanceRecord(employee_id, timestamp)
            self.records.append(record)
            print(f"员工 {employee_id} 签退成功，时间：{timestamp}")
        except Exception as e:
            print(f"签退失败：{e}")

    def get_attendance_records(self):
        """获取所有考勤记录"""
        return self.records

    def save_records_to_csv(self, file_path):
        """保存考勤记录到CSV文件"""
        try:
            df = pd.DataFrame([(record.employee_id, record.timestamp) for record in self.records], 
                             columns=['Employee ID', 'Timestamp'])
            df.to_csv(file_path, index=False)
            print(f"考勤记录已保存到 {file_path}")
        except Exception as e:
            print(f"保存考勤记录失败：{e}")

    def load_records_from_csv(self, file_path):
        """从CSV文件加载考勤记录"""
        try:
            df = pd.read_csv(file_path)
            self.records = [AttendanceRecord(row['Employee ID'], row['Timestamp']) for _, row in df.iterrows()]
            print(f"考勤记录已从 {file_path} 加载")
        except Exception as e:
            print(f"加载考勤记录失败：{e}")

# 示例代码
if __name__ == '__main__':
    attendance_system = AttendanceSystem()
    attendance_system.clock_in('E123')
    attendance_system.clock_out('E123')
    records = attendance_system.get_attendance_records()
    print(json.dumps([(record.employee_id, record.timestamp) for record in records], indent=4))
    attendance_system.save_records_to_csv('attendance.csv')
    attendance_system.load_records_from_csv('attendance.csv')
