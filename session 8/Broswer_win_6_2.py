import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

obj = Service(r"D:\japan_office\drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=obj)
driver.maximize_window()

driver.get("https://alianhub-beta-2lu4z.ondigitalocean.app/")

link = driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div/div/div/div/form/div[5]/span/a")
link.send_keys(Keys.CONTROL + Keys.RETURN)

# Return single window id
# windowId = driver.current_window_handle
# print(windowId)

windowIds = driver.window_handles
parentWin = windowIds[0]
childWin = windowIds[1]

ParentTitle = driver.title

driver.switch_to.window(childWin)

# Approach 2
for winId in windowIds:
    driver.switch_to.window(winId)
    print(driver.title)

# To select particular window
for winId in windowIds:
    driver.switch_to.window(winId)
    if driver.title == "Alian Hub | Login":
        driver.close()

print(f"Parent window is closed which title is {ParentTitle}")

# time.sleep(2)
print("Test case passed")