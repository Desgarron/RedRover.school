from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest
from webdriver_manager.chrome import ChromeDriverManager


"""
Найдите кпопку c текстом "Gold". Попробуйте подобрать как минимум 2 разных XPATH и/или CSS-селекторов
http://suninjuly.github.io/xpath_examples
"""
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


def choose_element_xpath_page() -> None:
    browser.get(r'http://suninjuly.github.io/xpath_examples')
    n_1 = browser.find_element(By.XPATH, '//div[2]/button[3]')
    print('n_1 ==', n_1.text)
    n_2 = browser.find_element(By.XPATH, '//*[contains(text(), "Gold")]')
    print('n_2 ==', n_2.text)
    n_3 = browser.find_element(By.XPATH, '//*[text()="Gold"]')
    print('n_3 ==', n_3.text)
    n_4 = browser.find_element(By.CSS_SELECTOR, 'div:nth-child(2) button:nth-child(3)')
    print('n_4 ==', n_4.text)
    n_5 = browser.find_element(By.CSS_SELECTOR, 'div:nth-child(2) .btn:nth-child(3)')
    print('n_5 ==', n_5.text)
    n_6 = browser.find_element(By.CSS_SELECTOR, 'div:nth-child(2) button:nth-last-child(2)')
    print('n_6 ==', n_6.text)


"""Найдите элемент с текстом "Fully charged cat". Чем больше разных XPATH и/или CSS-селекторов сможете подобрать, тем лучше
http://suninjuly.github.io/cats.html"""


def choose_element_cats() -> None:
    browser.get('http://suninjuly.github.io/cats.html')
    n_1 = browser.find_element(By.CSS_SELECTOR, 'div:nth-child(5) > div > div > p')
    print('n_1 ==', n_1.text)
    n_2 = browser.find_element(By.CSS_SELECTOR, 'div:nth-last-child(2) > div > div > p')
    print('n_2 ==', n_2.text)
    n_3 = browser.find_element(By.XPATH, '//*[text()="Fully charged cat"]')
    print('n_3 ==', n_3.text)
    n_4 = browser.find_element(By.XPATH, '(//div)[29]/p')
    print('n_4 ==', n_4.text)
    n_5 = browser.find_element(By.XPATH, '(//p)[5]')
    print('n_5 ==', n_5.text)
    n_6 = browser.find_element(By.XPATH, "(//div[@class='card-body'])[5]/p")
    print('n_6 ==', n_6.text)
    n_7 = browser.find_element(By.CSS_SELECTOR, "div:nth-child(5) .card-text")
    print('n_7 ==', n_7.text)


if __name__ == '__main__':
    choose_element_xpath_page()
    choose_element_cats()
