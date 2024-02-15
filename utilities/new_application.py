import time

from selenium.webdriver.common.by import By

from base.base_driver import BaseDriver


class NewApplication(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wpna = BaseDriver(driver)

    def select_new_application(self):
        # element = self.wpna.wait_until_element_to_be_clickable(By.CLASS_NAME, "btn-transaction")
        self.driver.execute_script("arguments[0].click();",
                                   self.wpna.wait_until_element_to_be_clickable(By.CLASS_NAME, "btn-transaction"))

# class NewApplication(BaseDriver):
#     def __init__(self, driver):
#         super().__init__(driver)
#         self.driver = driver
#         # self.wpna = BaseDriver(self.driver)
#
#     def select_new_application(self):
#         time.sleep(5)
#         new_application_button = self.driver.find_element(By.CLASS_NAME, "btn-transaction")
#         self.driver.execute_script("arguments[0].click();", new_application_button)
