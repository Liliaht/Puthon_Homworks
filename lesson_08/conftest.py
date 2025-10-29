import pytest
import os
from api_client import APIClient
from pages.projects_api import ProjectsAPI


def pytest_addoption(parser):
    parser.addoption(
        "--base-url",
        action="store",
        default="https://yougile.com",
        help="Base URL for Yougile API"
    )
    parser.addoption(
        "--api-token",
        action="store",
        help="Yougile API token for authorization"
    )


@pytest.fixture
def api_client(request):
    """Фикстура для создания экземпляра API клиента"""
    base_url = request.config.getoption("--base-url")
    api_token = request.config.getoption("--api-token")
    
    # Получаем токен из параметров или переменных окружения
    if not api_token:
        api_token = os.getenv("YOUGILE_API_TOKEN")
    
    if not api_token:
        pytest.skip("API token not provided. Use --api-token or set YOUGILE_API_TOKEN environment variable")
    
    # Создаем экземпляр APIClient
    client = APIClient(base_url=base_url, token=api_token)
    
    yield client
    
    # Закрываем соединение после теста
    client.close()


@pytest.fixture
def unauthorized_api_client(request):
    """Фикстура для создания неавторизованного API клиента"""
    base_url = request.config.getoption("--base-url")
    
    # Создаем клиент без токена или с невалидным токеном
    client = APIClient(base_url=base_url, token="invalid_token")
    
    yield client
    
    client.close()


@pytest.fixture
def projects_api(api_client):
    """Фикстура для работы с API проектов"""
    return ProjectsAPI(api_client)


@pytest.fixture
def created_project(projects_api):
    """Фикстура создает тестовый проект и возвращает его ID"""
    import time
    
    response = projects_api.create_project(
        title=f"Test Project {int(time.time())}",
        description="This project was created for automated testing"
    )
    
    assert response.status_code == 201, "Failed to create test project"
    project_data = response.json()
    project_id = project_data.get("id")
    
    yield project_id
    
    # Очистка: пытаемся удалить созданный проект после теста
    try:
        projects_api.delete_project(project_id)
    except Exception:
        # Игнорируем ошибки при удалении
        pass