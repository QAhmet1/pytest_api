from services.base_service import BaseService


class AlbumService(BaseService):
    def __init__(self):
        super().__init__()
        self.endpoint = "/albums"

    def get_all_albums(self):
        """ Get all albums """
        return self.request("GET", self.endpoint)

    def get_album_by_id(self, album_id):
        """ Get a specific album """
        return self.request("GET", f"{self.endpoint}/{album_id}")
    def get_album_by_user_id(self, user_id):
        """ Get a specific album """
        return self.request("GET", f"{self.endpoint}?userId={user_id}")
    def create_album(self, album):
        """ Create a new album """
        return self.request("POST", f"{self.endpoint}", json=album)