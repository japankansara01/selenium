from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

obj = Service(r"D:\japan_office\drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=obj)
driver.maximize_window()

driver.get("https://practice-automation.com")

# select all link and total number of links in page
link = driver.find_elements(By.TAG_NAME,'a')
print(len(link))

# Get all links text
for link_txt in link:
    print(link_txt.text)

# time.sleep(3)
print("Test case passed.")