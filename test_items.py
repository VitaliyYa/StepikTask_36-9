'''
В файл test_items.py напишите тест, который проверяет, что страница товара на сайте содержит кнопку добавления в корзину.
Например, можно проверять товар, доступный по http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/.
'''

import time


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_cart_button_presence(browser):
    browser.get(link)
    time.sleep(10)
    button = browser.find_element_by_css_selector('butеton.btn-add-to-basket')
    assert button
