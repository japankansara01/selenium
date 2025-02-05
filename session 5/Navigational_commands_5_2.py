import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

obj = Service(r"D:\japan_office\drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=obj)
driver.maximize_window()
driver.get("https://alianhub-beta-2lu4z.ondigitalocean.app/")

link = driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div/div/div/div/form/div[5]/span/a").click()
time.sleep(2)

# Navigate to back page
driver.back()
time.sleep(2)

# Navigate to forward page from where we come
driver.forward()
time.sleep(2)

# refresh the webpage
driver.refresh()
time.sleep(3)

driver.quit()