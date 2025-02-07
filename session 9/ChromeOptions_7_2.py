from selenium import webdriver
from selenium.webdriver.chrome.service import Service

ops = webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")
obj = Service(r"D:\japan_office\drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
# To disable location permission popup
driver = webdriver.Chrome(service=obj,  options=ops)
driver.maximize_window()

driver.get("https://whatmylocation.com/")