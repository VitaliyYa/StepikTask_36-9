'''
В файл test_items.py напишите тест, который проверяет, что страница товара на сайте содержит кнопку добавления в корзину.
Например, можно проверять товар, доступный по http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/.
'''

import time


link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_button_add_to_cart(browser): 
  browser.get(link)
  # time.sleep(30)
  button = browser.find_element_by_css_selector('button.btn-add-to-basket').get_attribute('value')
  assert button == 'Добавить в корзину' or 'Añadir al carrito' or 'Ajouter au panier', 'Add to cart button not found. (Кнопка добавления в корзину не найдена)'
