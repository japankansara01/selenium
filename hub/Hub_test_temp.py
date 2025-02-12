import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class GmailAutomation:
    def __init__(self, driver):
        self.driver = driver

    def login(self, email, password):
        self.driver.get("https://mail.google.com")
        self.driver.find_element(By.ID, "identifierId").send_keys(email)
        self.driver.find_element(By.XPATH, "//*[@id='identifierNext']/div/button/span").click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "Passwd")))
        self.driver.find_element(By.NAME, "Passwd").send_keys(password)
        self.driver.find_element(By.XPATH, "//*[@id='passwordNext']/div/button[1]").click()

    def search_email(self, keyword):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='gs_lc50']/input[1]")))
        self.driver.find_element(By.XPATH, "//*[@id='gs_lc50']/input[1]").send_keys(keyword)
        self.driver.find_element(By.XPATH, "//*[@id='aso_search_form_anchor']/button[4]").click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//tr[contains(@class, 'zA')]/td[6]/div/div/div[2]")))
        self.driver.find_element(By.XPATH, "//tr[contains(@class, 'zA')]/td[6]/div/div/div[2]").click()
        self.driver.find_element(By.CSS_SELECTOR, "a[href*='-beta']").click()
        print("Email Link Clicked Successfully")
        self.driver.switch_to.window(self.driver.window_handles[-1])

class HubAutomation:
    def __init__(self, driver):
        self.driver = driver

    def register(self, first_name, last_name, password):
        self.driver.find_element(By.ID, "firstName").send_keys(first_name)
        self.driver.find_element(By.ID, "lastName").send_keys(last_name)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "confirmPassword").send_keys(password)
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div/div[2]/div/div/form/div[4]/label/span").click()
        print("Form filled for registration")
        self.driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div/div[2]/div/div/form/div[5]/button").click()

    def login(self, email, password):
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.driver.find_element(By.XPATH, "//*[@id='email']").send_keys(email)
        self.driver.find_element(By.XPATH, "//*[@id='password']").send_keys(password)
        self.driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div/div[2]/div/div/form/div[3]/div/label/span").click()
        self.driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div/div[2]/div/div/form/div[4]/button").click()
        print("Login Successfully in Hub")

if __name__ == "__main__":
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    gmail = GmailAutomation(driver)
    gmail.login("riap1330@gmail.com", "Abc@556466")
    gmail.search_email("Alian Hub have sent you an invitation")

    hub = HubAutomation(driver)
    # hub.register("Japan", "Kansara", "Abc@223133") #temp comment
    hub.login("riap1330+104@gmail.com", "Abc@223133")

    time.sleep(10)
    print("Test case passed")
    driver.quit()