
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base
from utilities.logger import Logger

"""Страница Каталога Яндекс Маркета"""

class Catalog_Page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.action = ActionChains(driver)


    # Локаторы(Селекторы)

    filtres_btn = "div a button[data-tid='423ef8ed']"  # Все Фильтры
    min_price = "section div[data-prefix='от'] input[value]"  # Минимальная Цена
    max_price = "section div[data-prefix='до'] input[value]"  # Максимальная Цена
    dd_condition = "div[data-filter-id='resale_goods'] button"  # Ниспадающее меню Кнопки
    condition = "div label[id='resale_new']"  # Состояние Товара
    notebook_name = "div label[id='152981']"  # Наименование Ноутбука
    dd_nb_series = "div[data-filter-id='12782797'] button"  # Ниспадающее меню Кнопки
    notebook_series = "div label[id='16100292']"  # Линейка
    dd_resolution = "div[data-filter-id='14806501'] button"  # Ниспадающее меню Кнопки
    resolution = "div label[id='36763152']"  # Разрешение Экрана
    dd_fresh_rate = "div[data-filter-id='16499888'] button"  # Ниспадающее меню Кнопки
    fresh_rate = "div label[id='37513490']"  # Частота Обновления Экрана
    dd_cpu = "div[data-filter-id='6069383'] button"  # Ниспадающее меню Кнопки
    cpu = "div label[id='22389489']"  # Процессор
    # dd_cpu_cores = "div[data-filter-id='34814810'] button"  # Ниспадающее меню Кнопки
    # cpu_cores = "div label[id='35692085']"  # Количество Ядер Процессора
    # dd_ram = "div[data-filter-id='15938685'] button"  # Ниспадающее меню Кнопки
    # ram = "div label[id='15938699']"  # Оперативная Память
    # dd_gpu = "div[data-filter-id='36036031'] button"  # Ниспадающее меню Кнопки
    # gpu = "div label[id='36427132']" # Видеокарта
    # dd_vram = "div[data-filter-id='17322770'] button"  # Ниспадающее меню Кнопки
    # vram = "div label[id='17324210']"  # Видеопамять
    dd_ssd = "div[data-filter-id='37699290'] button"  # Ниспадающее меню Кнопки
    ssd = "div label[id='39025848']"  # Общий объём накопителей SSD
    show_btn = "div a[class='_2qvOO _3qN-v _1Rc6L']"  # Показать предложения
    add_notebook = "[class='_1Jo-W cia-vs cia-cs'] [class*='_2CQi1 pvpsJ']"  #  селектор работает на 2 элемента
    cart = "div[data-apiary-widget-name='@market/CartEntryPoint']"  # Корзина


    # Геттеры

    def get_filtres_btn(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.filtres_btn)))

    def get_min_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.min_price)))

    def get_max_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.max_price)))

    def get_dd_condition(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.dd_condition)))

    def get_condition(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.condition)))

    def get_notebook_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.notebook_name)))

    def get_dd_notebook_series(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.dd_nb_series)))

    def get_notebook_series(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.notebook_series)))

    def get_dd_resolution(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.dd_resolution)))

    def get_resolution(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.resolution)))

    def get_dd_fresh_rate(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.dd_fresh_rate)))

    def get_fresh_rate(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.fresh_rate)))

    def get_dd_cpu(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.dd_cpu)))

    def get_cpu(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.cpu)))

    # def get_dd_cpu_cores(self):
    #     return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.dd_cpu_cores)))
    #
    # def get_cpu_cores(self):
    #     return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.cpu_cores)))
    #
    # def get_dd_ram(self):
    #     return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.dd_ram)))
    #
    # def get_ram(self):
    #     return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.ram)))
    #
    # def get_dd_gpu(self):
    #     return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.dd_gpu)))
    #
    # def get_gpu(self):
    #     return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.gpu)))
    #
    # def get_dd_vram(self):
    #     return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.dd_vram)))
    #
    # def get_vram(self):
    #     return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.vram)))

    def get_dd_ssd(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.dd_ssd)))

    def get_ssd(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.ssd)))

    def get_show_btn(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.show_btn)))

    def get_add_notebook(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.add_notebook)))

    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.cart)))


    # Действия

    def click_all_filtres_btn(self):
        self.get_filtres_btn().click()
        print("Нажатие на Кнопку: 'Все фильтры'")
        self.driver.refresh()
        print("Нажатие на Кнопку: 'Обновить Страницу'")

    def input_min_price(self, min_price):
        self.get_min_price().click()
        self.get_min_price().send_keys(min_price)
        print("Ввод: " + min_price)

    def input_max_price(self, max_price):
        self.get_max_price().click()
        self.get_max_price().send_keys(max_price)
        print("Ввод: " + max_price)

    def click_condition(self):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.get_dd_condition())
        self.get_dd_condition().click()
        print("Нажатие на Ниспадающее Меню: 'Состояние товара'")
        self.get_condition().click()
        print("Нажатие на Чек-бокс: 'Новое'")

    def click_notebook_name(self):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.get_notebook_name())
        self.get_notebook_name().click()
        print("Нажатие на Чек-бокс: 'Lenovo'")

    def click_notebook_series(self):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.get_dd_notebook_series())
        self.get_dd_notebook_series().click()
        print("Нажатие на Ниспадающее Меню: 'Линейка'")
        self.get_notebook_series().click()
        print("Нажатие на Чек-бокс: 'Legion'")

    def click_resolution(self):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.get_dd_resolution())
        self.get_dd_resolution().click()
        print("Нажатие на Ниспадающее Меню: 'Разрешение экрана'")
        self.get_resolution().click()
        print("Нажатие на Чек-бокс: '1920x1080'")

    def click_fresh_rate(self):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.get_dd_fresh_rate())
        self.get_dd_fresh_rate().click()
        print("Нажатие на Ниспадающее Меню: 'Частота обновления экрана'")
        self.get_fresh_rate().click()
        print("Нажатие на Чек-бокс: '165 Гц'")

    def click_cpu(self):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.get_dd_cpu())
        self.get_dd_cpu().click()
        print("Нажатие на Ниспадающее Меню: 'Процессор'")
        self.get_cpu().click()
        print("Нажатие на Чек-бокс: 'Intel Core i7 11800H'")

    # def click_cpu_cores(self):
    #     self.driver.execute_script("arguments[0].scrollIntoView();", self.get_dd_cpu_cores())
    #     self.get_dd_cpu_cores().click()
    #     print("Нажатие на Ниспадающее Меню: 'Количество ядер процессора'")
    #     self.get_cpu_cores().click()
    #     print("Нажатие на Чек-бокс: '8 ядер'")

    # def click_ram(self):
    #     self.driver.execute_script("arguments[0].scrollIntoView();", self.get_dd_ram())
    #     self.get_dd_ram().click()
    #     print("Нажатие на Ниспадающее Меню: 'Оперативная память'")
    #     self.get_ram().click()
    #     print("Нажатие на Чек-бокс: '16 Гб ОЗУ'")

    # def click_gpu(self):
    #     self.driver.execute_script("arguments[0].scrollIntoView();", self.get_dd_gpu())
    #     self.get_dd_gpu().click()
    #     print("Нажатие на Ниспадающее Меню: 'Видеокарта'")
    #     self.get_gpu().click()
    #     print("Нажатие на Чек-бокс: 'NVIDIA GeForce RTX 3070'")

    # def click_vram(self):
    #     self.driver.execute_script("arguments[0].scrollIntoView();", self.get_dd_vram())
    #     self.get_dd_vram().click()
    #     print("Нажатие на Ниспадающее Меню: 'Видеопамять'")
    #     self.get_vram().click()
    #     print("Нажатие на Чек-бокс: '8 Гб Видеопамяти'")

    def click_ssd(self):
        self.driver.execute_script("arguments[0].scrollIntoView();", self.get_dd_ssd())
        self.get_dd_ssd().click()
        print("Нажатие на Ниспадающее Меню: 'Общий объём накопителей SSD'")
        self.get_ssd().click()
        print("Нажатие на Чек-бокс: 'SSD 512 Гб'")

    def click_show_btn(self):
        self.get_show_btn().click()
        print("Нажатие на Кнопку: 'Показать продукты'")

    def click_add_notebook(self):
        self.get_add_notebook().click()
        print("Нажатие на Кнопку: 'Добавить в Корзину'")

    def click_cart(self):
        self.get_cart().click()
        print("Переход на Страницу: 'Корзина'")


    # Методы

    def choosing_product(self):
        Logger.add_start_step(method="choosing_product")
        self.click_all_filtres_btn()
        self.input_min_price("150000")
        self.input_max_price("200000")
        self.click_condition()
        self.click_notebook_name()
        self.click_notebook_series()
        self.click_resolution()
        self.click_fresh_rate()
        self.click_cpu()
        # self.click_cpu_cores()
        # self.click_ram()
        # self.click_gpu()
        # self.click_vram()
        self.click_ssd()
        self.click_show_btn()
        self.click_add_notebook()
        self.click_cart()
        Logger.add_end_step(url=self.driver.current_url, method="choosing_product")
