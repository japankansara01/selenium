from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

obj = Service(r"D:\japan_office\drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=obj)
driver.maximize_window()
driver.get("https://alianhub-beta-2lu4z.ondigitalocean.app/")

single = driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div/div/div/div/form/div[1]/label")
print(single.text) #element return web element

txt1 = driver.find_elements(By.XPATH,"//*[@id='app']/div[1]/div/div/div[2]/div/div")
print(len(txt1))
print(txt1[0].text) #elements return list even if it have only single element