import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

obj = Service(r"D:\japan_office\drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=obj)
driver.maximize_window

driver.get("https://demo.automationtesting.in/FileUpload.html")

upload = driver.find_element(By.XPATH,"//*[@id='input-4']").send_keys("C:/Users/as-055/Downloads/test.pdf")

time.sleep(3)
print("Test case passed")