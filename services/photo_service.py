from services.base_service import BaseService


class PhotoService(BaseService):
    def __init__(self):
        super().__init__()
        self.endpoint = "/photos"

    def get_all_photos(self):
        """ Get all photos """
        return self.request("GET", self.endpoint)
    def get_photo_by_id(self, photo_id):
        """ Get photo by id """
        return self.request("GET", f"{self.endpoint}/{photo_id}")
    def get_photos_by_album_id(self, album_id):
        """ Get all photos by album id """
        return self.request("GET", f"{self.endpoint}?albumId={album_id}")
    def create_photo(self, payload):
        """ Create a new album """
        self.logger.info("Creating photo")
        return self.request("POST", f"{self.endpoint}", json=payload)