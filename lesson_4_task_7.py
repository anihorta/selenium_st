import pytest
from selenium import webdriver

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd

def test_example(driver):
    driver.get("http://localhost/litecart/admin/login.php")
    driver.find_element_by_name('username').send_keys('admin')
    driver.find_element_by_name('password').send_keys('admin')
    driver.find_element_by_name('login').click()

    c = driver.find_elements_by_css_selector('[id="app-"]')

    for i in range (len(c)):
        elems = driver.find_elements_by_css_selector('[id="app-"]')
        elems[i].click()
        assert(driver.find_elements_by_css_selector("h1"))
        elems = driver.find_elements_by_css_selector('[id="app-"]')
        in_elems = elems[i].find_elements_by_css_selector("li")

        for y in range (len(in_elems)):
            elems = driver.find_elements_by_css_selector('[id="app-"]')
            in_elems1 = elems[i].find_elements_by_css_selector("li")
            in_elems1[y].click()
            assert (driver.find_elements_by_css_selector("h1"))