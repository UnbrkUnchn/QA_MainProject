import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from FinalProject.base.base_class import Base

"""Страница Авторизации Яндекс Маркета"""

class Login_Page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Локаторы(Селекторы)

    login = "#passp-field-login"
    password = "#passp-field-passwd"
    login_button = "#passp\:sign-in"


    # Геттеры

    def get_login(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.login)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.password)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.login_button)))


    # Действия

    def input_login(self, email):
        self.get_login().send_keys(email)  # возможно сделать переключение принудительное на ввод почты
        print("Ввод Логина")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Ввод Пароля")

    def click_login_button(self):
        self.get_login_button().click()
        print("Нажатие на Кнопку: 'Вход'")


    # Методы

    def authorization(self):
        self.input_login("***")  # ЛОГИН ДЛЯ ВХОДА
        self.click_login_button()
        self.input_password("***")  # ПАРОЛЬ ДЛЯ ВХОДА
        self.click_login_button()
        time.sleep(3)
        self.get_current_url()
        self.assert_url("https://market.yandex.ru/?no-pda-redir=1&loggedin=1")
