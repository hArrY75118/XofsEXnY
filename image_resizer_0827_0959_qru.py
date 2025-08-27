# 代码生成时间: 2025-08-27 09:59:22
import os
import glob
from PIL import Image
import pandas as pd

"""
Image Resizer

This module is designed to batch resize images based on given dimensions.
It takes a directory path containing images, resizes them to the specified dimensions,
and saves them in the same directory or a new one.
"""

class ImageResizer:
    def __init__(self, directory, output_directory=None, size=(640, 480), new_size=None):
        """
        Initialize the ImageResizer with the directory of images, optional output directory,
        and the new size to resize the images to.
        
        :param directory: Path to the directory containing images.
        :param output_directory: Optional path to the output directory.
        :param size: A tuple representing the size to resize images to.
        :param new_size: A tuple representing a new size that can be used to override the size parameter.
        """
        self.directory = directory
        self.output_directory = output_directory if output_directory else directory
        self.size = new_size if new_size else size
        self.images = self._load_images()

    def _load_images(self):
        """
        Private method to load images from the directory.
        
        :return: A list of image paths.
        """
        try:
            # Load all image files from the directory
            return glob.glob(os.path.join(self.directory, '*'))
        except Exception as e:
            raise FileNotFoundError(f"Error loading images: {e}")

    def resize_images(self):
        """
        Resize all images in the directory and save them to the output directory.
        
        :return: A pandas DataFrame with details of the resized images.
        """
        resized_images = []
        for image_path in self.images:
            try:
                with Image.open(image_path) as img:
                    # Resize the image
                    resized_img = img.resize(self.size)
                    # Save the resized image
                    filename = os.path.basename(image_path)
                    new_path = os.path.join(self.output_directory, filename)
                    resized_img.save(new_path)
                    resized_images.append({"Original Path": image_path, "New Path": new_path})
            except Exception as e:
                print(f"Error resizing {image_path}: {e}")
        return pd.DataFrame(resized_images)

if __name__ == '__main__':
    # Example usage
    directory_path = '/path/to/images'
    output_path = '/path/to/output'
    # Create an instance of ImageResizer
    resizer = ImageResizer(directory_path, output_path, size=(1024, 768))
    
    # Resize images and get a report
    report = resizer.resize_images()
    print(report)