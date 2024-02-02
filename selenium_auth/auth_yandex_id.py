from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from config import url, login, pass_
'''
    Программа заходит на сайт https://passport.yandex.ru/auth/list, 
    вводит логин и пароль и нажимает кнопку "Войти".
    После нажатия на кнопку "Войти" программа закрывает браузер.
'''

def wait_element(browser, delay_seconds=1, by=By.TAG_NAME, value=None):
    return WebDriverWait(browser, delay_seconds).until(
        expected_conditions.presence_of_element_located((by, value))
    )


path = ChromeDriverManager().install()
browser_service = Service(executable_path=path)
browser = Chrome(service=browser_service)

def auth_func(wait_element, browser):
    email = wait_element(browser, by=By.ID, value='passp-field-login')
    email.clear()
    email.send_keys(login)
    email_button = wait_element(browser, by=By.ID, value='passp:sign-in').click()

    password = wait_element(browser, by=By.ID, value='passp-field-passwd')
    password.clear()
    password.send_keys(pass_)
    password_button = wait_element(browser, by=By.ID, value='passp:sign-in').click()

    return email, password

try:
    browser.get(url)

    auth_func(wait_element, browser)



finally:
    browser.close()