import time

import pytest
from selenium import webdriver


from pages.login_page import Login_Page
from pages.main_page import Main_Page
from pages.catalog_page import Catalog_Page

from selenium.webdriver.chrome.options import Options


"""Шаги теста"""

"""Тест Полной Проверки Бизнес Логики YandexMarket"""

@pytest.mark.run(order=1)
def test_buy_product():
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path='/home/unbreakunchain/TestTools/PyCharm/resources/chromedriver', options=options)

    mp = Main_Page(driver)
    mp.start_test()
    mp.login_page()

    lp = Login_Page(driver)
    lp.authorization()

    mp.type_product()

    cp = Catalog_Page(driver)
    cp.choosing_product()

    time.sleep(120)

    driver.quit()

