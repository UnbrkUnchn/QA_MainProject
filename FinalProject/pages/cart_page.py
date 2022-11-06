from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base


"""Страница Корзины Яндекс Маркета"""

class Cart_Page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Локаторы(Селекторы)

    final_name = "div a[data-tid*='ab65e805']"
    final_price = "div[data-tid='cbc72d33']"
    final_quantity = "div[data-auto='offerAmountCounter']"
    arrange_product = "span button[data-tid*='9e5e2c0d']"

    # Геттеры

    def get_final_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.final_name)))

    def get_final_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.final_price)))

    def get_final_quantity(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.final_quantity)))

    def get_arrange_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.arrange_product)))


    # Действия

    def click_arrange_product(self):
        self.get_arrange_product().click()
        print("Нажатие на Кнопку: 'Оформить Покупку'")


    # Методы

    def buy_product(self):
        self.assert_word(self.get_final_price, "178000")
        self.assert_word(self.get_final_quantity, "1")
        self.click_arrange_product()
