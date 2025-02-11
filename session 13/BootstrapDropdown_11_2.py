from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

obj = Service(r"D:\japan_office\drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=obj)
driver.maximize_window()

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")

driver.find_element(By.XPATH,"//*[@id='select2-billing_country-container']").click()
countrieslist = driver.find_elements(By.XPATH,"//*[@id='select2-billing_country-results']/li")
print(len(countrieslist))

for country in countrieslist:
    if country.text=="India":
        country.click()
        break

print("Test case passed")