# 代码生成时间: 2025-10-09 17:48:48
import pandas as pd
from typing import Dict, Any, Callable

# 定义工作流任务接口
class WorkflowTask:
    def execute(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        执行工作流任务
        :param data: 输入数据
        :return: 处理后的数据
        """
        raise NotImplementedError("子类必须实现execute方法")

# 定义工作流引擎
class WorkflowEngine:
    def __init__(self):
        """
        初始化工作流引擎
        """
        self.tasks: Dict[str, WorkflowTask] = {}

    def add_task(self, task_name: str, task: WorkflowTask) -> None:
        """
        添加工作流任务
        :param task_name: 任务名称
        :param task: 任务对象
        """
        if task_name in self.tasks:
            raise ValueError(f"任务 {task_name} 已存在")
        self.tasks[task_name] = task

    def run_workflow(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        运行工作流
        :param data: 初始数据
        :return: 最终结果数据
        """
        current_data = data
        for task_name, task in self.tasks.items():
            try:
                current_data = task.execute(current_data)
            except Exception as e:
                print(f"执行任务 {task_name} 出错: {str(e)}")
                raise
        return current_data

# 示例工作流任务
class ExampleTask(WorkflowTask):
    def execute(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        示例任务：对数据进行简单的处理
        """"
        data['new_column'] = data['existing_column'] * 2
        return data

# 使用示例
if __name__ == '__main__':
    # 创建工作流引擎
    engine = WorkflowEngine()

    # 添加任务
    engine.add_task('example_task', ExampleTask())

    # 创建示例数据
    data = pd.DataFrame({'existing_column': [1, 2, 3]})

    # 运行工作流
    result = engine.run_workflow(data)
    print(result)
