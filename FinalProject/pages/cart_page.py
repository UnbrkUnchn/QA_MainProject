# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait

from FinalProject.base.base_class import Base

"""Страница Корзины Яндекс Маркета"""

class Cart_Page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Локаторы(Селекторы)


    # Геттеры


    # Действия


    # Методы

    def buy_product(self):
        self.get_current_url()
        self.assert_url("https://market.yandex.ru/my/cart")
        self.get_screenshot()
        print("Ноутбук куплен(Условно)")

        print("Тест успешно завершён!")
