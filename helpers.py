import random
import string

def generate_email():
    random_digits = str(random.randint(10000, 99999))
    return f"bekbolat_test_{random_digits}@yandex.ru"

def generate_password():
    return "Test" + "".join(random.choices(string.digits, k=6))
