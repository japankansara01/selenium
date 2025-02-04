# partial xpath and full xpath
# xpath with "or & and" operator
# xpath with starts-with(), contains(), text()

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

obj = Service(r"D:\japan_office\drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=obj)
driver.maximize_window()

driver.get("https://demo.alianhub.com/")

email = driver.find_element(By.XPATH,"//*[@id='email']") #Partial XPath
email.clear()
email.send_keys("owner@example.com")

password = driver.find_element(By.XPATH,"/html/body/div/div[1]/div/div/div/div/div/form/div[2]/input") #Full XPath
password.clear()
password.send_keys("Abc@1234")
print("Test Case 1 Passed")

email = driver.find_element(By.XPATH,"//*[@id='email' or @placeholder='mail@abc.com']") #or operator used in xpath
email.clear()
email.send_keys("owner@example.com")

password = driver.find_element(By.XPATH,"//*[@id='password' and @placeholder='*****']") #and operator used in xpath
password.clear()
password.send_keys("Abc@1234")
print("Test Case 2 Passed")

email = driver.find_element(By.XPATH,"//input[starts-with(@id,'em')]") #start-with function used here
email.clear()
email.send_keys("owner@example.com")
print("Test Case 3 Passed")

password = driver.find_element(By.XPATH,"//input[contains(@id,'pass')]") #contains() used here
password.clear()
password.send_keys("Abc@1234")
print("Test Case 4 Passed")

bt = driver.find_element(By.XPATH,"//button[text()='Login']") #text() function used here
bt.click()
print("Test Case 5 Passed")