import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def delete_article(driver):
    wait = WebDriverWait(driver, 5)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[id="checkout-summary-wrapper"]')))

    elem = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '[name="cart_form"] [name="remove_cart_item"]')))
    elem.click()


def add_article(driver, count):
    driver.find_element_by_css_selector('.product').click()
    sel = driver.find_elements_by_css_selector('[name="options[Size]"]')
    if sel:
        sel = Select(sel[0])
        sel.select_by_index(1)
    driver.find_element_by_css_selector('[name="add_cart_product"]').click()
    wait = WebDriverWait(driver, 5)
    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#header .quantity'), str(count)))


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
    driver.get('http://litecart.stqa.ru/en/')
    driver.implicitly_wait(2)

    add_article(driver, 1)

    wait = WebDriverWait(driver, 5)
    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#header .quantity'), '1'))

    for i in range(2, 4):
        driver.back()
        add_article(driver, i)

    driver.find_element_by_css_selector('#cart .link').click()

    for i in range(3):

        if not driver.find_elements_by_xpath("//em[contains(text(),'no item')]"):
            delete_article(driver)
        else:
            break
