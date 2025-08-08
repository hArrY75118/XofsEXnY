# 代码生成时间: 2025-08-09 00:19:39
import pandas as pd

"""
表单数据验证器

这个模块包含了一个表单数据验证器类，用于验证表单数据是否符合预设的规则。
"""

class FormDataValidator:
    """表单数据验证器类"""

    def __init__(self, rules):
        """初始化验证器

        参数:
        rules (dict): 验证规则，键为字段名，值为验证函数
        """
        self.rules = rules

    def validate(self, data):
        """验证表单数据

        参数:
        data (dict): 要验证的数据，键为字段名，值为字段值

        返回:
        tuple: 包含验证结果和错误信息的元组
        """
        errors = {}
        for field, rule in self.rules.items():
            try:
                # 应用验证规则
                rule(data[field])
            except ValueError as e:
                # 如果验证失败，记录错误信息
                errors[field] = str(e)
        
        # 如果有错误，返回False和错误信息；否则返回True和空的错误信息
        return (len(errors) == 0, errors)

    def add_rule(self, field, rule):
        "