# 代码生成时间: 2025-09-18 22:42:34
import pandas as pd
from datetime import datetime, timedelta
from apscheduler.schedulers.blocking import BlockingScheduler

# 定义一个定时任务调度器类
class PandasScheduler:
    """
    定时任务调度器，用于调度定期执行的任务。
    """

    def __init__(self, schedule_interval):
        """
        初始化调度器
        :param schedule_interval: 调度间隔（分钟）
        """
        self.scheduler = BlockingScheduler()
        self.schedule_interval = schedule_interval

    def schedule(self, task, interval=None):
        """
        调度任务
        :param task: 要调度的任务函数
        :param interval: 调度间隔（分钟），如果未指定，则使用初始化时的值
        """
        if interval is None:
            interval = self.schedule_interval
        self.scheduler.add_job(task, 'interval', minutes=interval)

    def start(self):
        """
        启动调度器
        """
        try:
            self.scheduler.start()
        except Exception as e:
            print(f"调度器启动失败：{e}")

    def stop(self):
        """
        停止调度器
        """
        self.scheduler.shutdown(wait=False)

# 示例任务函数
def example_task():
    """
    示例任务函数，打印当前时间
    """
    print(f"执行任务：{datetime.now()}")

# 使用示例
if __name__ == '__main__':
    # 创建调度器实例，设置调度间隔为5分钟
    scheduler = PandasScheduler(5)
    
    # 调度一个任务，每天执行一次
    scheduler.schedule(example_task, interval=60)
    
    # 启动调度器
    scheduler.start()