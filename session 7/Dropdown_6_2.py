import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

obj = Service(r"D:\japan_office\drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=obj)
driver.maximize_window()

driver.get("https://practice-automation.com/form-fields/")

# select dropdown menu
# drpMenu = driver.find_element(By.XPATH,"//*[@id='automation']")
# drpMenu = Select(drpMenu)

# Alter way to select dropdown menu
drpMenu = Select(driver.find_element(By.XPATH,"//*[@id='automation']"))

# select option from dropdown menu
# drpMenu.select_by_visible_text("Undecided")
# time.sleep(2)
# drpMenu.select_by_value("yes")
# time.sleep(2)
# drpMenu.select_by_index(2)

# display all options of dropdown menu
allOptions = drpMenu.options
print("Total Options in Dropdown Menu:", len(allOptions))
for options in allOptions:
    print(options.text)


# Select option from dropdown menu without builtin method like select_by_value
for selectOpt in allOptions:
    if selectOpt.text == "Yes":
        selectOpt.click()
        break

# time.sleep(3)
print("Test case passed.")