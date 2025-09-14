# 代码生成时间: 2025-09-15 03:23:46
import psutil
import pandas as pd

"""
Process Manager using Python and Pandas framework.
This program allows users to view and filter system processes.
"""

class ProcessManager:
    """
    Class to manage system processes using psutil and Pandas.
    """

    def __init__(self):
        """Initialize the process manager."""
        self.processes = self.get_all_processes()

    def get_all_processes(self):
        """
        Get all system processes as a Pandas DataFrame.

        Returns:
            pd.DataFrame: DataFrame containing process information.
        """
        processes = []
        for proc in psutil.process_iter(['pid', 'name', 'status', 'username']):
            try:
                process_info = proc.info
                processes.append(process_info)
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                # Handle exceptions for processes that no longer exist or cannot be accessed
                pass

        return pd.DataFrame(processes)

    def filter_processes(self, **kwargs):
        """
        Filter processes based on provided keyword arguments.

        Args:
            **kwargs: Keyword arguments to filter processes (e.g., name, status, username).

        Returns:
            pd.DataFrame: Filtered DataFrame containing process information.
        """
        filtered_processes = self.processes.copy()
        for key, value in kwargs.items():
            filtered_processes = filtered_processes[filtered_processes[key] == value]
        return filtered_processes

    def display_processes(self, processes):
        """
        Display process information in a formatted table.

        Args:
            processes (pd.DataFrame): DataFrame containing process information to display.
        """
        print(processes.to_string(index=False))

if __name__ == '__main__':
    """
    Main entry point of the program.
    Run the process manager and display all system processes.
    """
    try:
        process_manager = ProcessManager()
        display_processes = process_manager.display_processes(process_manager.processes)
    except Exception as e:
        print(f"Error: {e}")
