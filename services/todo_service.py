from services.base_service import BaseService


class TodoService(BaseService):
    def __init__(self):
        super().__init__()
        self.endpoint="/todos"

    def get_all_todos(self):
        """Gets a list of all todos."""
        return self.request("GET", self.endpoint)
    def get_todo_by_id(self,todo_id):
        """ Get a todo by id"""
        return self.request("GET", f"{self.endpoint}/{todo_id}")
    def get_todos_by_status(self,is_completed):
        """Gets a list of todos by status."""
        status = "true" if is_completed else "false"
        return self.request("GET", f"{self.endpoint}?completed={status}")
    def create_todo(self,payload):
        """ Create a new todo"""
        return self.request("POST", f"{self.endpoint}", json=payload)

