import allure
import pytest

from services.post_service import PostService
from utils.logger import get_logger


@allure.feature("Posts API Management")
class TestPost:
    logger =get_logger()

    @pytest.fixture(scope="class")
    def post_service(self):
        # Initialize the post service for the test class
        return PostService()

    @allure.story("Getting all posts")
    def get_all_posts_status_code(self, post_service):
        self.logger.info("Verify that fetching all posts returns a 200 OK status.")
        """Verify that fetching all posts returns a 200 OK status."""
        response = post_service.get_all_posts()
        assert response.status_code == 200
        assert len(response.json) > 0

    @pytest.mark.parametrize("post_id,expected_title",[
         (1,"sunt aut facere repellat provident occaecati excepturi optio reprehenderit"),
         (2,"qui est esse"),
         (3,"ea molestias quasi exercitationem repellat qui ipsa sit aut")
    ])

    @allure.story("Getting a specific post")
    def test_single_post_content(self, post_service,post_id,expected_title):
        self.logger.info("Verify the content of specific posts using data-driven approach.")
        response= post_service.get_post_by_id(post_id)
        assert response.status_code == 200
        assert response.json()["title"] == expected_title

    @allure.story("Creating a post")
    def test_create_post_flow(self, post_service):
        self.logger.info("Verify that post creation flow works.")
        payload = {
            "title":"API Automation",
            "body":"Testing with Pytest is great!",
            "userId":1
        }
        response= post_service.create_post(payload)
        assert response.status_code == 201
        assert response.json()["title"] == "API Automation"
        assert response.json()["body"] == "Testing with Pytest is great!"
        self.logger.info(f"Post created with ID: {response.json().get('id')}")

        # --- NEGATIVE TESTS ---
    @allure.story("Getting a post with invalid post ID")
    def test_get_non_existing_post(self, post_service):
        self.logger.info("Verify that requesting a non-existent post returns 404.")
        response= post_service.get_post_by_id(999)
        assert response.status_code == 404
        self.logger.info("Correctly received 404 for invalid post ID.")
    @allure.story("Creating a post with invalid user ID")
    def test_create_post_with_invalid_userId(self, post_service):
        """
                Verify how the API handles invalid user IDs during post creation.
                Note: JSONPlaceholder is a mock API and might still return 201.
                """
        payload = {
            "title":"wrong user",
            "body":"wrong content",
            "userId":999 #invalid user id
        }
        response= post_service.create_post(payload)
        assert response.status_code == 201
        self.logger.info("Correctly received 201 for invalid user ID. NOTE: In real projects it returns 400")
    @allure.story("Updating a post")
    def test_update_post_fully(self,post_service,):
        """Verify that a post can be fully updated using PUT."""
        post_id =1
        payload = {
            "title":"API Automation-updated",
            "body":"Testing with Pytest is great! - Updated",
            "userId":1
        }
        response= post_service.update_post(post_id,payload)
        assert response.status_code == 200
        assert response.json()["title"] == "API Automation-updated"
        assert response.json()["body"] == payload["body"]
    @allure.story("Updating a post partially")
    def test_partially_update_post(self,post_service):
        """Verify that a post can be partially updated using PUT."""
        post_id =1
        payload = {
            "title":"Only title updated",
        }
        self.logger.info(f"Updating post {post_id} partially...")
        response= post_service.partial_update_post(post_id,payload)
        assert response.status_code == 200
        assert response.json()["title"] == payload["title"]
    @allure.story("Delete a post")
    def test_delete_post_successfully(self,post_service):
        """Verify that a post can be deleted using DELETE."""
        post_id =1
        self.logger.info(f"Deleting post {post_id} ...")
        response= post_service.delete_post(post_id)
        assert response.status_code == 200
        self.logger.info(f"Deleted post {post_id} successfully.")



