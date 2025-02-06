from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

obj = Service(r"D:\japan_office\drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=obj)
driver.maximize_window()

driver.get("http://practice-automation.com/iframes/")

driver.switch_to.frame(driver.find_element(By.ID,"iframe-1"))
# driver.find_element(By.XPATH,"//*[@id='__docusaurus']/nav/div[1]/div[1]/button").click()

mywait = WebDriverWait(driver,5)
menu = mywait.until(EC.element_to_be_clickable((By.XPATH,"//*[@id='__docusaurus']/nav/div[1]/div[1]/button")))
menu.click()
print("Test case passed")