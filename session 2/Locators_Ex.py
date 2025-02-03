# Website have capatcha issue
# open browser
# open url https://demo.nopcommerce.com
# search "Samsung Galaxy S24 256GB"
# add to wishlit
# go to wishlist page
# remove the samsung mobile
# close the browser
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://demo.nopcommerce.com")

driver.find_element(By.ID,"small-searchterms").send_keys("Samsung Galaxy S24 256GB")
time.sleep(2)

driver.find_element(By.XPATH,"//*[@id='small-search-box-form']/button").click()
time.sleep(3)

driver.get("https://demo.nopcommerce.com/samsung-galaxy-s24-256gb")
time.sleep(10)

driver.find_element(By.ID,"add-to-wishlist-button-46").click()
print("Added in wishlist")
time.sleep(10)

driver.find_elements(By.CSS_SELECTOR,"span.close").click()
time.sleep(5)

driver.find_elements(By.CSS_SELECTOR,"a.ico-wishlist").click()
time.sleep(3)

driver.find_elements(By.CSS_SELECTOR,"button.remove-btn").click()
time.sleep(5)

print("100% Work Done")
time.sleep(3)