import pytest
import allure
from services.photo_service import PhotoService
from utils.logger import get_logger


@allure.feature("Photos API Management")
class TestPhotos:
    logger = get_logger()

    @pytest.fixture(scope="class")
    def photo_service(self):
        return PhotoService()

    @allure.story("Verify Photo Data and URL Format")
    def test_photo_url_structure(self, photo_service):
        """Verify that the photo URLs start with the expected placeholder domain."""
        photo_id = 1
        response = photo_service.get_photo_by_id(photo_id)

        assert response.status_code == 200
        data = response.json()

        # Check if URL fields are actually strings and start with http
        assert data["url"].startswith("https://via.placeholder.com"), "Main URL format is incorrect!"
        assert data["thumbnailUrl"].startswith("https://via.placeholder.com"), "Thumbnail URL format is incorrect!"
        self.logger.info(f"Verified URL formats for photo {photo_id}")

    @allure.story("Relational Integrity: Album and Photos")
    def test_photos_belong_to_correct_album(self, photo_service):
        """Verify that all photos returned for albumId=1 actually belong to that album."""
        album_id = 1
        response = photo_service.get_photos_by_album_id(album_id)

        assert response.status_code == 200
        photos = response.json()

        # JSONPlaceholder usually has 50 photos per album
        assert len(photos) > 0
        for photo in photos:
            assert photo["albumId"] == album_id
        self.logger.info(f"Verified {len(photos)} photos belong to album {album_id}")

    @allure.story("Data Integrity")
    @pytest.mark.parametrize("photo_id, expected_title", [
        (1, "accusamus beatae ad facilis cum similique qui sunt"),
        (2, "reprehenderit est deserunt velit ipsam")
    ])
    def test_specific_photo_titles(self, photo_service, photo_id, expected_title):
        """Data-driven test for photo titles."""
        response = photo_service.get_photo_by_id(photo_id)
        assert response.status_code == 200
        assert response.json()["title"] == expected_title

    @allure.story("Create a new photo")
    def test_create_photo(self,photo_service):
        """Create a new photo."""
        payload ={
            "albumId": 1,
            "title": "accusamus",
            "url": "https://via.placeholder.com",
            "thumbnailUrl": "https://via.placeholder.com",

        }
        response = photo_service.create_photo(payload)
        assert response.status_code == 201
        assert response.json()["title"] == payload["title"]
