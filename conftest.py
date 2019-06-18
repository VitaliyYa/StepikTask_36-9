'''
Добавьте в файл conftest.py обработчик, который считывает из командной строки параметр language.
Реализуйте в файле conftest.py логику запуска браузера с указанным языком пользователя.
Браузер должен объявляться в фикстуре browser и передаваться в тест как параметр.
'''

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
  parser.addoption('--language', action='store', default='ru', help='Choose language: ru or es or fr')


@pytest.fixture(scope="function")
def browser(request):
  language = request.config.getoption('language')
  if language == "ru":
    print("\nStart chrome languages ru for test..")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': 'ru'})
    browser = webdriver.Chrome(options=options)
  elif language == "es":
    print("\nStart chrome languages en for test..")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': 'es'})
    browser = webdriver.Chrome(options=options)
  elif language == "fr":
    print("\nStart chrome languages en for test..")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': 'fr'})
    browser = webdriver.Chrome(options=options)
  else:
    print(f'Язык {language} не поддерживается. Выберите ru, es или fr.')
  yield browser
  print("\nQuit browser..")
  browser.quit()
