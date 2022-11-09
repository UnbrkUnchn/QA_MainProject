import time

from FinalProject.pages.login_page import Login_Page
from FinalProject.pages.main_page import Main_Page
from FinalProject.pages.catalog_page import Catalog_Page

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


"""Шаги теста"""

"""Тест Полной Проверки Бизнес Логики YandexMarket"""

@pytest.mark.run(order=1) # пайтест настроить фикстуру
def test_buy_product():
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome('/home/unbreakunchain/LocalGit/FinalProject/resources/chromedriver', options) # поменять путь без Локал Гита

    mp = Main_Page(driver)
    mp.start_test()
    mp.login_page()

    lp = Login_Page(driver)
    lp.authorization()

    mp.type_product()

    cp = Catalog_Page(driver)
    cp.choosing_product()

    time.sleep(120) #удалить потом

    driver.quit()

