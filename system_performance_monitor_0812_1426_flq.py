# 代码生成时间: 2025-08-12 14:26:46
import psutil
import pandas as pd
import datetime
import time

"""
系统性能监控工具
================

该工具使用psutil库监控系统性能，包括CPU、内存、磁盘和网络使用情况。
结果以Pandas DataFrame的形式返回。
"""


class SystemPerformanceMonitor:
    def __init__(self):
        """初始化监控工具"""
        pass

    def get_cpu_usage(self):
        """获取CPU使用率
        返回: float, CPU使用率百分比"""
        try:
            cpu_usage = psutil.cpu_percent(interval=1)
            return cpu_usage
        except Exception as e:
            print(f"获取CPU使用率失败: {e}")
            return None

    def get_memory_usage(self):
        """获取内存使用情况
        返回: dict, 包括内存总量、已使用量、可用量等"""
        try:
            memory_info = psutil.virtual_memory()
            memory_usage = {
                "total": memory_info.total / (1024 ** 3),  # GB
                "used": memory_info.used / (1024 ** 3),  # GB
                "available": memory_info.available / (1024 ** 3),  # GB
                "percent": memory_info.percent
            }
            return memory_usage
        except Exception as e:
            print(f"获取内存使用情况失败: {e}")
            return None

    def get_disk_usage(self):
        """获取磁盘使用情况
        返回: dict, 包括磁盘总量、已使用量、可用量等"