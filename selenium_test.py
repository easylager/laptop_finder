
from selenium import webdriver
import requests
from time import sleep
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

def get_number(url):

    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url=url)
    print(driver)
    button = driver.find_element(By.XPATH, "//div[@data_name='listings']")
    button.click()
    sleep(10)
    number = driver.find_element(By.XPATH, '//section').text.strip()
    return number

get_number(url='https://www.kufar.by/l/noutbuki?ot=1&query=ноутбуки&rgn=all')

