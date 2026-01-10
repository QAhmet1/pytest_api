from services.base_service import BaseService


class CommentService(BaseService):
    def  __init__(self):
        super().__init__()
        self.endpoint = "/comments"

    def get_all_comments(self):
        """Sends a GET request to the /comments endpoint."""
        return self.request("GET", self.endpoint)
    def get_comment_by_id(self, comment_id):
        """Sends a GET request to the /comments/{comment_id} endpoint."""
        return self.request("GET", f"{self.endpoint}/{comment_id}")
    def get_comment_by_post_id(self, post_id):
        """Sends a GET request to the /comments/{post_id} endpoint."""
        return self.request("GET", f"{self.endpoint}?postId={post_id}")
    def create_comment(self,payload):
        """Sends a POST request to create a comment."""
        return self.request("POST", f"{self.endpoint}", json=payload)
    def update_comment_partially(self,comment_id,payload):
        """Sends a PATCH request to update a comment."""
        return self.request("PATCH", f"{self.endpoint}/{comment_id}", json=payload)
    def update_comment_fully(self,comment_id,payload):
        """Sends a PUT request to update a comment."""
        return self.request("PUT", f"{self.endpoint}/{comment_id}", json=payload)
    def delete_comment(self,comment_id):
        """Sends a DELETE request to delete a comment."""
        return self.request("DELETE", f"{self.endpoint}/{comment_id}")