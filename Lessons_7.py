"""As a User, I want to login to my personal user account to manage private information, get Access Key
  and see my payment status

  Acceptance criteria #1
  GIVEN User has registered account
  WHEN User enter correct email AND password AND click button Submit
  THEN User get access to personal account

  Acceptance criteria #2
  GIVEN User has registered account
  WHEN User enter correct email AND incorrect password AND click button Submit
  THEN User receive Alert that information is incorrect

  Acceptance criteria #3
  GIVEN User has registered account
  WHEN User forgot password you can click button and enter email to recover it
  THEN User receive letter to email with instructions
  """

import time
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
EMAIL = 'nahornyi.y+1@gmail.com'
PASSWORD = 'Devil2421711'


def test_open_sign_in_page():
    driver.get('https://openweathermap.org/')
    button = driver.find_element(By.LINK_TEXT, "Sign in")
    driver.execute_script("arguments[0].click();", button)


def test_false_login():
    driver.implicitly_wait(2)
    driver.find_element(By.CSS_SELECTOR, ".input-group > input[type='email']").send_keys(EMAIL)
    driver.find_element(By.CSS_SELECTOR, ".input-group > input[type='password']").send_keys('qwe')
    driver.find_element(By.CSS_SELECTOR, "input[value='Submit']").click()

    alert_title = driver.find_element(By.CSS_SELECTOR, ".panel.panel-red > .panel-heading").text
    alert_text = driver.find_element(By.CSS_SELECTOR, ".panel.panel-red > .panel-body").text

    assert alert_title == 'Alert'
    assert alert_text == 'Invalid Email or password.'


def test_success_recovery_password():
    driver.implicitly_wait(3)
    driver.find_element(By.CSS_SELECTOR, ".pwd-lost-q > a").click()
    input_email = driver.find_element(By.CSS_SELECTOR, ".form-group.email.optional.user_email > input")

    assert driver.find_element(By.CSS_SELECTOR, '.text-muted').text == \
           'Enter your email address and we will send you a link to reset your password.'
    assert input_email.get_attribute('placeholder') == 'Enter email'

    if not input_email.get_attribute('value'):
        print("\nDon't have email in forgot password input email field")
        input_email.send_keys(EMAIL)

    driver.find_element(By.CSS_SELECTOR, "[value='Send']").click()

    success_title = driver.find_element(By.CSS_SELECTOR, '.panel.panel-green > .panel-heading')
    success_text = driver.find_element(By.CSS_SELECTOR, ".panel.panel-green >.panel-body")
    button_close = driver.find_element(By.CSS_SELECTOR, ".panel.panel-green >.panel-heading > button")

    assert success_title.text == 'x\nNotice'
    assert button_close.text == 'x'
    assert success_text.text == \
           'You will receive an email with instructions on how to reset your password in a few minutes.'
    button_close.click()


def test_success_login():
    driver.get('https://home.openweathermap.org/users/sign_in')
    assert driver.current_url == 'https://home.openweathermap.org/users/sign_in'
    driver.find_element(By.CSS_SELECTOR, ".input-group > input[type='email']").send_keys(EMAIL)
    driver.find_element(By.CSS_SELECTOR, ".input-group > input[type='password']").send_keys(PASSWORD)
    driver.find_element(By.CSS_SELECTOR, "input[value='Submit']").click()
