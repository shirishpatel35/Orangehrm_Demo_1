import pytest
from selenium import webdriver


# @pytest.fixture
# def setup():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
#     return driver


#------------------------------------------
# when we wants wants to run testcases in multiple browser
# if browser not found then all testcases run in headless mode

# def pytest_addoption(parser):
#     parser.addoption("--browser")
#
#
# @pytest.fixture()
# def browser(request):
#     return request.config.getoption("--browser")
#
# @pytest.fixture()
# def setup(browser):
#     if browser == 'chrome':
#         driver = webdriver.Chrome()
#         print("opening chrome browser")
#     elif browser == 'Edge':
#         driver = webdriver.Edge()
#         print("opening Edge Browser")
#     elif browser == 'Firefox':
#         driver = webdriver.Firefox()
#         print("Opening Firefox browser")
#     else:
#         print("headless mode")
#         chrome_options= webdriver.ChromeOptions()
#         chrome_options.add_argument("headless")
#         driver = webdriver.Chrome(options=chrome_options)
#     driver.maximize_window()
#     return driver


#--------------------------------------------------------------
# when we wants wants to run testcases in multiple browser
# if browser not found then all testcases run in chrome(default)


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture()
def setup(browser):
    if browser == 'Edge':
        driver = webdriver.Edge()
        print("opening Edge Browser")
    elif browser == 'Firefox':
        driver = webdriver.Firefox()
        print("Opening Firefox browser")
    else:
        driver = webdriver.Chrome()
        print("opening chrome browser")
    driver.maximize_window()
    return driver



@pytest.fixture(params=[
    ("Admin","admin123","Pass"),
    ("Admin12","admin123","Fail"),
    ("Admin","admin321","Fail"),
    ("Admin123","admin321","Fail")
])

def getDataForLogin(request):
    return request.param