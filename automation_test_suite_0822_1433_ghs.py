# 代码生成时间: 2025-08-22 14:33:11
import pandas as pd
import unittest

# 测试用例基类
class PandasTestCase(unittest.TestCase):
    def setUp(self):
        """ 设置测试环境，每个测试方法运行前都会执行 
        """
        # 这里可以初始化一些需要用到的数据或环境
        self.data = {'Name': ['John', 'Anna', 'James', 'Linda'],
                   'Age': [28, 23, 35, 29],
                   'Country': ['USA', 'UK', 'USA', 'UK']}
        self.df = pd.DataFrame(self.data)

    def tearDown(self):
        """ 清理测试环境，每个测试方法运行后都会执行 
        """
        # 这里可以进行一些清理工作，例如关闭数据库连接等
        pass

    # 测试DataFrame创建
    def test_dataframe_creation(self):
        """ 测试DataFrame是否可以正确创建 
        """
        self.assertIsInstance(self.df, pd.DataFrame)
        self.assertEqual(self.df.shape, (4, 3))

    # 测试DataFrame的列操作
    def test_dataframe_column_operations(self):
        """ 测试DataFrame的列操作 
        """
        self.assertIn('Name', self.df.columns)
        self.assertEqual(self.df['Name'].iloc[0], 'John')

    # 测试DataFrame的行操作
    def test_dataframe_row_operations(self):
        """ 测试DataFrame的行操作 
        """
        self.assertEqual(self.df.iloc[0]['Name'], 'John')
        self.assertEqual(self.df.iloc[-1]['Country'], 'UK')

    # 测试DataFrame的聚合操作
    def test_dataframe_aggregation(self):
        """ 测试DataFrame的聚合操作 
        """
        result = self.df['Age'].mean()
        self.assertAlmostEqual(result, 29.25)

# 运行测试套件
if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)
