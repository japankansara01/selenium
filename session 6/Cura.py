#Test Case
# Open the URL- https://katalon-demo-cura.herokuapp.com/
# Click on the make appointment button
# Verify that URL Changes - assert
# time.sleep (3)
# Enter the username, password
# Next page verify the current URL
# Make appointment text on the web page.

import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

obj = Service(r"D:\japan_office\drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=obj)
driver.maximize_window()
driver.get("https://katalon-demo-cura.herokuapp.com/")

driver.find_element(By.ID,"btn-make-appointment").click()
assert "profile.php#login" in driver.current_url, "Url mismatch" #the last one is error msg #partial assertion link matching
print("Make appointment is clicked")
time.sleep(3)

# driver.find_element(By.ID,"txt-username").send_keys("John Doe")
# driver.find_element(By.ID,"txt-password").send_keys("ThisIsNotAPassword")
# driver.find_element(By.ID,"btn-login").click()
#
# assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment"
# print("Logged In")
#
# heading = driver.find_element(By.XPATH,"//*[@id='appointment']/div/div/div/h2")
# assert heading.text == "Make Appointment"
#
# # time.sleep(3) #checkpoint
# print("test case passed of appointment booking.")