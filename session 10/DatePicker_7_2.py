import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

obj = Service(r"D:\japan_office\drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=obj)
driver.maximize_window()

driver.get("https://testautomationpractice.blogspot.com/")

#driver.find_element(By.XPATH,"//*[@id='datepicker']").send_keys("01/01/2001")
year = "2026"
month = "January"
day = "15"
driver.find_element(By.XPATH,"//*[@id='datepicker']").click()

while True:
    Month = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
    Year = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text
    if Month == month and Year==year:
        break
    else:
        # driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']/div/a[1]/span").click() #Back arrow button
        driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div/a[2]/span").click()  # Next arrow button


Date = driver.find_elements(By.XPATH,"//div[@id='ui-datepicker-div']//table/tbody/tr/td/a")
for element in Date:
    if element.text==day:
        element.click()
        break

time.sleep(3)
print("Test case passed")