"""API client for external data sources"""
import requests

class APIClient:
    def __init__(self, base_url, api_key):
        self.base_url = base_url
        self.api_key = api_key

    def fetch_data(self, endpoint):
        """Fetch data from API endpoint"""
        return requests.get(f"{self.base_url}/{endpoint}")
