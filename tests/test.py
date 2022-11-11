
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.main_page import Main_Page
from pages.login_page import Login_Page
from pages.catalog_page import Catalog_Page
from pages.cart_page import Cart_Page


"""Шаги теста"""

"""Тест Полной Проверки Бизнес Логики YandexMarket"""

@pytest.mark.run(order=1)
def test_buy_product(set_up):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path='/home/unbreakunchain/Repo/resources/chromedriver', chrome_options=options)

    mp = Main_Page(driver)
    mp.start_test()
    mp.login_page()

    lp = Login_Page(driver)
    lp.authorization()

    mp.type_product()

    catalog_p = Catalog_Page(driver)
    catalog_p.choosing_product()

    cart_p = Cart_Page(driver)
    cart_p.buy_product()

    driver.quit()
