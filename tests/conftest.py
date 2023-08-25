import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope='function', autouse=True)
def config_browser():
    driver = webdriver.Chrome()
    browser.config.base_url = 'https://github.com'
