import time

from selenium.webdriver.common.by import By

from base.base_driver import BaseDriver


class AppDesc(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        # self.wait = wait

    def application_description(self, applicationdescription):
        bapp_d = self.driver.find_element(By.ID, "app_description")
        bapp_d.send_keys(applicationdescription)
        time.sleep(5)
        # next_b = self.driver.find_element(By.ID, "nextToSecond")
        # self.driver.execute_script("arguments[0].click();", next_b)
        # time.sleep(5)
