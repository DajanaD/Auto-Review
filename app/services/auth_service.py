import httpx


class Auth:
    def __init__(self):
        # Можна ініціалізувати будь-які залежності тут
        pass

    def login(self, username: str, password: str):
        # Логіка авторизації користувача
        return {"username": username, "token": "fake-token"}

    def verify_token(self, token: str):
        # Логіка перевірки токену
        return True if token == "fake-token" else False
