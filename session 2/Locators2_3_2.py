import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# driver = webdriver.Chrome()
driver = webdriver.Edge()
driver.maximize_window()

driver.get("https://www.facebook.com/")

# CSS Selector (TAG & ID)
driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("1")
# driver.find_element(By.CSS_SELECTOR,"#email").send_keys("japankansara") Tag Name(input) is not mandatory

# CSS Selector (TAG & CLASS)
driver.find_element(By.CSS_SELECTOR,"input.inputtext").send_keys("2")

# CSS Selector (TAG & Attribute)
driver.find_element(By.CSS_SELECTOR,"input[data-testid=royal-email]").send_keys("3")

# CSS Selector (TAG & Class & Attribute)
driver.find_element(By.CSS_SELECTOR,"input.inputtext[data-testid=royal-pass]").send_keys("4")

print("CSS Selectors Test Case Done")

time.sleep(5)