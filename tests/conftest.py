import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url = 'https://demoqa.com/automation-practice-form'
    browser.config.timeout = 2.0
    browser.config.window_width = 1200
    browser.config.window_height = 1080

#    browser.config.type_by_js = True

#    driver_options = webdriver.ChromeOptions()
#    driver_options.add_argument('--headless=new')
#    browser.config.driver_options = driver_options

    yield

    browser.quit()