import time

from selenium.webdriver.common.by import By
import XLUtils
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select

obj = Service(r"D:\japan_office\drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=obj)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html")
driver.find_element(By.XPATH,"//*[@id='wzrk-cancel']").click()

file = "D://japan_office/feb/selenium/session 14/fd.xlsx"
rows = XLUtils.getRowCount(file,"Sheet1")
for r in range(2,rows+1):
    princi=XLUtils.readData(file,"Sheet1",r,1)
    roi=XLUtils.readData(file,"Sheet1",r,2)
    per1 = XLUtils.readData(file,"Sheet1",r,3)
    per2 = XLUtils.readData(file,"Sheet1",r,4)
    frequency = XLUtils.readData(file,"Sheet1",r,5)
    exp_mvalue = XLUtils.readData(file,"Sheet1",r,6)
    # Passing data to application
    driver.find_element(By.XPATH,"//*[@id='principal']").send_keys(princi)
    driver.find_element(By.XPATH,"//*[@id='interest']").send_keys(roi)
    driver.find_element(By.XPATH,"//*[@id='tenure']").send_keys(per1)
    driver.find_element(By.XPATH, "//*[@id='frequency']").send_keys(per2)
    periodMenu = Select(driver.find_element(By.XPATH,"//*[@id='tenurePeriod']"))
    periodMenu.select_by_visible_text(per2)
    freqMenu = Select(driver.find_element(By.XPATH, "//*[@id='frequency']"))
    freqMenu.select_by_visible_text(frequency)
    driver.find_element(By.XPATH,"//*[@id='fdMatVal']/div[2]/a[1]/img").click()
    act_mvalue = driver.find_element(By.XPATH,"//*[@id='resp_matval']/strong").text

    #Validation
    if float(exp_mvalue) == float(act_mvalue):
        print("Test passed")
        XLUtils.writeData(file,"Sheet1",r,8,"Passed")
        XLUtils.fillGreenColor(file,"Sheet1",r,8)
    else:
        print("Test failed")
        XLUtils.writeData(file, "Sheet1", r, 8, "Failed")
        XLUtils.fillRedColor(file, "Sheet1", r, 8)

    driver.find_element(By.XPATH,"//*[@id='fdMatVal']/div[2]/a[2]/img").click()
    time.sleep(3)

print("Test case passed")
driver.quit()