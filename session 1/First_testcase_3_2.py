#For chrome
# open browser
# open url https://opensource-demo.orangehrmlive.com/
# Enter username (Admin)
# enter password (admin123)
# click on login
# capture title of the home page
# verify title of the:OrangeHRM (Expected)
# close browser

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# service = Service(r"D:\japan_office\drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
# driver = webdriver.Chrome(service=service)

# driver = webdriver.Chrome()
#driver = webdriver.Edge()
driver = webdriver.Firefox()
driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com/")

username_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "username"))
)
username_field.send_keys("Admin")

password_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "password"))
)
password_field.send_keys("admin123")

login_button = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button"))
)
login_button.click()

act_title = driver.title
print("Page Title: ", act_title) #get title from webpage
exp_title = "OrangeHRM"
if act_title==exp_title:
    print("Title Matched, Test Case passed")
else:
    print("Test case failed")
