import datetime

from selenium.webdriver import ActionChains


class Base():
    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(driver)


    """Метод получения текущего URL"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print("Фактический URL: " + get_url)


    """Метод парсинга для сравнения текстовых значений"""

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Подтверждение Входа выполнено успешно")


    """Метод Создание Скриншота"""

    def get_screenshot(self):
        current_date = datetime.datetime.today().strftime("Date %d-%m-%y, Time %H-%M-%S")
        name_screenshot = 'Screenshot ' + current_date + '.png'
        self.driver.save_screenshot('/home/unbreakunchain/TestTools/PyCharm/FinalProject/screen/' + name_screenshot)
        print("Создан Скриншот Страницы: " + name_screenshot)


    """Метод Подтверждения URL"""

    def assert_url(self, result):
        try:
            get_url = self.driver.current_url
            assert get_url == result
            print("Подтверждён Ожидаемый URL")
        except AssertionError:
            print("Ошибка подтверждения")
