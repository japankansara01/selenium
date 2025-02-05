from selenium import webdriver
from selenium.common import ElementNotVisibleException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

obj = Service(r"D:\japan_office\drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=obj)
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/")

mywait = WebDriverWait(driver,5) # Explicit wait declaration

#With other parameters
mywait = WebDriverWait(driver,5,poll_frequency = 1,ignored_exceptions=[ElementNotVisibleException])

usrname = mywait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input")))
usrname.send_keys("Admin")