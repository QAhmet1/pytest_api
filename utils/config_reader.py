import configparser
import os

class ConfigReader:
    def __init__(self):
        # Create a config parser object
        self.config = configparser.ConfigParser()
        # Get the absolute path of the config file
        path = os.path.join(os.path.dirname(__file__), '../config.ini')
        self.config.read(path)

    def get_base_url(self):
        # Fetch the base URL from the [api] section
        return self.config.get('api', 'base_url')

    def get_timeout(self):
        # Fetch timeout value as an integer
        return self.config.getint('api', 'timeout')