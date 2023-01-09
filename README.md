# Проект автоматизации тестирования интернет-магазина: [Яндекс.Маркет](https://market.yandex.ru/) #


## Общее Описание проекта: ##

Проект по Автоматизации Тестирования выполнен на языке Python 3.10.6, pytest 7.1.3, allure 3.11.1, на системе Linux Ubuntu 22.04.1 LTS в интегрированной среде разработки PyCharm 2022.2.3 (Community Edition), на Google Chrome версии 106.0.5249.119 (Официальная сборка), (64 бит)


### Общее Описание проекта: ###

Репозиторий содержит следующие директории и файлы:

* Директории base - содержит различные методы, pages - хранит классы страниц, screen - создаваемые скриншоты, tests - тесты, utilities  - логгирование.
* Директория resources - содержит chromedriver для Google Chrome и Selenium,
* Файл conftest.py - файл, содержащий некоторые параметры для pytest.

### Цель: ###

Провести тестирование авторизации и тестирование всего бизнес пути интернет-магазина на примере покупки товара с установленными фильтровыми значениями.


#### Шаги теста - test1.py: ####

##### 1. Тестирование Авторизации на Веб-сайте: #####

* Введение логина и пароля,
* Нажатие на кнопку "Вход",
* Подтверждение входа с помощью короткого кода, приходящего на номер телефона, привязанного к электронной почте,
* Проверка подтверждения входа в аккаунт, с помощью 'assert' текущего и фактического URL.

##### 2. Выбор продукта и прохождение всего бизнес пути (Выбор продукта - Добавление в Корзину - Покупка): #####

* Переход на страницу "Каталога",
* Выбор категории искомого продукта: "Ноутбуки и Персональные Компьютеры" -> "Ноутбуки",
* Переход на страницу "Фильтров" категории "Ноутбуки",
* Выборка некоторых фильтров, указанным для данного типа продукта,
* Выбор товара в соответствии с введёнными значениями фильтров и добавление его в "Корзину",
* Нажатие на кнопку "Корзина",
* Создание Скриншота Страницы "Корзины" с нашим товаром,
* (Условно)Успешное завершение теста.

##### 3. В тесте имеется собственная система логгирования и подключён Allure для вывода отчётов и удобства для работы с итоговыми результатами. #####


_Примечание: Так как автотест написан любительским образом для самообучения и демонстрации своих навыков работодателю, такие моменты веб-сайтов, как "Captcha" или "двух-факторная аутентификация", приходится проходить вручную, ибо я не имею доступа к тестовой среде площадки Яндекс.Маркета. Также, я не имею различных входных данных тестовых сценариев, данных тестового счёта и данных о клиенте. Поэтому некоторые этапы прохождения тестирования мне пришлось опустить, например вышеупомянутая: "Оплата Товара"_

Конарев Илья
