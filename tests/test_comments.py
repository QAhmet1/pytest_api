import allure
import pytest
from services.comment_service import CommentService
from utils.logger import get_logger

allure.feature("Comments API Management")
class TestComments:
    logger = get_logger()


    @pytest.fixture(scope="class")
    def comment_service(self):
        # Initialize the CommentService for the class
        return CommentService()
    @allure.story("Get all comments")
    def test_get_all_comments(self, comment_service):
        """Verify that fetching all comments returns 200."""
        response = comment_service.get_all_comments()
        assert response.status_code == 200
        assert isinstance(response.json(), list)

    @pytest.mark.parametrize("comment_id, expected_email", [
        (1, "Eliseo@gardner.biz"),
        (5, "Hayden@althea.biz")
    ])

    @allure.story("Get a comment by id")
    def test_get_comment_by_id(self, comment_service, comment_id, expected_email):
        """Verify comment data for specific IDs."""
        response = comment_service.get_comment_by_id(comment_id)
        assert response.status_code == 200
        assert response.json()["email"] == expected_email

    @allure.story("Get a comment by post id")
    def test_get_comments_by_post_filter(self, comment_service):
        """Verify filtering comments by post_id (Query Param)."""
        post_id = 2
        response = comment_service.get_comment_by_post_id(post_id)

        assert response.status_code == 200
        for comment in response.json():
            # Check if all returned comments belong to the requested post
            assert comment["postId"] == post_id

    @allure.story("Create a comment")
    def test_create_comment_flow(self, comment_service):
        """Verify creating a new comment for a post."""
        payload = {
            "postId": 1,
            "name": "New Tester Comment",
            "email": "test@test.com",
            "body": "This is a comment body."
        }
        # Correcting the POST endpoint usage
        response = comment_service.request("POST", "/comments", json=payload)
        assert response.status_code == 201
        assert response.json()["name"] == payload["name"]

    @allure.story("Update a comment")
    def test_update_comment_fully(self, comment_service):
        """Verify full update of a comment using PUT."""
        comment_id = 1
        payload = {
            "postId": 1,
            "id": 1,
            "name": "Updated Name",
            "email": "updated@test.com",
            "body": "Updated Body"
        }
        response = comment_service.update_comment_fully(comment_id, payload)
        assert response.status_code == 200
        assert response.json()["name"] == payload["name"]

    @allure.story("Update a comment partially")
    def test_update_comment_partial(self, comment_service):
        """Verify partial update of a comment using PATCH."""
        comment_id = 1
        payload = {
            "name": "Only updated Name",
        }
        response = comment_service.update_comment_partially(comment_id, payload)
        assert response.status_code == 200
        assert response.json()["name"] == payload["name"]

    @allure.story("Delete a comment")
    def test_delete_comment_flow(self, comment_service):
        """Verify deleting a comment."""
        comment_id = 1
        response = comment_service.delete_comment(comment_id)
        assert response.status_code == 200
        self.logger.info(f"Comment {comment_id} deleted successfully.")