import pytest


@pytest.fixture()
def set_up():
    print("Начало Теста")
    yield
    print("Конец Теста")

@pytest.fixture(scope="module")
def set_group():
    print("Начало тестирования группы")
    yield
    print("Конец тестирования группы")