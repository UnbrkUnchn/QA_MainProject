
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from FinalProject.base.base_class import Base

"""Главная Страница Яндекс Маркета"""

class Main_Page(Base):

    url = 'https://market.yandex.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Локаторы(Селекторы)

    login_menu = "noindex div[data-zone-name='headerLoginButton']"
    search_field = "#header-search"
    catalog = "#catalogPopupButton"
    c_nbs_and_pc = "div ul li[data-zone-data='{\"id\":\"97009164\"}']"
    c_nbs = "li div a[data-tid='9f4dba48 a0dedf54 9b0f1b47']"


    # Геттеры

    def get_login_menu(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.login_menu)))

    def get_search_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.search_field)))

    def get_catalog(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.catalog)))

    def get_category_notebooks_and_pc(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.c_nbs_and_pc)))

    def get_category_notebooks(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.c_nbs)))


    # Действия

    def click_login_menu(self):
        self.get_login_menu().click()
        print("Нажатие на Кнопку: 'Меню Авторизации'")

    def click_catalog(self):
        self.get_catalog().click()
        print("Нажатие на Кнопку: 'Каталог'")

    def click_category_notebooks_and_pc(self):
        self.get_category_notebooks_and_pc().click()
        print("Нажатие на Кнопку: 'Ноутбуки и Компьютеры'")

    def click_category_notebooks(self):
        self.get_category_notebooks().click()
        print("Нажатие на Кнопку: 'Ноутбуки'")


    # Методы

    def start_test(self):
        self.driver.get(self.url)
        print("Открываем в браузере URL: " + self.url)
        self.driver.maximize_window()

    def login_page(self):
        self.click_login_menu()

    def type_product(self):
        self.click_catalog()
        self.click_category_notebooks_and_pc()
        self.click_category_notebooks()
