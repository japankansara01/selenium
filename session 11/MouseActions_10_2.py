# Action chains
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

obj = Service(r"D:\japan_office\drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=obj)
driver.maximize_window()

driver.get("https://testautomationpractice.blogspot.com/")

point = driver.find_element(By.XPATH,"//*[@id='HTML3']/div[1]/div/button")
mobile = driver.find_element(By.XPATH,"//*[@id='HTML3']/div[1]/div/div/a[1]")

act = ActionChains(driver)
# Hover action
#here without perform method the click action not happen
act.move_to_element(point).move_to_element(mobile).click().perform()

# Right click action
# act.context_click().perform()

# Double click
f1 = driver.find_element(By.ID,"field1")
f1.clear()
f1.send_keys("COPY")
Copy = driver.find_element(By.XPATH,"//*[@id='HTML10']/div[1]/button")
act.double_click(Copy).perform()

# Drag and drop
source_ele = driver.find_element(By.XPATH,"//*[@id='draggable']")
target_ele = driver.find_element(By.XPATH,"//*[@id='droppable']")
act.drag_and_drop(source_ele,target_ele).perform()

#Slider
min_slider = driver.find_element(By.XPATH,"//*[@id='slider-range']/span[1]")
max_slider = driver.find_element(By.XPATH,"//*[@id='slider-range']/span[2]")
print("Minimum Slider",min_slider.location)
print("Maximum Slider",max_slider.location)
act.drag_and_drop_by_offset(min_slider, 100,0).perform()
act.drag_and_drop_by_offset(max_slider, -50,0).perform()
print("Minimum Slider",min_slider.location)
print("Maximum Slider",max_slider.location)

time.sleep(5)
