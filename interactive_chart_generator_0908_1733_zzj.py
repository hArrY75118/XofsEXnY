# 代码生成时间: 2025-09-08 17:33:09
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import filedialog, messagebox
import numpy as np

"""
Interactive Chart Generator

This script creates an interactive chart generator using Python and Pandas.
It allows users to select a CSV file, choose chart types, and display the chart.
"""

class InteractiveChartGenerator:
    """Interactive Chart Generator class"""

    def __init__(self, root):
        """Initialize the application"""
        self.root = root
        self.root.title('Interactive Chart Generator')
        self.root.geometry('800x600')
        self.selected_file = None
        self.df = None

        # Create menu
        self.create_menu()

        # Create buttons
        self.create_buttons()

    def create_menu(self):
        "