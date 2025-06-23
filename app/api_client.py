import requests

class APIClient:
    BASE_URL = "https://jsonplaceholder.typicode.com"  # публічний фейковий API

    def get_posts(self):
        """Отримати список усіх постів"""
        response = requests.get(f"{self.BASE_URL}/posts")
        response.raise_for_status()  # якщо 400/500 — викликає помилку
        return response.json()

    def get_post(self, post_id):
        """Отримати один пост за ID"""
        response = requests.get(f"{self.BASE_URL}/posts/{post_id}")
        if response.status_code == 404:
            return None
        response.raise_for_status()
        return response.json()
