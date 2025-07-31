# 代码生成时间: 2025-07-31 19:56:01
import psutil
import pandas as pd

"""
Memory Usage Analysis Program
===========================

This program analyzes the memory usage of the system and provides a detailed breakdown of memory usage.

Features:
- Retrieves memory usage statistics
- Converts bytes to human-readable format
- Provides a DataFrame with memory usage details

Usage:
- Run the program to get a DataFrame with memory usage details

"""


def get_memory_usage() -> pd.DataFrame:
    """
    Retrieves memory usage statistics and returns a DataFrame with human-readable values.

    Returns:
        pd.DataFrame: A DataFrame containing memory usage details
    """
    try:
        # Get memory usage statistics
        mem = psutil.virtual_memory()

        # Convert bytes to human-readable format
        total = f"{mem.total / (1024 ** 3):.2f} GB"
        available = f"{mem.available / (1024 ** 3):.2f} GB"
        used = f"{mem.used / (1024 ** 3):.2f} GB"
        free = f"{mem.free / (1024 ** 3):.2f} GB"
        used_percent = f"{mem.percent}%"

        # Create a DataFrame with memory usage details
        mem_usage_df = pd.DataFrame(
            {
                "Total Memory": [total],
                "Available Memory": [available],
                "Used Memory": [used],
                "Free Memory": [free],
                "Memory Usage (%)": [used_percent],
            }
        )

        return mem_usage_df

    except Exception as e:
        # Handle any exceptions that occur during memory usage retrieval
        print(f"An error occurred: {e}")
        return None


if __name__ == "__main__":
    # Run the memory usage analysis program
    mem_usage_df = get_memory_usage()
    if mem_usage_df is not None:
        # Print the memory usage DataFrame
        print(mem_usage_df)
    else:
        print("Failed to retrieve memory usage statistics.")