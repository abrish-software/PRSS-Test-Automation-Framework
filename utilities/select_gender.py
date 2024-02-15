import time

from selenium.webdriver.common.by import By

from base.base_driver import BaseDriver


class SelectGender(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wp = BaseDriver(self.driver)

    def select_gender(self):
        gender = self.driver.find_element(By.ID, "party_sex_female")
        self.driver.execute_script("arguments[0].click();", gender)
        time.sleep(2)