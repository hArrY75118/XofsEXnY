# 代码生成时间: 2025-08-24 02:10:42
import pandas as pd
import requests
from bs4 import BeautifulSoup

"""
Web Content Scraper

This program is designed to scrape content from web pages.
It uses the pandas library for data manipulation, requests for making HTTP requests,
and BeautifulSoup for parsing HTML content.
"""

class WebContentScraper:
    def __init__(self, url):
        """Initialize the WebContentScraper with a given URL."""
        self.url = url
        self.data = None

    def fetch_content(self):
        """Fetch the content from the specified URL."""
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Raise an HTTPError if the HTTP request returned an unsuccessful status code
            self.data = response.text
        except requests.exceptions.RequestException as e:
            print(f"An error occurred while fetching content: {e}")

    def parse_content(self):
        """Parse the fetched content using BeautifulSoup."""
        if self.data is None:
            print("No content fetched. Please run fetch_content() first.")
            return None

        soup = BeautifulSoup(self.data, 'html.parser')
        return soup

    def extract_table(self):
        """Extract a table from the parsed content and return it as a pandas DataFrame."""
        try:
            soup = self.parse_content()
            if soup is None:
                return None

            table = soup.find('table')
            if table is None:
                print("No table found in the content.")
                return None

            df = pd.read_html(str(table))[0]
            return df
        except Exception as e:
            print(f"An error occurred while extracting table: {e}")
            return None

    def save_to_csv(self, df, file_path):
        """Save the extracted table to a CSV file."""
        try:
            df.to_csv(file_path, index=False)
            print(f"Data saved to {file_path}")
        except Exception as e:
            print(f"An error occurred while saving to CSV: {e}")

# Example usage:
if __name__ == '__main__':
    url = "http://example.com"
    scraper = WebContentScraper(url)
    scraper.fetch_content()
    table_df = scraper.extract_table()
    if table_df is not None:
        scraper.save_to_csv(table_df, "output.csv")
