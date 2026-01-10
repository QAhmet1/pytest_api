import allure
import pytest
from services.user_service import UserService
from utils.logger import get_logger

@allure.feature("User API Management")
class TestUsers:
    logger = get_logger()
    @pytest.fixture(scope="class")
    def user_service(self):
        # Initialize the service once for the entire test class
        return UserService()

    def test_status_code_check(self, user_service):
        # Verify that the GET users endpoint is working
        response = user_service.get_all_users()
        assert response.status_code == 200

    @allure.story("get all users")
    @pytest.mark.parametrize("user_id, expected_name", [
        (1, "Leanne Graham"),
        (2, "Ervin Howell"),
        (3, "Clementine Bauch")
    ])
    def test_user_names(self, user_service, user_id, expected_name):
        # Data-driven test: check multiple users in one test function
        response = user_service.get_user_by_id(user_id)
        assert response.json()["name"] == expected_name

    @allure.story("Create a new user")
    def test_create_user_flow(self, user_service):
        self.logger.info("--- Starting Test: Create User Flow ---")

        payload = {"name": "Test User", "email": "test@test.com"}
        response = user_service.create_user(payload)

        assert response.status_code == 201
        self.logger.info(f"User created successfully with ID: {response.json().get('id')}")