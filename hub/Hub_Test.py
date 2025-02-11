# Open & login gmail with given credentials
# go to searchbox and search "Alian Hub have sent you an invitation"
# and in results, open the first email
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.implicitly_wait(15)
driver.get("https://mail.google.com")

driver.find_element(By.ID,"identifierId").send_keys("riap1330@gmail.com")
driver.find_element(By.XPATH,"//*[@id='identifierNext']/div/button/span").click()


driver.find_element(By.XPATH,"//*[@id='password']/div[1]/div/div[1]/input[1]").send_keys("Abc@556466")
driver.find_element(By.XPATH,"//*[@id='passwordNext']/div/button[1]").click()


driver.find_element(By.XPATH,"//*[@id='gs_lc50']/input[1]").send_keys("Alian Hub have sent you an invitation")

driver.find_element(By.XPATH,"//*[@id='aso_search_form_anchor']/button[4]").click()


driver.find_element(By.XPATH,"//tr[contains(@class, 'zA')]/td[6]/div/div/div[2]").click()
driver.find_element(By.CSS_SELECTOR,"a[href*='alianhub-beta']").click()
print("Email Link Clicked Successfully")

driver.switch_to.window(driver.window_handles[-1])

driver.find_element(By.ID,"firstName").send_keys("Japan")
driver.find_element(By.ID,"lastName").send_keys("Kansara")
driver.find_element(By.ID,"password").send_keys("Abc@223133")
driver.find_element(By.ID,"confirmPassword").send_keys("Abc@223133")
driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div/div[2]/div/div/form/div[4]/label/span").click()
print("Form filled for registration")
driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div/div[2]/div/div/form/div[5]/button").click()

driver.find_element(By.XPATH,"//*[@id='email']").send_keys("riap1330+102@gmail.com")
driver.find_element(By.XPATH,"//*[@id='password']").send_keys("Abc@223133")
driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div/div[2]/div/div/form/div[3]/div/label/span").click()
driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div/div[2]/div/div/form/div[4]/button").click()
print("Login Successfully in Alian Hub")

time.sleep(20)
print("Test case passed")
driver.quit()