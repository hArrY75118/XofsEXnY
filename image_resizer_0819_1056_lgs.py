# 代码生成时间: 2025-08-19 10:56:48
import os
import glob
from PIL import Image
import pandas as pd

"""
Image Resizer

A Python program that resizes images in a batch using the PIL library.

Attributes:
    None

Methods:
    resize_images(source_folder, output_folder, size): Resizes images from source folder to specified size and saves them in output folder.
"""

# Define a function to resize images
def resize_images(source_folder, output_folder, size, file_extension='*.jpg'):
    """
    Resizes multiple images from the source folder to the specified size and saves them to the output folder.

    Parameters:
        source_folder (str): The directory containing the original images.
        output_folder (str): The directory where the resized images will be saved.
        size (tuple): A tuple representing the new size of the images (width, height).
        file_extension (str): The file extension of the images to resize (default is '.jpg').
    """
    # Create the output folder if it does not exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Find all images in the source folder with the specified extension
    image_files = glob.glob(os.path.join(source_folder, file_extension))

    # Initialize a list to store the status of each image
    images_resized = []

    # Process each image file
    for image_file in image_files:
        try:
            # Open the image file
            with Image.open(image_file) as img:
                # Resize the image
                img = img.resize(size, Image.ANTIALIAS)

                # Construct the new file path
                new_file_path = os.path.join(output_folder, os.path.basename(image_file))

                # Save the resized image
                img.save(new_file_path)

                # Append the status to the list
                images_resized.append({'original_file': image_file, 'resized_file': new_file_path})

        except Exception as e:
            # Handle any exceptions and print the error message
            print(f"Error resizing {image_file}: {e}")

    # Return the list of resized images
    return images_resized

# Example usage
if __name__ == '__main__':
    source_folder = 'source_images'
    output_folder = 'resized_images'
    size = (800, 600)

    # Call the function to resize images
    resized_images = resize_images(source_folder, output_folder, size)

    # Create a DataFrame from the list of resized images
    df = pd.DataFrame(resized_images)

    # Print the DataFrame
    print(df)