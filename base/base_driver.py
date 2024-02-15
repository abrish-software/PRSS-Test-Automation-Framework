import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseDriver():
    def __init__(self, driver):
        self.driver = driver

    def log_into_nrlais(self, UserName, PassWord):
        username = self.driver.find_element(By.ID, "username")
        password = self.driver.find_element(By.ID, "password")
        username.send_keys(UserName)
        password.send_keys(PassWord)
        self.driver.execute_script("arguments[0].click();",
                                   self.wait_until_element_to_be_clickable(By.ID, "button_login"))
        time.sleep(3)

    def logout(self):
        logout_button = self.driver.find_element(By.ID, "logoutButton")
        self.driver.execute_script("arguments[0].click();", logout_button)
        time.sleep(5)

    def wait_until_presence_of_element_located(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 200)
        element = wait.until(EC.presence_of_element_located((locator_type, locator)))
        return element

    def wait_until_element_to_be_clickable(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 200)
        clickable_element = wait.until(EC.element_to_be_clickable((locator_type, locator)))
        return clickable_element

    def wait_until_element_is_visible(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 200)
        visible_element = wait.until(EC.visibility_of_element_located((locator_type, locator)))
        return visible_element
