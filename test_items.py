# import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_guest_should_see_browser_language(browser): 
    browser.get(link)
    # time.sleep(30)
    #    Проверяем наличие самой кнопки селектором
    b1 = browser.find_element_by_class_name('btn-add-to-basket').get_attribute('value')
    #    Проверяем язык кнопки
    assert ((b1 == 'Добавить в корзину' or 'Añadir al carrito' or 'Ajouter au panier'), "Кнопка не найдена")
