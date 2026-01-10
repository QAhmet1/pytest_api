
# 🚀 Python API Test Automation Framework

This project is a professional-grade API testing framework built with **Python**, **Pytest**, and **Allure Reports**. It provides full coverage for the [JSONPlaceholder](https://jsonplaceholder.typicode.com/) fake online REST API.

---

## 🏗️ Project Structure

The framework follows a modular Page Object Model (POM) like structure adapted for API testing, ensuring high maintainability and scalability.

```text
API_Framework/
├── allure-results/     # Temporary folder for Allure report data
├── services/           # Service layer for different API endpoints
│   ├── base_service.py     # Core request handler (wraps requests library)
│   ├── user_service.py     # User-related API calls
│   ├── post_service.py     # Post-related API calls
│   ├── comment_service.py  # Comment-related API calls
│   ├── todo_service.py     # Todo-related API calls
│   ├── album_service.py    # Album-related API calls
│   └── photo_service.py    # Photo-related API calls
├── tests/              # Test suites categorized by service
│   ├── test_users.py
│   ├── test_posts.py
│   └── ... (others)
├── utils/              # Helper utilities
│   ├── config_reader.py    # Config.ini file reader
│   └── logger.py           # Custom logging configuration
├── config.ini          # Base URL and environment settings
├── requirements.txt    # Project dependencies
└── api_tests.log       # Runtime execution logs


🛠️ Prerequisites
Python 3.10+

Java 8+ (Required for Allure Report)

Allure Command Line Tool (Can be installed via brew install allure on macOS or manually on Windows)

📥 Installation
Clone the repository:
git clone <repository-url>
cd API_Framework

2. Create and activate a virtual environment:
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

3. Install dependencies:
pip install -r requirements.txt

🧪 Running Tests
1. Run All Tests
To execute the entire test suite:
pytest tests/ -v -s

2. Run Specific Test Suites
pytest tests/test_posts.py -v
pytest tests/test_users.py -v

3. Generate Allure Report
Run tests with Allure results enabled:
pytest tests/ --alluredir=allure-results

4. View the generated report:
allure serve allure-results


📊 Coverage and Features
The framework currently provides ~100% endpoint coverage for the JSONPlaceholder API:

Users: Profile data validation, status code checks.

Posts: CRUD operations, filtering by UserID.

Comments: Relational integrity checks, email format validation.

Todos: Completion status filtering (Boolean logic).

Albums & Photos: Relation mapping and URL format verification.

Key Framework Features:
Modular Architecture: Isolated service and test layers.

Data-Driven Testing: Using @pytest.mark.parametrize for multiple data sets.

Logging: Detailed request/response logs stored in api_tests.log.

Reporting: Interactive HTML reports with Allure featuring Story/Feature grouping.

Robust Error Handling: Centralized request management in BaseService.

🔧 Configuration
You can change the base_url or other environment-specific variables in the config.ini file:
[API]
base_url = [https://jsonplaceholder.typicode.com](https://jsonplaceholder.typicode.com)
