import pytest
import time
from api_client import APIClient


class TestProjectsAPI:
    """Тесты для API проектов Yougile"""
    
    # POSITIVE TESTS
    
    def test_create_project_positive(self, projects_api):
        """Позитивный тест создания проекта с валидными данными"""
        project_data = {
            "title": f"Auto Test Project {int(time.time())}",
            "description": "Project created by automated test"
        }
        
        response = projects_api.create_project(
            title=project_data["title"],
            description=project_data["description"]
        )
        
        assert response.status_code == 201
        response_data = response.json()
        
        assert "id" in response_data
        assert response_data["title"] == project_data["title"]
        assert response_data["description"] == project_data["description"]
    
    def test_get_project_positive(self, projects_api, created_project):
        """Позитивный тест получения проекта по ID"""
        response = projects_api.get_project(created_project)
        
        assert response.status_code == 200
        response_data = response.json()
        
        assert response_data["id"] == created_project
        assert "title" in response_data
        assert "description" in response_data
    
    def test_update_project_positive(self, projects_api, created_project):
        """Позитивный тест обновления проекта"""
        new_title = f"Updated Project {int(time.time())}"
        new_description = "Updated description"
        
        response = projects_api.update_project(
            project_id=created_project,
            title=new_title,
            description=new_description
        )
        
        assert response.status_code == 200
        
        # Проверяем, что изменения применились
        get_response = projects_api.get_project(created_project)
        project_data = get_response.json()
        
        assert project_data["title"] == new_title
        assert project_data["description"] == new_description
    
    # NEGATIVE TESTS
    
    def test_create_project_negative_missing_title(self, projects_api):
        """Негативный тест создания проекта без обязательного поля title"""
        response = projects_api.create_project(title="")
        assert response.status_code == 400
    
    def test_get_project_negative_invalid_id(self, projects_api):
        """Негативный тест получения проекта с несуществующим ID"""
        response = projects_api.get_project("invalid_id_12345")
        assert response.status_code in [400, 404]
    
    def test_update_project_negative_invalid_id(self, projects_api):
        """Негативный тест обновления проекта с несуществующим ID"""
        response = projects_api.update_project(
            project_id="invalid_id_12345",
            title="New Title"
        )
        assert response.status_code in [400, 404]


class TestProjectsAuthorization:
    """Тесты авторизации для API проектов"""
    
    def test_create_project_unauthorized(self, unauthorized_api_client):
        """Тест создания проекта без авторизации"""
        from pages.projects_api import ProjectsAPI
        
        projects_api = ProjectsAPI(unauthorized_api_client)
        response = projects_api.create_project(title="Test Project")
        
        assert response.status_code == 401