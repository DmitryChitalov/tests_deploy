from selenium import webdriver
from pytest import fixture
from page.login_page import LoginPage
from test_data.data_provider import DataProvider
from configuration.config_provider import ConfigProvider

from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument("--headless")  # Запуск без графического интерфейса
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")


@fixture(autouse=True)
def driver(config):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.timeouts.implicit_wait = config.get_int("ui", "timeout_seconds")
    yield driver
    if driver is not None:
        driver.quit()


@fixture()
def login_page(driver, config):
    driver.get(config.get_int("ui", "url"))
    page = LoginPage(driver)
    yield page


# "session" - фикстура отрабатывает один раз, чтобы постоянно не извлекать данные из файла
@fixture(scope="session")
def test_data(config):
    file_name = config.get("test_data", "file_name")
    provider = DataProvider(file_name)
    return {"user": provider.get("user"), "pswrd": provider.get("pswrd")}


@fixture(scope="session")
def config():
    return ConfigProvider("test_config.ini")


@fixture()
def db(config):
    return config.get("db", "database")
