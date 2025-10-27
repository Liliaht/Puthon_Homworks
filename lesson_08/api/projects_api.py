class ProjectsAPI:
    def __init__(self, api_client):
        self.api_client = api_client
    
    def create_project(self, title, description=None):
        """Создание проекта"""
        data = {"title": title}
        if description:
            data["description"] = description
        
        return self.api_client.post("/api-v2/projects", data)
    
    def get_project(self, project_id):
        """Получение проекта по ID"""
        return self.api_client.get(f"/api-v2/projects/{project_id}")
    
    def update_project(self, project_id, title=None, description=None):
        """Обновление проекта"""
        data = {}
        if title:
            data["title"] = title
        if description is not None:  # Позволяет установить пустое описание
            data["description"] = description
        
        return self.api_client.put(f"/api-v2/projects/{project_id}", data)
    
    def delete_project(self, project_id):
        """Удаление проекта"""
        return self.api_client.delete(f"/api-v2/projects/{project_id}")