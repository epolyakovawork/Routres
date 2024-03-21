import pytest
from selenium.common.exceptions import NoAlertPresentException # в начале файла
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

browser = webdriver.Chrome()
url1 = "https://app.routres.com/auth/login/"
browser.get(url1)
time.sleep(10)

loginfield = browser.find_element(By.XPATH,"/html/body/div/div/div/div/main/div/form/div[2]/div[1]/div[1]/div/input")
loginfield.send_keys("epolyakovawork@gmail.com")

passfield = browser.find_element(By.XPATH,"/html/body/div/div/div/div/main/div/form/div[2]/div[1]/div[2]/div/input")
passfield.send_keys("plmOn1234@")
button = browser.find_element(By.XPATH,"/html/body/div/div/div/div/main/div/form/div[2]/button")
button.click()
time.sleep(10)
browser.quit()
