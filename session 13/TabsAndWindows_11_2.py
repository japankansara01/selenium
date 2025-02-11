from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

obj = Service(r"D:\japan_office\drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=obj)
driver.maximize_window()

# Selenium 4 way to open new window
driver.get("https://practice-automation.com/form-fields/")
driver.switch_to.new_window('window')
driver.get("https://opensource-demo.orangehrmlive.com/")