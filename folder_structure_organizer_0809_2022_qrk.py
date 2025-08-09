# 代码生成时间: 2025-08-09 20:22:39
import os
import shutil
from pathlib import Path

"""
Folder Structure Organizer
This script organizes files in a specified directory into subdirectories based on file extensions.
"""

class FolderStructureOrganizer:
    def __init__(self, source_dir):
        """
        Initialize the FolderStructureOrganizer with the source directory.
        :param source_dir: Path to the directory to be organized
        """
        self.source_dir = Path(source_dir)
        if not self.source_dir.exists():
            raise ValueError(f"The directory {source_dir} does not exist.")
        if not self.source_dir.is_dir():
            raise ValueError(f"The path {source_dir} is not a directory.")

    def organize(self):
        """
        Organize files in the source directory into subdirectories based on their extensions.
        """
        # Check if the source directory is empty
        if not os.listdir(self.source_dir):
            print("The source directory is empty. Nothing to organize.")
            return

        # Iterate over each file in the source directory
        for file in os.listdir(self.source_dir):
            file_path = self.source_dir / file
            # Skip if it's a directory, not a file
            if file_path.is_dir():
                continue

            # Get the file extension and create a corresponding subdirectory
            file_extension = file_path.suffix
            if not file_extension:
                continue  # Skip files without extension

            target_dir = self.source_dir / file_extension[1:]  # Remove the dot from the extension
            target_dir.mkdir(exist_ok=True)  # Create the directory if it doesn't exist

            # Move the file to the new directory
            shutil.move(str(file_path), str(target_dir / file_path.name))
            print(f"Moved {file} to {target_dir / file_path.name}")

    def __str__(self):
        return f"FolderStructureOrganizer for directory: {self.source_dir}"


def main():
    """
    Main function to run the folder organizer.
    """
    # Specify the source directory
    source_dir_input = input("Enter the path to the directory you want to organize: ")
    try:
        organizer = FolderStructureOrganizer(source_dir_input)
        organizer.organize()
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
