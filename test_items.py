def test_find_button_add_to_basket(browser):
    btn = browser.find_elements_by_class_name("btn-add-to-basket")
    assert len(btn) > 0, "Element not found"
