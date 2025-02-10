import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

obj = Service(r"D:\japan_office\drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=obj)
driver.maximize_window()

driver.get("https://testautomationpractice.blogspot.com/")

input1 = driver.find_element(By.ID,"name").send_keys("Hello")
input2 = driver.find_element(By.ID,"email")

act = ActionChains(driver)

# Ctrl+A (Input 1)
act.key_down(Keys.CONTROL)
act.send_keys("a")
act.key_up(Keys.CONTROL)
act.perform()
# Alter way
# act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

# Ctrl+C
act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()

# Tab to navigate to next key
act.send_keys(Keys.TAB).perform()

# Ctrl+V (Input 2)
act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()

time.sleep(5)
print("Test case passed")