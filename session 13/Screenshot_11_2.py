import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

obj = Service(r"D:\japan_office\drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=obj)
driver.maximize_window()

driver.get("https://practice-automation.com/form-fields/")

driver.save_screenshot("D:/japan_office/feb/selenium/session 13/ss.png")
driver.save_screenshot(os.getcwd()+"ss2.png")
# driver.get_screenshot_as_base64()     (In binary format)

driver.quit()