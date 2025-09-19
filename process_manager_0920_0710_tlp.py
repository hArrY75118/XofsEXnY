# 代码生成时间: 2025-09-20 07:10:10
import psutil
import pandas as pd
from tabulate import tabulate

"""
Process Manager
=============

This module provides functionality to manage system processes. It allows users to
list processes, get details about a specific process, and terminate processes.

"""

def list_processes() -> pd.DataFrame:
    """
    Lists all running processes and returns a DataFrame with process information.

    Returns:
        pd.DataFrame: A DataFrame with columns 'PID', 'Name', 'Status', and 'Created Time'.
    """
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'status', 'create_time']):
        try:
            processes.append(proc.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue
    df = pd.DataFrame(processes)
    return df


def get_process_info(pid: int) -> pd.DataFrame:
    """
    Retrieves information about a specific process.

    Args:
        pid (int): The process ID.

    Returns:
        pd.DataFrame: A DataFrame with detailed information about the process.
    """
    try:
        proc = psutil.Process(pid)
        info = proc.as_dict(attrs=['pid', 'name', 'status', 'create_time', 'memory_info', 'cpu_times', 'io_counters', 'open_files', 'connections', 'num_threads'])
        df = pd.DataFrame([info])
        return df
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        print(f"No process found with PID {pid} or access denied.")
        return pd.DataFrame()


def terminate_process(pid: int) -> bool:
    "