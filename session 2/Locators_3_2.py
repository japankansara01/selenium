import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver

driver = webdriver.Chrome()
# driver = webdriver.Edge()
driver.maximize_window()

driver.get("https://demo.nopcommerce.com/")

# ID
# driver.find_element(By.ID,"small-searchterms").send_keys("Apple iPhone 15 128GB")
# driver.find_element(By.NAME,"q").send_keys("Apple iPhone 15 128GB")
#
# LINK TEXT
# driver.find_element(By.LINK_TEXT,"Register").click()
# driver.find_element(By.PARTIAL_LINK_TEXT,"Register").click()

# class name and find elements
# sliders = driver.find_elements(By.CLASS_NAME,"slidername")
# print((len)sliders)
links = driver.find_elements(By.TAG_NAME,"a")
print(len(links))

time.sleep(5)