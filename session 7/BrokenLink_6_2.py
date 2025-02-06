# install requests in pythoninterpreter in setting
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

obj = Service(r"D:\japan_office\drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=obj)
driver.maximize_window()

driver.get("http://www.deadlinkcity.com/")

allLinks = driver.find_elements(By.TAG_NAME,'a')
count=0

for link in allLinks:
    url = link.get_attribute('href')
    # Need to use try block because link is not exist
    try:
        response = requests.head(url)
    except:
        None

    if response.status_code>=400:
        print(f"Broken Link: {url}")
        count+=1
    else:
        print(url," is valid link")

print("Invalid Link Count: ",count)
print("Test case passed.")