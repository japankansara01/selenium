import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
import mysql.connector

obj = Service(r"D:\japan_office\drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=obj)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html")

try:
    con = mysql.connector.connect(host="localhost",port=3306,user="root",passwd="root",database="mydb")
    curs=con.cursor() #create cursor
    curs.execute("select * from simple_interest")

    driver.find_element(By.XPATH, "//*[@id='wzrk-cancel']").click()
    for rows in curs:
        princi= rows[0]
        roi= rows[1]
        per1 = rows[2]
        per2 = rows[3]
        frequency = rows[4]
        exp_mvalue = rows[5]

        # Passing data to application
        time.sleep(3)
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

        else:
            print("Test failed")

        driver.find_element(By.XPATH,"//*[@id='fdMatVal']/div[2]/a[2]/img").click()
        time.sleep(1)

    con.close()  #closing connection
    print("Test case passed")

except Exception as e:
    print(f"Connection unsuccessful: {e}")

driver.quit()