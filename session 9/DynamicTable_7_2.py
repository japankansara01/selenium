import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait

obj = Service(r"D:\japan_office\drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=obj)
driver.maximize_window()

driver.get("https://testautomationpractice.blogspot.com/")

Len_Row = len(driver.find_elements(By.XPATH,"//table[@id='taskTable']//tr"))
Len_Col = len(driver.find_elements(By.XPATH,"//table[@id='taskTable']//tr[1]/th"))
print(Len_Row)
print(Len_Col)

# count = 0
# for rOws in range(2, Len_Row+1):
#     browser = driver.find_element(By.XPATH,"//table[@id='taskTable']/tbody/tr/td[1]").text
#     if browser == "Chrome":
#         count = count+1
#
# print("Total number of list: ", rOws)
# print("Number of Chrome browser: ", count)
# time.sleep(15)

# Print All Data of table
wait = WebDriverWait(driver, 10)

# Wait for table to be present
wait.until(EC.presence_of_element_located((By.ID, "taskTable")))

# Get total rows dynamically
Len_Row = len(driver.find_elements(By.XPATH, "//table[@id='taskTable']//tr"))
print(f"Total Rows: {Len_Row}")

# Loop through each row
for rOws in range(2, Len_Row + 1):  # Start from row 2 if row 1 is header
    # Get column count for the current row
    row_xpath = f"//table[@id='taskTable']//tr[{rOws}]/td"
    Len_Col = len(driver.find_elements(By.XPATH, row_xpath))

    print(f"Row {rOws} has {Len_Col} columns")

    for cOlumn in range(1, Len_Col + 1):
        try:
            cell_xpath = f"//table[@id='taskTable']//tr[{rOws}]/td[{cOlumn}]"
            tableData = driver.find_element(By.XPATH, cell_xpath).get_attribute("textContent").strip()
            print(tableData, end="      ")
        except:
            print("[Missing Data]", end="      ")
    print()

print("test case passed")