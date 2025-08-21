# 代码生成时间: 2025-08-21 18:13:55
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import numpy as np

"""
Interactive Chart Generator

This program allows the user to generate interactive charts from a specified CSV file.
It provides the ability to update the chart dynamically when the user selects different columns.
"""

class InteractiveChartGenerator:
    def __init__(self, filepath):
        """
        Initialize the InteractiveChartGenerator with a CSV file.
        :param filepath: Path to the CSV file containing the data.
        """
        self.filepath = filepath
        self.data = pd.read_csv(filepath)
        self.fig, self.ax = plt.subplots()
        self.buttons = {}

    def generate_chart(self):
        "