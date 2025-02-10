import time
from selenium import webdriver
import os
location = os.getcwd()
from selenium.webdriver.common.by import By

def chrome_setup():
    from selenium.webdriver.chrome.service import Service
    obj = Service(r"D:\japan_office\drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
    preferences = {"download.default_directory":location}
    ops = webdriver.ChromeOptions()
    ops.add_experimental_option("prefs",preferences)
    driver = webdriver.Chrome(service=obj,options=ops)
    return driver

def Edge_setup():
    from selenium.webdriver.edge.service import Service
    obj = Service(r"D:\japan_office\drivers\edgedriver_win64\msedgedriver.exe")
    preferences = {"download.default_directory":location}
    ops = webdriver.EdgeOptions()
    ops.add_experimental_option("prefs",preferences)
    driver = webdriver.Edge(service=obj,options=ops)
    return driver

def Firefox_setup():
    from selenium.webdriver.firefox.service import Service
    obj = Service(r"D:\japan_office\drivers\geckodriver-v0.35.0-win64\geckodriver.exe")
    ops = webdriver.FirefoxOptions()
    ops.set_preference("browser.helperApps.neverAsk.saveToDisk","application/msword") #value is mimetype
    ops.set_preference("browser.download.manager.showWhenStarting",False)
    ops.set_preference("browser.download.folderList",2) # 0-desktop, 1-default download location, 2-desired location for download
    ops.set_preference("browser.download.dir",location)
    driver = webdriver.Firefox(service=obj,options=ops)
    return driver

# Automation
# driver = chrome_setup()
# driver = Edge_setup()
driver = Firefox_setup()
driver.maximize_window()
driver.get("https://practice-automation.com/file-download/")
driver.find_element(By.XPATH,"//*[@id='post-1042']/div/div[1]/div/div/div/div[3]/a").click()

time.sleep(3)
print("test case passed")
driver.quit()