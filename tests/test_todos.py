import allure
import pytest
from services.todo_service import TodoService
from utils.logger import get_logger

@allure.feature("Todos API Management")
class TestTodos:
    logger = get_logger()


    @pytest.fixture(scope="class")
    def todo_service(self):
        return TodoService()
    @allure.story("Get all comments")
    def test_get_all_todos_count(self, todo_service):
        """Verify that all todos are fetched successfully."""
        response = todo_service.get_all_todos()
        assert response.status_code == 200
        # Check if the list is not empty
        assert len(response.json()) > 0

    @pytest.mark.parametrize("todo_id, expected_status", [
        (1, False),  # Todo 1 is usually not completed in this API
        (4, True)  # Todo 4 is usually completed
    ])
    @allure.story("Get comments by status")
    def test_todo_completion_status(self, todo_service, todo_id, expected_status):
        """Verify the 'completed' field for specific todos."""
        response = todo_service.get_todo_by_id(todo_id)
        assert response.status_code == 200
        assert response.json()["completed"] == expected_status

    @allure.story("Get completed todos")
    def test_filter_completed_todos(self, todo_service):
        """Verify that filtering by completed=true only returns completed todos."""
        self.logger.info("Filtering todos by status: completed=true")
        response = todo_service.get_todos_by_status(True)

        assert response.status_code == 200
        todos = response.json()

        for todo in todos:
            # If this fails, Pytest will show which ID caused the failure
            assert todo["completed"] is True, f"Todo ID {todo['id']} is not completed!"
        self.logger.info(f"Verified {len(todos)} items are all completed.")

    @allure.story("Create a todo")
    def test_create_todo_check_types(self, todo_service):
        """Verify that a new todo can be created with correct data types."""
        payload = {
            "title": "Learn Pytest Schema Validation",
            "completed": False,
            "userId": 1
        }
        response = todo_service.create_todo(payload)

        assert response.status_code == 201
        data = response.json()
        # Verifying data types in the response
        assert isinstance(data["title"], str)
        assert isinstance(data["completed"], bool)