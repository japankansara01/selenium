import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

obj = Service(r"D:\japan_office\drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=obj)
driver.maximize_window()

driver.get("https://testautomationpractice.blogspot.com/")

# ------ JAVASCRIPT USED FOR SCROLLING ----------
# Scroll down by pixel
# driver.execute_script("window.scrollBy(0,500)", "")
# value = driver.execute_script("return window.pageYOffset;")
# print("Number of pixels moved:",value)

# Scroll down till element is visible
flag = driver.find_element(By.XPATH,"//*[@id='HTML15']/h2")
driver.execute_script("arguments[0].scrollIntoView();",flag)
value = driver.execute_script("return window.pageYOffset;")
print("Number of pixels moved:",value)

#Scroll page till end
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")

#Scroll page to starting position
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
print("Number of pixels moved:",value)

time.sleep(5)