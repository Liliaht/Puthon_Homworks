import pytest
import requests
from config import BASE_URL, API_TOKEN


@pytest.fixture
def auth_headers():
    """Фикстура для заголовков авторизации"""
    return {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json"
    }


@pytest.fixture
def api_client(auth_headers):
    """Фикстура для API клиента"""
    class APIClient:
        def __init__(self):
            self.base_url = BASE_URL
            self.headers = auth_headers
        
        def post(self, endpoint, data):
            return requests.post(f"{self.base_url}{endpoint}", json=data, headers=self.headers)
        
        def put(self, endpoint, data):
            return requests.put(f"{self.base_url}{endpoint}", json=data, headers=self.headers)
        
        def get(self, endpoint):
            return requests.get(f"{self.base_url}{endpoint}", headers=self.headers)
    
    return APIClient()


@pytest.fixture
def created_project_id(api_client):
    """Фикстура для создания проекта и получения его ID"""
    project_data = {
        "title": "Test Project for Fixture",
        "description": "Project created for testing purposes"
    }
    
    response = api_client.post("/api-v2/projects", project_data)
    assert response.status_code == 201
    project_id = response.json()["id"]
    
    yield project_id
    
    # Очистка - удаление проекта после теста
    api_client.delete(f"/api-v2/projects/{project_id}")