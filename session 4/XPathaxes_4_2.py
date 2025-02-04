from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

obj = Service(r"D:\japan_office\drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=obj)
driver.maximize_window()

driver.get("https://demo.opencart.com/")

#self
msg = driver.find_element(By.XPATH,"//*[@id='content']/div[2]/div[1]/div/div[2]/div/h4/a/self::a").text
print(msg)

#parent
msg1 = driver.find_element(By.XPATH,"//*[@id='content']/div[2]/div[1]/div/div[2]/div/h4/a/parent::h4").text
print(msg1)

#ancestor
msg2 = driver.find_element(By.XPATH,"//*[@id='content']/div[2]/div[1]/div/div[2]/div/h4/a/ancestor::div").text
print(msg2)

#child
childs = driver.find_elements(By.XPATH,"//*[@id='content']/ancestor::div/child::div")
print(len(childs))

#Decendant
msg3 = driver.find_element(By.XPATH,"//*[@id='content']/div[2]/div[1]/div/div[2]/div/descendant::a").text
print(msg3)


# print("Following")
msg4 = driver.find_element(By.XPATH,"//*[@id='content']/div[2]/div[1]/div/div[2]/div/h4/a/following::*").text
print(msg4)

#Following-sibling
#msg5 = driver.find_element(By.XPATH,"//*[@id='content']/div[2]/div[1]/div/div[2]/div/h4/a/following-sibling::*")
#print(len(msg5))

# Preceding
# msg6 = driver.find_element(By.XPATH,"/html/body/footer/div/div/div[2]/ul/li[2]/a/preceding::*")
# print(len(msg6))
#
# Preceding-sibling
# msg7 = driver.find_element(By.XPATH,"/html/body/footer/div/div/div[2]/ul/li[2]/a/preceding-sibling::*")
# print(len(msg7))