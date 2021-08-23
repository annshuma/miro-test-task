import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", "-B", action="store", default="chrome", help="Please choose your browser")
    parser.addoption("--url", "-U", action="store", help="Please enter base url")
    parser.addoption("--path_to_browser_driver", "-P", action="store", help="Please enter path to browser driver")

@pytest.fixture(scope='session')
def url(request):
    return request.config.getoption("--url")


@pytest.fixture(scope='session')
def browser(request):
    """ Fixture for initialize browser """
    browser = request.config.getoption("--browser")
    driver_path = request.config.getoption("--path_to_browser_driver")
    if browser == "chrome":
        driver = webdriver.Chrome(driver_path)
    elif browser == "firefox":
        driver = webdriver.Firefox(driver_path)
    elif browser == "safari":
        driver = webdriver.Safari(driver_path)
    else:
        raise Exception(f"The browser {browser} is not supported!")
    driver.implicitly_wait(10)
    yield driver
    driver.quit()