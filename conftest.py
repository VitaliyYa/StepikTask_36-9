from selenium import webdriver
import pytest


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None, help="Choose language")


@pytest.fixture('function')
def browser(request):
    language = request.config.getoption("--language")
    browser = webdriver.Chrome()
    browser.implicitly_wait(3)
    browser.get("http://selenium1py.pythonanywhere.com/{}/catalogue/coders-at-work_207/".format(language))
    yield browser
    browser.quit()
