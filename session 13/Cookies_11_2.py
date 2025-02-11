from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

obj = Service(r"D:\japan_office\drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=obj)
driver.maximize_window()

driver.get("https://practice-automation.com/form-fields/")

cookies = driver.get_cookies()
print("Size of cookies: ",len(cookies))

# Print details of all cookies
for c in cookies:
    print(c)
    print(c.get('name'),":",c.get('value'))

# Add new cookie to browser
driver.add_cookie({"name":"MyCookie", "value":"123456"})
cookies = driver.get_cookies()
print("Size of cookies after adding new one:" ,len(cookies))

# Deleting specific cookie
driver.delete_cookie("MyCookie")
cookies=driver.get_cookies()
print("Size of cookies after deleted one:", len(cookies))

# Deleting all cookies
# driver.delete_all_cookies()

print("Test case passed")
driver.quit()