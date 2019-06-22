import pytest


# описываем аргумент командной строки
def pytest_addoption(parser):
    parser.addoption("--language", action="store", default=None, help="Choose user language")


@pytest.fixture(scope="function")
def browser(request):
    # считываем аргумент командной строк
    user_language = request.config.getoption("language")
    from selenium.webdriver.chrome.options import Options
    options = Options()
    options.add_experimental_option("prefs", {"intl.accept_languages": user_language})

    import os
    from selenium import webdriver
    print(os.path.abspath(os.path.join(os.getcwd(), os.pardir, "chromedriver.exe")))
    driver = webdriver.Chrome(executable_path=os.path.abspath(os.path.join(os.getcwd(), os.pardir, "chromedriver.exe")),
                              options=options)

    yield driver
    driver.quit()
