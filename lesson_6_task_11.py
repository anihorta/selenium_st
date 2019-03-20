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

    driver.find_element_by_css_selector('[id="box-account-login"] a').click()

    driver.find_element_by_css_selector('[name="firstname"]').send_keys('Nemo')
    driver.find_element_by_css_selector('[name="lastname"]').send_keys("O'Shey")
    driver.find_element_by_css_selector('[name="address1"]').send_keys("Moscow")
    driver.find_element_by_css_selector('[name="postcode"]').send_keys("12345")
    driver.find_element_by_css_selector('[class="select2-selection__rendered"]').click()
    import time
    time.sleep(5)




