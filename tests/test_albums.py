import allure
import pytest
from services.album_service import AlbumService
from utils.logger import get_logger

@allure.feature("Albums API Management")
class TestAlbums:
    logger = get_logger()


    @pytest.fixture(scope="class")
    def album_service(self):
        # Dependency injection for AlbumService
        return AlbumService()
    @allure.story("Get all albums")
    def test_get_all_albums_status(self, album_service):
        """Verify that fetching all albums returns 200."""
        response = album_service.get_all_albums()
        assert response.status_code == 200
        assert len(response.json()) > 0

    @allure.story("Verify album title")
    @pytest.mark.parametrize("album_id, expected_title", [
        (1, "quidem molestiae enim"),
        (2, "sunt qui excepturi placeat culpa")
    ])
    def test_album_titles(self, album_service, album_id, expected_title):
        """Verify the title of specific albums (Data Driven)."""
        response = album_service.get_album_by_id(album_id)
        assert response.status_code == 200
        assert response.json()["title"] == expected_title

    @allure.story("Get albums by userId")
    def test_filter_albums_by_user(self, album_service):
        """Verify that filtering by userId=1 only returns albums of that user."""
        user_id = 1
        self.logger.info(f"Filtering albums for user: {user_id}")
        response = album_service.get_album_by_user_id(user_id)

        assert response.status_code == 200
        albums = response.json()

        for album in albums:
            # Relational integrity check
            assert album["userId"] == user_id
        self.logger.info(f"Successfully verified {len(albums)} albums for user {user_id}")

    @allure.story("Create a new album")
    def test_create_album_flow(self, album_service):
        """Verify that a user can create a new album."""
        payload = {
            "title": "My Holiday Photos",
            "userId": 5
        }
        response = album_service.create_album(payload)
        assert response.status_code == 201
        assert response.json()["title"] == payload["title"]
        assert response.json()["userId"] == 5