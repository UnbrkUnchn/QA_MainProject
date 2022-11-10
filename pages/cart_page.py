
from base.base_class import Base

"""Страница Корзины Яндекс Маркета"""

class Cart_Page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    def buy_product(self):
        self.get_current_url()
        self.assert_url("https://market.yandex.ru/my/cart")
        self.get_screenshot()
        print("Ноутбук куплен(Условно)")

        print("Тест успешно завершён!")
