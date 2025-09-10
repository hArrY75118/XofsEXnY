# 代码生成时间: 2025-09-10 16:56:38
import pandas as pd
from pathlib import Path

"""
Document Converter

This module provides a function to convert documents from one format to another
using the PANDAS framework.
"""

def convert_document(input_path: str, output_path: str, output_format: str):
    """Converts a document from one format to another.

    Args:
        input_path (str): The path to the input document.
        output_path (str): The path to save the converted document.
        output_format (str): The format of the output document.
    
    Raises:
        ValueError: If the output format is not supported.
        FileNotFoundError: If the input document does not exist.
    """
    # Check if the output format is supported
    supported_formats = ['csv', 'xlsx', 'json']
    if output_format not in supported_formats:
        raise ValueError(f"Unsupported output format: {output_format}. Supported formats are: {supported_formats}")
    
    # Check if the input file exists
    try:
        input_file = Path(input_path)
        if not input_file.is_file():
            raise FileNotFoundError(f"Input file not found: {input_path}")
    except Exception as e:
        raise Exception(f"An error occurred while checking the input file: {e}")
    
    # Read the input document
    try:
        if input_file.suffix == '.csv':
            df = pd.read_csv(input_path)
        elif input_file.suffix == '.xlsx':
            df = pd.read_excel(input_path)
        elif input_file.suffix == '.json':
            df = pd.read_json(input_path)
        else:
            raise ValueError(f"Unsupported input format: {input_file.suffix}. Supported formats are: csv, xlsx, json")
    except Exception as e:
        raise Exception(f"An error occurred while reading the input file: {e}")
    
    # Convert the document to the specified format
    try:
        if output_format == 'csv':
            df.to_csv(output_path, index=False)
        elif output_format == 'xlsx':
            df.to_excel(output_path, index=False)
        elif output_format == 'json':
            df.to_json(output_path, orient='records')
    except Exception as e:
        raise Exception(f"An error occurred while converting the document: {e}")
    
    print(f"Document successfully converted to {output_format} and saved to {output_path}")

# Example usage:
# convert_document('input.csv', 'output.xlsx', 'xlsx')
