
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base
from utilities.logger import Logger

"""Страница Авторизации Яндекс Маркета"""

class Login_Page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Локаторы(Селекторы)

    login_menu = "div button[data-type='login']"
    login = "#passp-field-login"
    password = "#passp-field-passwd"
    sign_in_button = "#passp\:sign-in"


    # Геттеры

    def get_login_menu(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.login_menu)))

    def get_login(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.login)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.password)))

    def get_sign_in_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.sign_in_button)))


    # Действия

    def click_login_menu(self):
        self.get_login_menu().click()
        print("Нажатие на Кнопку: 'Почта'")

    def input_login(self, email):
        self.get_login().send_keys(email)
        print("Ввод Логина")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Ввод Пароля")

    def click_sign_in_button(self):
        self.get_sign_in_button().click()
        print("Нажатие на Кнопку: 'Вход'")


    # Методы

    def authorization(self):
        Logger.add_start_step(method="authorization")
        self.click_login_menu()
        self.input_login("***")  # ЛОГИН ДЛЯ ВХОДА
        self.click_sign_in_button()
        self.input_password("***")  # ПАРОЛЬ ДЛЯ ВХОДА
        self.click_sign_in_button()
        self.get_current_url()
        self.assert_url(
            "https://passport.yandex.ru/auth/welcome?origin=market_desktop_header"
            "&retpath=https%3A%2F%2Fmarket.yandex.ru%2F%3Fno-pda-redir%3D1%26loggedin%3D1")
        Logger.add_end_step(url=self.driver.current_url, method="authorization")
