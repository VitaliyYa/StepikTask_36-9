import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help='Choose language: ru or en')

@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption('language')
    if language == "ru":
        print("\nstart chrome languages ru for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': 'ru'})
        browser = webdriver.Chrome(options=options)
    elif language == "es":
        print("\nstart chrome languages en for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': 'es'})
        browser = webdriver.Chrome(options=options)
    elif language == "fr":
        print("\nstart chrome languages en for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': 'fr'})
        browser = webdriver.Chrome(options=options)
    else:
        print("Browser {} still is not implemented".format(language))
    yield browser
    print("\nquit browser..")
    browser.quit()
