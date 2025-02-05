from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

obj = Service(r"D:\japan_office\drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=obj)
driver.maximize_window()
# driver.get("https://alianhub-beta-2lu4z.ondigitalocean.app/")
driver.get("https://opensource-demo.orangehrmlive.com/")

# Implicit wait
# driver.implicitly_wait(3) #try to run without this to see the issue

driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys("Admin")

