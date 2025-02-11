from selenium import webdriver

def headless_chrome():
    from selenium.webdriver.chrome.service import Service
    obj = Service(r"D:\japan_office\drivers\chromedriver-win64\chromedriver-win64\chromedriver.exe")
    ops = webdriver.ChromeOptions()
    ops.headless=True
    driver = webdriver.Chrome(service=obj,options=ops)
    return driver

def headless_edge():
    from selenium.webdriver.chrome.service import Service
    obj = Service(r"D:\japan_office\drivers\edgedriver_win64\msedgedriver.exe")
    ops = webdriver.EdgeOptions()
    ops.headless=True
    driver = webdriver.Edge(service=obj,options=ops)
    return driver

driver = headless_chrome()
# driver = headless_edge()
driver.get("https://practice-automation.com/form-fields/")
print(driver.title)
print(driver.current_url)
driver.close()