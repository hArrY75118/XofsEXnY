# 代码生成时间: 2025-09-04 18:25:14
import psutil
import pandas as pd
import time

"""
System Performance Monitor tool using Python and Pandas.
This tool will collect system performance metrics at specified intervals and store the data in a DataFrame.
"""

class SystemPerformanceMonitor:
    """
    A class to monitor system performance metrics.
    """
    def __init__(self, interval=1):
        """
        Initialize the SystemPerformanceMonitor with the specified interval.
        :param interval: The interval in seconds between metric collections.
        """
        self.interval = interval
        self.metrics = []

    def collect_metrics(self):
        """
        Collect system performance metrics.
        """
        # Collect CPU metrics
        cpu_usage = psutil.cpu_percent(interval=1)

        # Collect memory metrics
        memory = psutil.virtual_memory()
        memory_usage = memory.percent

        # Collect disk metrics
        disk_usage = psutil.disk_usage('/')
        disk_usage_percent = disk_usage.percent

        # Collect network metrics
        net_io = psutil.net_io_counters()
        bytes_sent = net_io.bytes_sent
        bytes_recv = net_io.bytes_recv

        # Store the metrics in a list
        self.metrics.append({
            'timestamp': time.time(),
            'cpu_usage': cpu_usage,
            'memory_usage': memory_usage,
            'disk_usage_percent': disk_usage_percent,
            'bytes_sent': bytes_sent,
            'bytes_recv': bytes_recv
        })

    def start_monitoring(self):
        """
        Start monitoring system performance at the specified interval.
        """
        try:
            while True:
                self.collect_metrics()
                time.sleep(self.interval)
        except KeyboardInterrupt:
            print("Monitoring stopped.")

    def save_metrics_to_csv(self, filename):
        """
        Save the collected metrics to a CSV file.
        :param filename: The name of the CSV file to save the metrics to.
        """
        try:
            df = pd.DataFrame(self.metrics)
            df.to_csv(filename, index=False)
            print(f"Metrics saved to {filename}.")
        except Exception as e:
            print(f"Error saving metrics to CSV: {str(e)}")

    def display_metrics(self):
        """
        Display the collected metrics.
        """
        df = pd.DataFrame(self.metrics)
        print(df)

# Example usage
if __name__ == '__main__':
    monitor = SystemPerformanceMonitor(interval=5)
    monitor.start_monitoring()
    monitor.save_metrics_to_csv('system_metrics.csv')
    monitor.display_metrics()