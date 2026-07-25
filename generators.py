import random
import string

def generate_email():
    """
    Генерирует уникальный email в формате:
    amanbek_bekbolat_49_123@yandex.ru
    """
    return f"amanbek_bekbolat_49_{random.randint(100, 999)}@yandex.ru"

def generate_password(length=8):
    """
    Генерирует случайный пароль длиной не менее 6 символов.
    """
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))
