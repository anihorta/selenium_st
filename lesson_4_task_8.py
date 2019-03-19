import pytest
from selenium import webdriver

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    # wd = webdriver.Firefox()
    # wd = webdriver.Ie()

    request.addfinalizer(wd.quit)
    return wd

def test_example(driver):
    driver.get("http://localhost/litecart")

    elems = driver.find_elements_by_css_selector('.product')
    for elem in elems:
        assert (len(elem.find_elements_by_css_selector('[class*="sticker"]')) == 1)