# 代码生成时间: 2025-09-05 21:55:48
import psutil
import pandas as pd
import time

"""
System Performance Monitor using Python and Pandas
"""

class SystemPerformanceMonitor:
    """Monitor system performance metrics using psutil and Pandas"""

    def __init__(self):
        """Initialize the System Performance Monitor"""
        self.metrics = []

    def get_cpu_usage(self):
        """Get CPU usage percentage"""
        try:
            cpu_usage = psutil.cpu_percent(interval=1)
            return cpu_usage
        except Exception as e:
            print(f"Error getting CPU usage: {e}")
            return None

    def get_memory_usage(self):
        """Get memory usage details"""
        try:
            memory = psutil.virtual_memory()
            memory_usage = {
                "total": memory.total / (1024 ** 3),  # GB
                "available": memory.available / (1024 ** 3),  # GB
                "used": memory.used / (1024 ** 3),  # GB
                "percentage": memory.percent
            }
            return memory_usage
        except Exception as e:
            print(f"Error getting memory usage: {e}")
            return None

    def get_disk_usage(self):
        """Get disk usage details"""
        try:
            disk_usage = psutil.disk_usage('/')
            disk_usage_details = {
                "total": disk_usage.total / (1024 ** 3),  # GB
                "used": disk_usage.used / (1024 ** 3),  # GB
                "free": disk_usage.free / (1024 ** 3),  # GB
                "percentage": disk_usage.percent
            }
            return disk_usage_details
        except Exception as e:
            print(f"Error getting disk usage: {e}")
            return None

    def get_network_usage(self):
        """Get network usage details"""
        try:
            network_stats = psutil.net_io_counters()
            network_usage = {
                "bytes_sent": network_stats.bytes_sent,
                "bytes_recv": network_stats.bytes_recv,
                "packets_sent": network_stats.packets_sent,
                "packets_recv": network_stats.packets_recv
            }
            return network_usage
        except Exception as e:
            print(f"Error getting network usage: {e}")
            return None

    def monitor_performance(self, interval=5, duration=60):
        """Monitor system performance metrics over a specified duration and interval"""
        try:
            for _ in range(int(duration / interval)):
                time.sleep(interval)
                cpu_usage = self.get_cpu_usage()
                memory_usage = self.get_memory_usage()
                disk_usage = self.get_disk_usage()
                network_usage = self.get_network_usage()

                # Create a DataFrame for the metrics
                df = pd.DataFrame([
                    {
                        "timestamp": time.time(),
                        "cpu_usage": cpu_usage,
                        "memory_usage": memory_usage,
                        "disk_usage": disk_usage,
                        "network_usage": network_usage
                    }
                ])

                # Append the DataFrame to the metrics list
                self.metrics.append(df)

            # Concatenate all DataFrames into a single DataFrame
            metrics_df = pd.concat(self.metrics, ignore_index=True)
            return metrics_df

        except Exception as e:
            print(f"Error monitoring performance: {e}")
            return None


# Example usage
if __name__ == "__main__":
    monitor = SystemPerformanceMonitor()
    metrics_df = monitor.monitor_performance(interval=5, duration=60)
    if metrics_df is not None:
        print(metrics_df)