# 代码生成时间: 2025-09-06 08:41:23
import psutil
import pandas as pd
import time
import json

"""
System Performance Monitor Tool using Python and Pandas.

This tool will monitor system performance metrics such as CPU utilization,
memory usage, disk usage, and network activity.
"""

# Function to get CPU utilization
def get_cpu_usage():
    """
    Get the current CPU utilization percentage.

    Returns:
        float: CPU utilization percentage.
    """
    return psutil.cpu_percent(interval=1)


# Function to get memory usage
def get_memory_usage():
    """
    Get the current memory usage as a percentage of total memory.

    Returns:
        float: Memory usage percentage.
    """
    memory = psutil.virtual_memory()
    return (memory.used / memory.total) * 100


# Function to get disk usage
def get_disk_usage():
    """
    Get the current disk usage percentage for all partitions.

    Returns:
        dict: Dictionary with partition names as keys and usage percentages as values.
    """
    disk_usage = {}
    for partition in psutil.disk_partitions():
        usage = psutil.disk_usage(partition.mountpoint)
        disk_usage[partition.device] = (usage.used / usage.total) * 100
    return disk_usage


# Function to get network activity
def get_network_activity():
    """
    Get the current network activity (bytes sent and received).

    Returns:
        dict: Dictionary with network interfaces as keys and total bytes as values.
    """
    network_activity = {}
    for interface, stats in psutil.net_io_counters(pernic=True).items():
        network_activity[interface] = {
            "bytes_sent": stats.bytes_sent,
            "bytes_recv": stats.bytes_recv
        }
    return network_activity


# Function to monitor system performance
def monitor_system_performance(interval):
    """
    Monitor system performance metrics at a specified interval.

    Args:
        interval (int): Time interval in seconds between each measurement.
    """
    try:
        while True:
            # Get system performance metrics
            cpu_usage = get_cpu_usage()
            memory_usage = get_memory_usage()
            disk_usage = get_disk_usage()
            network_activity = get_network_activity()

            # Create a Pandas DataFrame to store the metrics
            df = pd.DataFrame(
                {
                    "CPU Usage": [cpu_usage],
                    "Memory Usage": [memory_usage],
                    "Disk Usage": list(disk_usage.values()),
                    "Network Activity": [json.dumps(network_activity)]
                },
                index=[time.time()]
            )

            # Print the DataFrame
            print(df)

            # Wait for the specified interval
            time.sleep(interval)

    except KeyboardInterrupt:
        print("Monitoring stopped by user.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Run the system performance monitor tool
    interval = 5  # Set the interval to 5 seconds
    monitor_system_performance(interval)