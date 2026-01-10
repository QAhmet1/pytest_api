import requests
from utils.config_reader import ConfigReader
from utils.logger import get_logger


class BaseService:
    def __init__(self):
        # Initialize config reader to fetch environment settings
        self.config = ConfigReader()
        self.base_url = self.config.get_base_url()
        self.timeout = self.config.get_timeout()
        self.logger= get_logger()
        self.session = requests.Session()
        self.session.headers.update({"Content-Type": "application/json"})

    def request(self, method, endpoint, **kwargs):
        # A central method to handle all requests and logging
        url = f"{self.base_url}{endpoint}"
        # Logging the request details
        self.logger.info(f"Sending {method} request to: {url}")

        print(f"\n[REQUEST] {method} {url}")  # Detailed logging

        try:
            response = self.session.request(
                method,
                url,
                timeout=self.timeout,
                **kwargs
            )
            # Logging the response status
            self.logger.info(f"Response Status Code: {response.status_code}")

            # If request fails (4xx or 5xx), log it as an error
            if not response.ok:
                self.logger.error(f"Request failed with body: {response.text}")
            return response
        except requests.exceptions.RequestException as e:
            print(f"[ERROR] Request failed: {e}")
            raise