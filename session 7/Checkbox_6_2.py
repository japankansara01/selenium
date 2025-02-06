import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

obj = Service(r"D:\japan_office\drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=obj)
driver.maximize_window()

driver.get("https://practice-automation.com/form-fields/")

check_box = driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains=(@id='drink')]")
print(len(check_box))

# select all checkbox
for i in range(len(check_box)):
    check_box[i].click()

# select custom multiple checkboxes
for checkbox in check_box:
    tick = checkbox.get_attribute('value')
    if tick=='Coffee' or tick=='Wine':
        checkbox.click()

# time.sleep(3)
print("Test case passed.")