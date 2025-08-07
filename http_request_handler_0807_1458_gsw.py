# 代码生成时间: 2025-08-07 14:58:12
import pandas as pd
import requests
from flask import Flask, request, jsonify
from requests.exceptions import RequestException

"""
HTTP Request Handler Application
This application handles HTTP requests and provides a simple API to interact with.
It can make GET requests to any specified URL and return results as a JSON response.
"""

app = Flask(__name__)

@app.route('/fetch-data', methods=['GET'])
def fetch_data():
    """
    Endpoint to fetch data from a specified URL.
    It accepts a URL as a query parameter, makes a GET request to the URL,
    and returns the response as a JSON object along with HTTP status code.
    """
    try:
        # Extract the URL parameter from the request
        url = request.args.get('url')
        if not url:
            return jsonify({'error': 'URL parameter is required'}), 400

        # Make a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Convert response content to a pandas DataFrame
        data = pd.json_normalize(response.json())

        # Return the DataFrame as a JSON response
        return jsonify(data.to_dict(orient='records')), 200
    except RequestException as e:
        # Handle any request-related exceptions
        return jsonify({'error': str(e)}), 500
    except ValueError as e:
        # Handle any JSON-related exceptions
        return jsonify({'error': 'Invalid JSON response'}), 500
    except Exception as e:
        # Handle any other exceptions
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)