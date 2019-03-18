import pytest
from selenium import webdriver

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd

def test_example(driver):
    driver.get("http://localhost/litecart")

    elems = driver.find_elements_by_css_selector('[class*="product column"]')
    for elem in elems:
        assert (elem.find_elements_by_css_selector('[class*="sticker"]'))