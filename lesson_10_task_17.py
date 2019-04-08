import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def login_as_admin(driver):
    driver.find_element_by_name('username').send_keys('admin')
    driver.find_element_by_name('password').send_keys('admin')
    driver.find_element_by_name('login').click()


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    # wd = webdriver.Firefox()
    # wd = webdriver.Ie()

    # caps = DesiredCapabilities.CHROME
    # caps['loggingPrefs'] = {'performance': 'ALL'}
    # wd = webdriver.Chrome(desired_capabilities=caps)

    request.addfinalizer(wd.quit)
    return wd


def test_logs(driver):
    driver.get('http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=1')
    login_as_admin(driver)
    waren = driver.find_elements_by_css_selector('[class="dataTable"] td:nth-child(3) [href*=product]')

    for i in range(len(waren)):
        waren = driver.find_elements_by_css_selector('[class="dataTable"] td:nth-child(3) [href*=product]')
        waren[i].click()
        assert not driver.get_log('browser')
        # print(driver.get_log('performance'))
        driver.back()

