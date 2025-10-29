import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


class APIClient:
    """
    Универсальный клиент для работы с API
    """
    
    def __init__(self, base_url, token=None):
        self.base_url = base_url
        self.session = requests.Session()
        
        # Настройка стратегии повторных попыток
        retry_strategy = Retry(
            total=3,
            backoff_factor=1,
            status_forcelist=[429, 500, 502, 503, 504],
        )
        
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("http://", adapter)
        self.session.mount("https://", adapter)
        
        # Установка базовых заголовков
        headers = {
            "Content-Type": "application/json",
            "User-Agent": "Python-API-Client/1.0"
        }
        
        # Добавляем авторизацию, если передан токен
        if token:
            headers["Authorization"] = f"Bearer {token}"
            
        self.session.headers.update(headers)
    
    def get(self, endpoint, params=None, **kwargs):
        """
        GET запрос к API
        """
        url = f"{self.base_url}{endpoint}"
        response = self.session.get(url, params=params, **kwargs)
        return response
    
    def post(self, endpoint, data=None, json=None, **kwargs):
        """
        POST запрос к API
        """
        url = f"{self.base_url}{endpoint}"
        response = self.session.post(url, data=data, json=json, **kwargs)
        return response
    
    def put(self, endpoint, data=None, json=None, **kwargs):
        """
        PUT запрос к API
        """
        url = f"{self.base_url}{endpoint}"
        response = self.session.put(url, data=data, json=json, **kwargs)
        return response
    
    def patch(self, endpoint, data=None, json=None, **kwargs):
        """
        PATCH запрос к API
        """
        url = f"{self.base_url}{endpoint}"
        response = self.session.patch(url, data=data, json=json, **kwargs)
        return response
    
    def delete(self, endpoint, **kwargs):
        """
        DELETE запрос к API
        """
        url = f"{self.base_url}{endpoint}"
        response = self.session.delete(url, **kwargs)
        return response
    
    def set_header(self, key, value):
        """
        Установка дополнительного заголовка
        """
        self.session.headers[key] = value
    
    def remove_header(self, key):
        """
        Удаление заголовка
        """
        if key in self.session.headers:
            del self.session.headers[key]
    
    def close(self):
        """
        Закрытие сессии
        """
        self.session.close()