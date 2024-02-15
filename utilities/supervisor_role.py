import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait

from base.base_driver import BaseDriver


class Supervisor(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # click on the transaction to be approved
    def wait_approve_transaction(self):
        waitapproval = BaseDriver(self.driver)
        self.driver.execute_script("arguments[0].scrollIntoView();", waitapproval.wait_until_presence_of_element_located(By.XPATH, "//table[@id='transcation_table']/tbody/tr[1]"))  # Ensure the element is in view
        self.driver.execute_script("arguments[0].click();",waitapproval.wait_until_presence_of_element_located(By.XPATH, "//table[@id='transcation_table']/tbody/tr[1]"))
        time.sleep(3)

    # switch to an iframe and click on accept transaction button
    def approve_transaction(self):
        s_iframe_id = "transactionContent-iframe"
        self.driver.switch_to.frame(s_iframe_id)
        approve_button = self.driver.find_element(By.ID, "edit_tran_btn_approve")
        self.driver.execute_script("arguments[0].click();", approve_button)
        time.sleep(3)

    # add remark text and click on submit button
    def submit_to_Officer(self, supervisorremarktext):
        s_remark_text = self.driver.find_element(By.ID, "text_accept")
        s_remark_text.send_keys(supervisorremarktext)
        time.sleep(5)
        s_submit_button = self.driver.find_element(By.XPATH, '//*[@id="remarkPopover_accept"]/div[3]/a')
        self.driver.execute_script("arguments[0].click();", s_submit_button)
        time.sleep(5)
        self.driver.switch_to.default_content()
        time.sleep(5)

    def approved_transaction(self, supervisorremarktext):
        self.wait_approve_transaction()
        self.approve_transaction()
        self.submit_to_Officer(supervisorremarktext)


