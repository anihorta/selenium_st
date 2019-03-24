import pytest
from selenium import webdriver
import datetime
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random
import os

def login_as_admin(driver):
    driver.find_element_by_name('username').send_keys('admin')
    driver.find_element_by_name('password').send_keys('admin')
    driver.find_element_by_name('login').click()


@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    # wd = webdriver.Firefox()
    # wd = webdriver.Ie()

    request.addfinalizer(wd.quit)
    return wd


def test_example(driver):
    driver.get('http://localhost/litecart/admin/')
    login_as_admin(driver)
    driver.find_element_by_css_selector("[id='box-apps-menu'] [href*=catalog]").click()
    driver.find_element_by_css_selector('[href*=edit_product]').click()

    name = 'Waren{}'.format(random.randint(1,100))

    driver.find_element_by_css_selector('[name="name[en]"]').send_keys(name)
    driver.find_element_by_css_selector('[name="code"]').send_keys(str(random.randint(999,9999)))
    driver.find_element_by_css_selector('[data-name="Rubber Ducks"]').click()
    driver.find_element_by_css_selector('[name="quantity"]').send_keys(str(random.randint(999, 9999)))

    path = os.path.abspath("detektiv_utochka.jpg")
    driver.find_element_by_css_selector('[name="new_images[]"]').send_keys(path)

    date = datetime.date.today()
    date_to = date + datetime.timedelta(days=5)
    elem = driver.find_element_by_css_selector('[name="date_valid_from"]')
    elem.send_keys(str(date.day)+str(date.month)+str(date.year))

    elem = driver.find_element_by_css_selector('[name="date_valid_to"]')
    elem.send_keys(str(date_to.day) + str(date_to.month) + str(date_to.year))

    # попытка заполнить поле с датой с помощью js
    # try: driver.execute_async_script("$('{}').datepicker('setDate', '{}');".format('[name="date_valid_from"]', '02.20.2002'))
    # except Exception: pass

    # вкладка information

    driver.find_element_by_css_selector('[class="tabs"] [href="#tab-information"]').click()
    select = Select(driver.find_element_by_css_selector('select[name="manufacturer_id"]'))
    select.select_by_index(1)
    driver.find_element_by_css_selector('[name="keywords"]').send_keys(str(random.randint(999, 9999)))
    driver.find_element_by_css_selector('[name="short_description[en]"]').send_keys(str(random.randint(999, 9999)))
    driver.find_element_by_css_selector('.input-wrapper .trumbowyg-editor').send_keys('отличный товар')
    driver.find_element_by_css_selector('[name="head_title[en]"]').send_keys(str(random.randint(999, 9999)))
    driver.find_element_by_css_selector('[name="meta_description[en]"]').send_keys(str(random.randint(999, 9999)))

    # вкладка prices

    driver.find_element_by_css_selector('[class="tabs"] [href="#tab-prices"]').click()
    driver.find_element_by_css_selector('[name="purchase_price"]').send_keys(str(random.randint(999, 9999)))
    select = Select(driver.find_element_by_css_selector('[name="purchase_price_currency_code"]'))
    select.select_by_index(1)
    driver.find_element_by_css_selector('[name="prices[USD]"]').send_keys(str(random.randint(999, 9999)))
    driver.find_element_by_css_selector('[name="prices[EUR]"]').send_keys(str(random.randint(999, 9999)))

    driver.find_element_by_css_selector('[name="save"]').click()

    # открываем каталог, проверяем, есть ли товар с нужным названием

    driver.find_element_by_css_selector("[id='box-apps-menu'] [href*=catalog]").click()
    assert driver.find_element_by_xpath('//*[@class="dataTable"] //a[contains(text(),"{}")]'.format(name))