from selenium import webdriver
from selenium.webdriver.chrome.service import Service

obj = Service(r"D:\japan_office\drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=obj)
driver.maximize_window()

driver.get("https://alianhub-beta-2lu4z.ondigitalocean.app/")

#Application Commands (diff in java)
print(driver.title)
print(driver.current_url)
print(driver.page_source)