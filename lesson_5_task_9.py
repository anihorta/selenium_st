import pytest
from selenium import webdriver


def login(driver):
    driver.find_element_by_name('username').send_keys('admin')
    driver.find_element_by_name('password').send_keys('admin')
    driver.find_element_by_name('login').click()


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_countries(driver):
    driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")
    login(driver)

    elems_text = []

    all = driver.find_elements_by_css_selector('[class=row]')

    for i in range(len(all)):
        elems = driver.find_elements_by_css_selector('[class=row]')
        elems_text.append(elems[i].find_element_by_css_selector('a').text)

        if int(elems[i].find_element_by_css_selector('[class=row] td:nth-child(6)').text) > 0:

            elems[i].find_element_by_css_selector('a').click()
            textes = []
            inner_elems = driver.find_elements_by_xpath('//*[@id = "table-zones"]//td[3]/*[@type="hidden"]/..')

            for inner_e in inner_elems:
                textes.append(inner_e.text)

            assert textes == sorted(textes)

            driver.back()

    assert elems_text == sorted(elems_text)


def test_geozones(driver):
    driver.get('http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones')
    login(driver)

    first_list = driver.find_elements_by_css_selector('[class=row]')

    for i in range(len(first_list)):
        elems = driver.find_elements_by_css_selector('[class=row]')
        elems[i].find_element_by_css_selector('a').click()

        inner_elems = driver.find_elements_by_css_selector('[id *= "table-zones"] td:nth-child(3) [selected]')
        textes = []
        for inn in inner_elems:
            textes.append(inn.text)
        assert textes == sorted(textes)
        driver.back()
