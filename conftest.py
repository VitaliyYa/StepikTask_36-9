'''
Добавьте в файл conftest.py обработчик, который считывает из командной строки параметр language.
Реализуйте в файле conftest.py логику запуска браузера с указанным языком пользователя.
Браузер должен объявляться в фикстуре browser и передаваться в тест как параметр.
'''

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
  parser.addoption('--language', action='store', default='ru',
  help='Choose language: ar ca cs da de el en es fi fr it ko nl pl pt pt-br ro ru sk uk zh-hans en-gb')


@pytest.fixture(scope="function")
def browser(request):
  languages = ['ar', 'ca', 'cs', 'da', 'de', 'el', 'en', 'es', 'fi', 'fr', 'it', 'ko', 'nl', 'pl', 'pt', 'pt-br', 'ro', 'ru', 'sk', 'uk', 'zh-hans', 'en-gb']
  language = request.config.getoption('language')
  if language in languages:
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(options=options)
  else:
    print(f'\nlanguage "{language}"" is not supported. Язык "{language}" не поддерживается.')
    print(f'Try: {", ".join(languages)}.')
  yield browser
  browser.quit()
