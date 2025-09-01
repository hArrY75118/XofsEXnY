# 代码生成时间: 2025-09-02 02:36:35
import pandas as pd

"""
Form Data Validator

This module provides a simple form data validator using the pandas library.
It checks if the given data matches the specified schema and validates
the data types, required fields, and optional constraints.
"""

class FormDataValidator:
    """
    A class to validate form data against a schema.
    """
    def __init__(self, schema):
        """
        Initialize the validator with a schema.
        :param schema: A dict specifying the expected data structure.
        """
        self.schema = schema

    def validate(self, data):
        """
        Validate the given data against the schema.
        :param data: A pandas DataFrame to validate.
        :return: A pandas DataFrame with NaN values for invalid entries.
        """
        # Check if data is a pandas DataFrame
        if not isinstance(data, pd.DataFrame):
            raise ValueError("Data must be a pandas DataFrame.")
        
        # Check if the number of columns in data matches the schema
        if len(data.columns) != len(self.schema):
            raise ValueError("The number of columns in data does not match the schema.")
        
        # Initialize a new DataFrame to store the validated data
        validated_data = pd.DataFrame(index=data.index)
        
        for column, constraints in self.schema.items():
            # Check if the column exists in the data
            if column not in data.columns:
                raise ValueError(f"Column '{column}' not found in the data.")
            
            # Check the data type of the column
            if data[column].dtype != constraints['type']:
                raise TypeError(f"Data type mismatch for column '{column}'. Expected {constraints['type']}.")
            
            # Check for required columns
            if 'required' in constraints and constraints['required']:
                if data[column].isnull().any():
                    raise ValueError(f"Column '{column}' is required but has missing values.")
            
            # Add the validated column to the validated data
            validated_data[column] = data[column]
        
        return validated_data

# Example usage
if __name__ == '__main__':
    schema = {
        'name': {'type': 'str', 'required': True},
        'age': {'type': 'int', 'required': True},
        'email': {'type': 'str', 'required': False}
    }
    
    # Create a sample DataFrame
    data = pd.DataFrame({
        'name': ['Alice', 'Bob', None],
        'age': [25, 30, 35],
        'email': ['alice@example.com', 'bob@example.com', None]
    })
    
    validator = FormDataValidator(schema)
    try:
        validated_data = validator.validate(data)
        print(validated_data)
    except Exception as e:
        print(f"Validation error: {e}")