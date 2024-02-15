import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from base.base_driver import BaseDriver


class MaritalStatus(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        # self.wait = wait
        self.waitforaddparcel = BaseDriver(self.driver)

    def marital_status(self, pocfile, pocref, poctext):
        add_marital_info = self.driver.find_element(By.CSS_SELECTOR, 'td#pom_btn a#add_id')
        add_poc_file = self.driver.find_element(By.ID, "pom_file")
        add_poc_reference = self.driver.find_element(By.CSS_SELECTOR, "input#pom_ref")
        add_poc_text = self.driver.find_element(By.CSS_SELECTOR, "input#pom_text")
        add_poc_content = self.driver.find_element(By.XPATH, "//a[@class='btn btn-nrlais' and "
                                                             "@href=\"javascript:applicantPicker.validateAndSavePOM("
                                                             ")\"]")
        next_to_third = self.driver.find_element(By.ID, "doc_nextbtn")

        self.driver.execute_script("arguments[0].click();", add_marital_info)
        time.sleep(5)
        add_poc_file.send_keys(pocfile)
        time.sleep(5)
        add_poc_reference.send_keys(pocref)
        time.sleep(5)
        add_poc_text.send_keys(poctext)
        time.sleep(5)
        self.driver.execute_script("arguments[0].click();", add_poc_content)
        time.sleep(5)
        self.driver.execute_script("arguments[0].click();", next_to_third)
        time.sleep(5)
