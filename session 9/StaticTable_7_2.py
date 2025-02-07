from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

obj = Service(r"D:\japan_office\drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=obj)
driver.maximize_window()

driver.get("https://testautomationpractice.blogspot.com/")

Len_Row = len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr"))
Len_Col = len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr[1]/th"))
print(Len_Row)
print(Len_Col)

# Print All Data of table
for rOws in range(2, Len_Row+1):
    for cOlumn in range(1, Len_Col+1):
        tableData = driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(rOws)+"]/td["+str(cOlumn)+"]").text
        print(tableData, end='      ')
    print()

# Print books by author name
print("Books By Amit:-")
for rOws in range(2, Len_Row+1):
    authorName = driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(rOws)+"]/td[2]").text
    if authorName == "Amit":
        bookName = driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(rOws)+"]/td[1]").text
        bookPrice = driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(rOws)+"]/td[4]").text
        print(bookName, "     ",authorName, "     ", bookPrice)

print("Test Case passed")