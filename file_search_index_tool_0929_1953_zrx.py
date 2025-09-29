# 代码生成时间: 2025-09-29 19:53:01
import os
import pandas as pd
from pathlib import Path

"""
A file search and indexing tool using Python and Pandas.

This tool allows users to search for files within a directory and its subdirectories,
and then create an index of those files.
"""

class FileSearchIndexTool:
    def __init__(self, root_directory):
        """Initialize the tool with the root directory to search."""
        self.root_directory = Path(root_directory)

        if not self.root_directory.exists():
            raise ValueError(f"The directory {self.root_directory} does not exist.")

    def search_files(self, extension=None):
        "