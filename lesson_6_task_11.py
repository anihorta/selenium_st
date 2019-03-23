import pytest
from selenium import webdriver
import datetime
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def logout(driver):
    driver.find_element_by_css_selector('[id="box-account"] [href*=logout]').click()


def login(driver, login, password):
    driver.find_element_by_css_selector('[name="email"]').send_keys(login)
    driver.find_element_by_css_selector('[name="password"]').send_keys(password + Keys.ENTER)


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    # wd = webdriver.Firefox()
    # wd = webdriver.Ie()

    request.addfinalizer(wd.quit)
    return wd


def test_example(driver):
    driver.get("http://litecart.stqa.ru")

    driver.find_element_by_css_selector('[id="box-account-login"] a').click()

    driver.find_element_by_css_selector('[name="firstname"]').send_keys('Nemo')
    driver.find_element_by_css_selector('[name="lastname"]').send_keys("O'Shey")
    driver.find_element_by_css_selector('[name="address1"]').send_keys("Moscow")
    driver.find_element_by_css_selector('[name="postcode"]').send_keys("12345")
    driver.find_element_by_css_selector('[name="city"]').send_keys('Moscow again')

    select = Select(driver.find_element_by_css_selector('[name="country_code"]'))
    select.select_by_visible_text('United States')

    import time
    time.sleep(2)
    wait = WebDriverWait(driver, 2)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[id="create-account"] select[name="zone_code"]')))

    select1 = Select(driver.find_element_by_css_selector('[id="create-account"] select[name="zone_code"]'))
    select1.select_by_visible_text('Alaska')

    email = 'test{}@test.com'.format(datetime.datetime.timestamp(datetime.datetime.now()))
    driver.find_element_by_css_selector('[name="email"]').send_keys(email)
    driver.find_element_by_css_selector('[name="phone"]').send_keys('9051234567')
    password = '123456'
    driver.find_element_by_css_selector('[name="password"]').send_keys(password)
    driver.find_element_by_css_selector('[name="confirmed_password"]').send_keys(password)

    driver.find_element_by_css_selector('[name="create_account"]').click()

    logout(driver)
    login(driver, email, password)
    logout(driver)
