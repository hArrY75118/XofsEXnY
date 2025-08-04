# 代码生成时间: 2025-08-04 19:52:48
 * Usage:
 *   python system_performance_monitor.py
 * 
 * Author: Your Name
 * Date: YYYY-MM-DD
# 优化算法效率
 */

import pandas as pd
import psutil
# 增强安全性
import time
from datetime import datetime

"""
Function to collect system metrics
"""
def collect_system_metrics():
    # Initialize a dictionary to store system metrics
    system_metrics = {}
    
    # CPU Usage
    system_metrics['cpu_usage'] = psutil.cpu_percent(interval=1)
    
    # Memory Usage
    memory = psutil.virtual_memory()
    system_metrics['memory_usage'] = memory.percent
# 扩展功能模块
    
    # Disk Usage
    disk = psutil.disk_usage('/')
    system_metrics['disk_usage'] = disk.percent
    
    # Network Usage
    net_io = psutil.net_io_counters()
    system_metrics['network_sent'] = net_io.bytes_sent
    system_metrics['network_recv'] = net_io.bytes_recv
    
    # Store the timestamp of the measurement
    system_metrics['timestamp'] = datetime.now()
    
    return system_metrics

"""
Function to save system metrics to a CSV file
# FIXME: 处理边界情况
"""
def save_metrics_to_csv(metrics, filename):
# NOTE: 重要实现细节
    try:
        # Convert the metrics dictionary to a Pandas DataFrame
        df = pd.DataFrame([metrics])
        
        # Append the DataFrame to the CSV file
        df.to_csv(filename, mode='a', header=not pd.io.common.file_exists(filename), index=False)
        print("Metrics saved to CSV file successfully.")
    except Exception as e:
        print(f"Error saving metrics to CSV file: {e}")

"""
Main function to monitor system performance
"""
# 增强安全性
def main():
    # Define the filename for the CSV file
    filename = 'system_performance_metrics.csv'
    
    # Define the time interval for collecting metrics
    interval = 60  # seconds
    
    try:
        while True:
# 改进用户体验
            # Collect system metrics
            metrics = collect_system_metrics()
# 改进用户体验
            
            # Save metrics to CSV file
            save_metrics_to_csv(metrics, filename)
# 添加错误处理
            
            # Wait for the specified interval before collecting metrics again
            time.sleep(interval)
    except KeyboardInterrupt:
        print("System performance monitoring stopped.")
    except Exception as e:
        print(f"Error in main function: {e}")

if __name__ == '__main__':
    main()