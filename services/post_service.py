from services.base_service import BaseService


class PostService(BaseService):
    def __init__(self):
        super().__init__()
        self.endpoint="/posts"

    def get_all_posts(self):
        # Initializing the post endpoint
        return self.request('GET', self.endpoint)

    def get_post_by_id(self, post_id):
        return self.request('GET', self.endpoint+'/'+str(post_id))

    def create_post(self, post):
        return self.request('POST', self.endpoint, json=post)
    def update_post(self, post_id,payload):
        """Sends a PUT request to update an entire post."""
        return self.request('PUT', f"{self.endpoint}/{post_id}", json=payload)
    def partial_update_post(self, post_id,payload):
        """Sends a PATCH request to update an entire post."""
        return self.request('PATCH', f"{self.endpoint}/{post_id}", json=payload)
    def delete_post(self, post_id):
        """Sends a DELETE request to remove a post."""
        return self.request('DELETE', f"{self.endpoint}/{post_id}")
