from selenium import webdriver
from constants.home_page_locator import *
import pytest
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService

@pytest.fixture(scope="function")
def setup(request, browser):
    if browser == "chrome":
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--incognito")
        driver = webdriver.Chrome(service=ChromeService(), options=chrome_options)
    elif browser == "edge":
        edge_options = EdgeOptions()
        edge_options.add_argument("--disable-notifications")
        edge_options.add_argument("--inprivate")
        driver = webdriver.Edge(service=EdgeService(), options=edge_options)
    elif browser == "firefox":
        firefox_options = FirefoxOptions()
        firefox_options.add_argument("--disable-notifications")
        firefox_options.add_argument("--private")
        driver = webdriver.Firefox(service=FirefoxService(), options=firefox_options)
    else:
        raise ValueError("Geçersiz tarayıcı seçimi! Lütfen 'chrome', 'edge' veya 'firefox' girin.")
    
    driver.maximize_window()
    driver.get(BASE_URL)
    request.cls.driver = driver
    yield
    driver.quit()

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Tarayıcı seçimi: chrome, edge veya firefox")

@pytest.fixture(scope="function")
def browser(request):
    return request.config.getoption("--browser")
