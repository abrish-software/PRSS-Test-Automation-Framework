import time
from selenium.webdriver.common.by import By


class ExpertLogout():
    def __init__(self, driver):
        self.driver = driver

    def expert_logout(self):
        welcome_expert = self.driver.find_element(By.CSS_SELECTOR, "button.btn-welcome")
        self.driver.execute_script("arguments[0].click();", welcome_expert)
        time.sleep(5)
        button = self.driver.find_element(By.ID, "logoutButton")
        self.driver.execute_script("arguments[0].click();", button)
        time.sleep(5)
