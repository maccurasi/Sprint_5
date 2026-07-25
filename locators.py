from selenium.webdriver.common.by import By

class MainPageLocators:
    # Кнопка «Войти в аккаунт»
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    # Кнопка «Личный кабинет»
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[contains(text(),'Личный')]")
    # Кнопка «Конструктор»
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    # Логотип Stellar Burgers
    LOGO = (By.XPATH, "//a[@href='/']")
    # Вкладка «Булки»
    BUNS_TAB = (By.XPATH, "//span[text()='Булки']")
    # Вкладка «Соусы»
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']")
    # Вкладка «Начинки»
    FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']")
    # Активная вкладка конструктора
    ACTIVE_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]")

class LoginPageLocators:
    # Поле Email
    EMAIL_INPUT = (By.NAME, "name")
    # Поле Пароль
    PASSWORD_INPUT = (By.NAME, "Пароль")
    # Кнопка «Войти»
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    # Ссылка «Зарегистрироваться»
    REGISTER_LINK = (By.XPATH, "//a[text()='Зарегистрироваться']")
    # Ссылка «Восстановить пароль»
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")
    # Заголовок «Вход»
    TITLE = (By.CSS_SELECTOR, ".auth-form__title")

class RegisterPageLocators:
    # Поле Имя
    NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
    # Поле Email
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    # Поле Пароль
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    # Кнопка «Зарегистрироваться»
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    # Ссылка «Войти»
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")
    # Ошибка «Некорректный пароль»
    INCORRECT_PASSWORD = (By.XPATH, "//p[text()='Некорректный пароль']")

class ProfilePageLocators:
    # Кнопка «Выход»
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
