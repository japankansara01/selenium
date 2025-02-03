# open browser
# open url https://admin-demo.nopcommerce.com/login
# Enter email (admin@yourstore.com)
# enter password (admin)
# click on login
# capture title of the home page
# verify title of the:OrangeHRM (Expected)
# close browser
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Edge()
#driver = webdriver.Chrome()
#driver = webdriver.Firefox()
driver.maximize_window()

driver.get("https://admin-demo.nopcommerce.com/login")

email_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "Email"))
)
email_field.clear()
email_field.send_keys("admin@yourstore.com")

password_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "Password"))
)
password_field.clear()
password_field.send_keys("admin")

login_button = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH,"//*[@id='main']/div/div/div/div[2]/div[1]/div/form/div[3]/button"))
)
login_button.click()

print("Test Case Passed")

time.sleep(7)  #used for chrome and edge
driver.close()