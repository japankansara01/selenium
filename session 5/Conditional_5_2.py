from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By

obj = Service(r"D:\japan_office\drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=obj)
driver.maximize_window()
driver.get("https://alianhub-beta-2lu4z.ondigitalocean.app/")

# Conditional commands
label = driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div/div/div/div/form/div[1]/label")
print("Display Status:",label.is_displayed())

box = driver.find_element(By.XPATH,"//*[@id='email']")
print("Email is enabled:",box.is_enabled())

ch_box = driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div/div/div/div/form/div[3]/div/label")
print("Remember me is checked?:",ch_box.is_selected())
ch_box.click()
ch_box = driver.find_element(By.XPATH,"//*[@id='chk-remember-me']")
print("Remember me is checked?:",ch_box.is_selected())