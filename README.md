# Автотесты Stellar Burgers

Фреймворк: pytest + Selenium WebDriver

## Установка
pip install -r requirements.txt

## Запуск
pytest -v

## Реализованные тесты

### Регистрация (test_registration.py)
- test_register_success — успешная регистрация
- test_register_invalid_password — ошибка при коротком пароле

### Вход (test_login.py)
- test_login_via_main_button — вход через кнопку "Войти в аккаунт"
- test_login_via_personal_account — вход через "Личный кабинет"
- test_login_via_register_link — вход через форму регистрации
- test_login_via_forgot_password_link — вход через форму восстановления пароля

### Профиль (test_profile.py)
- test_go_to_personal_account — переход в личный кабинет
- test_go_to_constructor_from_profile — переход в конструктор из кабинета
- test_go_to_constructor_via_logo — переход в конструктор через логотип
- test_logout — выход из аккаунта

### Конструктор (test_constructor.py)
- test_go_to_buns_section — переход к разделу "Булки"
- test_go_to_sauces_section — переход к разделу "Соусы"
- test_go_to_fillings_section — переход к разделу "Начинки"
