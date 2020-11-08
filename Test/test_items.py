import time


def test_page_should_be_contain_button_add_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    #time.sleep(30)
    text_button = browser.find_element_by_css_selector("button.btn-add-to-basket").text
    print(text_button)

    button = browser.find_elements_by_css_selector("button.btn-add-to-basket")
    len_element_button = len(button)
    print(len_element_button)

    assert len_element_button == 1, \
        f" got {len_element_button} expected '1'"
