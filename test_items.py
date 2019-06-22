def test_btn_cart_present(browser):
    browser.get("http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/")

    from selenium.common.exceptions import NoSuchElementException
    try:
        button = browser.find_element_by_class_name("btn-add-to-basket")
    except NoSuchElementException:
        button = None

    assert button is not None, "Add to cart button is not present"
  