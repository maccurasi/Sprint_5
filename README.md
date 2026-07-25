# Автотесты Stellar Burgers

Фреймворк: pytest + Selenium WebDriver

## Установка
pip install -r requirements.txt

## Запуск
pytest tests/ -v

## Реализованные тесты

### Регистрация (test_registration.py)
- test_successful_registration — успешная регистрация
- test_registration_with_invalid_password — ошибка при коротком пароле

### Вход (test_login.py)
- test_login_from_main_page — вход через кнопку "Войти в аккаунт"
- test_login_from_personal_account — вход через "Личный кабинет"
- test_login_from_registration_form — вход через форму регистрации
- test_login_from_forgot_password_form — вход через форму восстановления пароля

### Личный кабинет (test_account.py)
- test_go_to_personal_account — переход в личный кабинет
- test_go_from_account_to_constructor_by_constructor_button — переход в конструктор через кнопку
- test_go_from_account_to_constructor_by_logo — переход в конструктор через логотип
- test_logout_from_personal_account — выход из аккаунта

### Конструктор (test_constructor.py)
- test_go_to_sauces_section — переход к разделу "Соусы"
- test_go_to_fillings_section — переход к разделу "Начинки"
- test_go_to_buns_section — переход к разделу "Булки"
