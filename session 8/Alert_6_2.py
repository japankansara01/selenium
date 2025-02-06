import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

obj = Service(r"D:\japan_office\drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=obj)
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/javascript_alerts")

driver.find_element(By.XPATH,"//*[@id='content']/div/ul/li[3]/button").click()
alertWin = driver.switch_to.alert
print(alertWin.text)
alertWin.send_keys("Hello")
# alertWin.accept()
alertWin.dismiss()

time.sleep(3)

print("Test case passed")