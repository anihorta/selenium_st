import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def there_and_back_again(driver: webdriver, element):
    now = driver.current_window_handle
    element.click()

    wait = WebDriverWait(driver, 5)
    wait.until(EC.number_of_windows_to_be(2))

    windows = driver.window_handles

    for i in windows:
        if i != now:
            driver.switch_to.window(i)

            driver.close()
            print('1: ', driver.window_handles)
            driver.switch_to.window(now)
            return


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


def test_windows(driver):
    driver.get('http://localhost/litecart/admin/?app=countries&doc=countries')
    login_as_admin(driver)
    driver.find_element_by_xpath('//*[@id = "content"] // td[7]').click()
    buttons = driver.find_elements_by_css_selector('[class="fa fa-external-link"]')

    for b in buttons:
        print(driver.current_window_handle)
        buttons = driver.find_elements_by_css_selector('[class="fa fa-external-link"]')
        there_and_back_again(driver, b)

    print(driver.window_handles)
    print(driver.current_window_handle)
