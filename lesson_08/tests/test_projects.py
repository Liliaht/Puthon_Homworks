import pytest
from api.projects_api import ProjectsAPI


class TestProjectsAPI:
    """Тесты для API проектов Yougile"""
    
    # POSITIVE TESTS
    
    def test_create_project_positive(self, api_client):
        """Позитивный тест создания проекта"""
        projects_api = ProjectsAPI(api_client)
        
        project_data = {
            "title": "Test Project Positive",
            "description": "This is a test project created by API"
        }
        
        response = projects_api.create_project(**project_data)
        
        assert response.status_code == 201
        response_data = response.json()
        assert "id" in response_data
        assert response_data["title"] == project_data["title"]
        assert response_data["description"] == project_data["description"]
        
        # Очистка
        projects_api.delete_project(response_data["id"])
    
    def test_get_project_positive(self, api_client, created_project_id):
        """Позитивный тест получения проекта"""
        projects_api = ProjectsAPI(api_client)
        
        response = projects_api.get_project(created_project_id)
        
        assert response.status_code == 200
        response_data = response.json()
        assert response_data["id"] == created_project_id
        assert "title" in response_data
        assert "description" in response_data
    
    def test_update_project_positive(self, api_client, created_project_id):
        """Позитивный тест обновления проекта"""
        projects_api = ProjectsAPI(api_client)
        
        update_data = {
            "title": "Updated Project Title",
            "description": "Updated project description"
        }
        
        response = projects_api.update_project(created_project_id, **update_data)
        
        assert response.status_code == 200
        response_data = response.json()
        assert response_data["title"] == update_data["title"]
        assert response_data["description"] == update_data["description"]
        
        # Проверяем, что изменения сохранились
        get_response = projects_api.get_project(created_project_id)
        get_data = get_response.json()
        assert get_data["title"] == update_data["title"]
        assert get_data["description"] == update_data["description"]
    
    # NEGATIVE TESTS
    
    def test_create_project_negative_missing_title(self, api_client):
        """Негативный тест создания проекта без обязательного поля title"""
        projects_api = ProjectsAPI(api_client)
        
        project_data = {
            "description": "Project without title"
        }
        
        response = projects_api.create_project(**project_data)
        
        assert response.status_code == 400
        # Проверяем, что в ответе есть информация об ошибке
        response_data = response.json()
        assert "error" in response_data or "message" in response_data
    
    def test_get_project_negative_invalid_id(self, api_client):
        """Негативный тест получения проекта с несуществующим ID"""
        projects_api = ProjectsAPI(api_client)
        
        invalid_project_id = "invalid_id_12345"
        response = projects_api.get_project(invalid_project_id)
        
        # Ожидаем ошибку 404 или 400 для невалидного ID
        assert response.status_code in [400, 404]
    
    def test_update_project_negative_empty_title(self, api_client, created_project_id):
        """Негативный тест обновления проекта с пустым title"""
        projects_api = ProjectsAPI(api_client)
        
        update_data = {
            "title": "",  # Пустой title
            "description": "Valid description"
        }
        
        response = projects_api.update_project(created_project_id, **update_data)
        
        # Ожидаем ошибку, так как title не может быть пустым
        assert response.status_code == 400
    
    def test_update_project_negative_invalid_id(self, api_client):
        """Негативный тест обновления проекта с несуществующим ID"""
        projects_api = ProjectsAPI(api_client)
        
        invalid_project_id = "non_existing_project_id"
        update_data = {
            "title": "New Title",
            "description": "New Description"
        }
        
        response = projects_api.update_project(invalid_project_id, **update_data)
        
        # Ожидаем ошибку 404
        assert response.status_code == 404
    
    def test_create_project_negative_long_title(self, api_client):
        """Негативный тест создания проекта с слишком длинным названием"""
        projects_api = ProjectsAPI(api_client)
        
        # Создаем очень длинное название (предполагая ограничение в 255 символов)
        long_title = "A" * 1000
        
        project_data = {
            "title": long_title,
            "description": "Project with very long title"
        }
        
        response = projects_api.create_project(**project_data)
        
        # Ожидаем ошибку валидации
        assert response.status_code == 400
    
    def test_update_project_description_to_null(self, api_client, created_project_id):
        """Тест обновления описания проекта на null"""
        projects_api = ProjectsAPI(api_client)
        
        update_data = {
            "title": "Project with null description",
            "description": None  # Пытаемся установить описание в null
        }
        
        response = projects_api.update_project(created_project_id, **update_data)
        
        # Проверяем результат (может быть 200 или 400 в зависимости от API)
        if response.status_code == 200:
            response_data = response.json()
            assert response_data["description"] is None
        else:
            # Если API не поддерживает null для description
            assert response.status_code == 400