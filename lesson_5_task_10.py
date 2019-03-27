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


def get_channel(rgba):
    rgba = rgba[rgba.find('(')+1:rgba.find(')')].split(',')
    ans = []
    for i in rgba[:3]:
        ans.append(int(i))
    return ans


def test_start_page(driver):
    elem = driver.find_element_by_css_selector('[id =box-campaigns ] [class*="product column"]')
    r_price = elem.find_element_by_css_selector('[class="regular-price"]')
    c_price = elem.find_element_by_css_selector('[class="campaign-price"]')

    # проверка, что р цена серая
    color = (str(r_price.value_of_css_property('color')))
    channels = get_channel(color)
    assert len(set(channels)) == 1

    # проверка, что р цена зачеркнутая
    lines = [r_price.value_of_css_property('text-decoration-line'), r_price.value_of_css_property('text-decoration')]
    assert 'line-through' in lines

    # проверка, что акционная цена красная
    color = str(c_price.value_of_css_property('color'))
    channels = get_channel(color)
    assert channels[1] == 0 and channels[2] == 0

    # проверка, что акционная цена жирная
    assert int(c_price.value_of_css_property('font-weight')) >= 700

    # проверка, что акционная цена крупнее
    assert float(c_price.value_of_css_property('font-size')[0:-2]) > float(
        r_price.value_of_css_property('font-size')[0:-2])


def test_product_page(driver):
    elem = driver.find_element_by_css_selector('[id =box-campaigns ] [class*="product column"]')

    elem.find_element_by_css_selector('a').click()

    elem = driver.find_element_by_css_selector('[id ="box-product"]')

    r_price = elem.find_element_by_css_selector(' [class="regular-price"]')
    c_price = elem.find_element_by_css_selector('[class="campaign-price"]')

    # проверка, что р цена серая
    color = (str(r_price.value_of_css_property('color')))
    channels = get_channel(color)
    assert len(set(channels)) == 1

    # проверка, что р цена зачеркнутая
    lines = [r_price.value_of_css_property('text-decoration-line'), r_price.value_of_css_property('text-decoration')]
    assert 'line-through' in lines

    # проверка, что акционная цена красная
    color = str(c_price.value_of_css_property('color'))
    channels = get_channel(color)
    assert channels[1] == 0 and channels[2] == 0

    # проверка, что акционная цена жирная
    assert int(c_price.value_of_css_property('font-weight')) >= 700

    # проверка, что акционная цена крупнее
    assert float(c_price.value_of_css_property('font-size')[0:-2]) > float(
        r_price.value_of_css_property('font-size')[0:-2])


def test_compare(driver):
    product_page = {}
    start_page = {}

    elem = driver.find_element_by_css_selector('[id =box-campaigns ] [class*="product column"]')

    r_price = elem.find_element_by_css_selector('[class="regular-price"]')
    c_price = elem.find_element_by_css_selector('[class="campaign-price"]')
    name = elem.find_element_by_css_selector('[class="name"]')

    start_page['r_price'] = r_price.text
    start_page['c_price'] = c_price.text
    start_page['name'] = name.text

    elem = driver.find_element_by_css_selector('[id =box-campaigns ] [class*="product column"]')
    elem.find_element_by_css_selector('a').click()
    elem = driver.find_element_by_css_selector('[id = box-product]')

    r_price = elem.find_element_by_css_selector(' [class="regular-price"]')
    c_price = elem.find_element_by_css_selector('[class="campaign-price"]')
    name = elem.find_element_by_css_selector('[itemprop="name"]')

    product_page['r_price'] = r_price.text
    product_page['c_price'] = c_price.text
    product_page['name'] = name.text

    assert product_page == start_page
