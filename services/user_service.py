from services.base_service import BaseService

class UserService(BaseService):
    def __init__(self):
        super().__init__()
        self.endpoint = "/users"

    def get_all_users(self):
        # Logic to fetch all users from the endpoint
        return self.request("GET", self.endpoint)

    def get_user_by_id(self, user_id):
        # Logic to fetch a specific user by their unique ID
        return self.request("GET", f"{self.endpoint}/{user_id}")

    def create_user(self, payload):
        """
        Sends a POST request to create a new user.
        :param payload: Dictionary containing user data (e.g., name, email)
        :return: Response object from the POST request
        """
        return self.request("POST", self.endpoint, json=payload)