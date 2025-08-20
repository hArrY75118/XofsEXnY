# 代码生成时间: 2025-08-21 07:17:21
import pandas as pd
import os
import shutil
from datetime import datetime

"""
Data backup and restore program using Python and Pandas.

This program allows for the backup of a specified CSV file to a specified directory,
and provides a method to restore the data from the backup.
"""

# Define the class for data backup and restore
class DataBackupRestore:
    def __init__(self, source_file_path, backup_directory):
        """
        Initialize the DataBackupRestore class with the source file and backup directory.
        :param source_file_path: str, path to the CSV file to be backed up
        :param backup_directory: str, directory where the backup should be stored
        """
        self.source_file_path = source_file_path
        self.backup_directory = backup_directory
        self.backup_file_name = None

    def backup(self):
        """
        Backup the data from the source file to the backup directory.
        """
        try:
            # Check if the source file exists
            if not os.path.exists(self.source_file_path):
                raise FileNotFoundError("Source file not found.")

            # Create a timestamped backup file name
            self.backup_file_name = "backup_{}.csv".format(datetime.now().strftime('%Y%m%d%H%M%S'))

            # Create the backup directory if it does not exist
            os.makedirs(self.backup_directory, exist_ok=True)

            # Copy the source file to the backup directory with the new name
            shutil.copy(self.source_file_path, os.path.join(self.backup_directory, self.backup_file_name))
            print(f"Data backed up successfully to {self.backup_file_name}.")

        except Exception as e:
            print(f"An error occurred during backup: {e}")

    def restore(self, restore_file_name):
        """
        Restore the data from the backup file to the source file.
        :param restore_file_name: str, name of the backup file to restore from
        """
        try:
            # Check if the backup file exists
            backup_file_path = os.path.join(self.backup_directory, restore_file_name)
            if not os.path.exists(backup_file_path):
                raise FileNotFoundError("Backup file not found.")

            # Copy the backup file to the source file path
            shutil.copy(backup_file_path, self.source_file_path)
            print(f"Data restored successfully from {restore_file_name}.")

        except Exception as e:
            print(f"An error occurred during restore: {e}")

# Example usage
if __name__ == '__main__':
    # Define the source file path and backup directory
    source_file_path = "./data.csv"
    backup_directory = "./backups"

    # Create an instance of DataBackupRestore
    db_restore = DataBackupRestore(source_file_path, backup_directory)

    # Perform a backup
    db_restore.backup()

    # Perform a restore (replace 'backup_20230328120000.csv' with the actual backup file name)
    db_restore.restore('backup_20230328120000.csv')