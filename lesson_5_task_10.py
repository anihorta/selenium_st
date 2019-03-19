import pytest
from selenium import webdriver

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    # wd = webdriver.Firefox()
    # wd = webdriver.Ie()
    wd.get("http://localhost/litecart")

    request.addfinalizer(wd.quit)
    return wd

def test_example(driver):

    start_page = {}
    product_page = {}

    elem = driver.find_element_by_css_selector('[id =box-campaigns ] [class*="product column"]')
    r_price = elem.find_element_by_css_selector('[class="regular-price"]')
    c_price = elem.find_element_by_css_selector('[class="campaign-price"]')
    name = elem.find_element_by_css_selector('[class="name"]')

    start_page['r_price'] = r_price.text
    start_page['c_price'] = c_price.text
    start_page['name'] = name.text

    print(start_page)

    # проверка, что р цена серая
    color = (str(elem.find_element_by_css_selector('[class="regular-price"]').value_of_css_property('color')[5:-4]).split(','))
    assert(str(color[0])== str(color[1])== str(color[2]))