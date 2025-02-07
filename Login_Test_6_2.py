# Open & login gmail with given credentials
# go to searchbox and search "Alian Hub have sent you an invitation"
# and in results, open the first email
import time

# ERROR BECAUSE OF AUTOMATION DETECTION WHILE LOGIN FROM GOOGLE SIDE

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver = webdriver.Chrome()
# driver.maximize_window()

#from deepseek
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
chrome_options = Options()
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://mail.google.com/mail/u/0/")

driver.find_element(By.ID,"identifierId").send_keys("riap1330@gmail.com")
driver.find_element(By.XPATH,"//*[@id='identifierNext']/div/button/span").click()
time.sleep(20)

# driver.find_element(By.XPATH,"//*[@id='password']/div[1]/div/div[1]/input")
print("Test case passed")