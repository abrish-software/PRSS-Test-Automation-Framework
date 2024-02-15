import time

from selenium.webdriver.common.by import By

from base.base_driver import BaseDriver


class CloseTheTransaction(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        # self.wait = wait

    def transaction_to_be_closed(self):
        self.driver.refresh()
        time.sleep(5)
        tc = BaseDriver(self.driver)
        self.driver.execute_script("arguments[0].scrollIntoView();", tc.wait_until_presence_of_element_located(By.XPATH,
                                                                                                               "//table[@id='transcation_table']/tbody/tr[1]"))  # Ensure the element is in view
        self.driver.execute_script("arguments[0].click();", tc.wait_until_presence_of_element_located(By.XPATH,
                                                                                                      "//table[@id='transcation_table']/tbody/tr[1]"))
        time.sleep(3)

    # click on open transaction
    # def open_transaction_tab(self):
    #     ot = BaseDriver(self.driver)
    #     self.driver.execute_script("arguments[0].click();", ot.wait_until_element_to_be_clickable(By.XPATH,
    #                                                                                               '//*[@id="view'
    #                                                                                               '-content"]/div'
    #                                                                                               '/div[1]/div/a[1]'))
    #     time.sleep(3)

    # click on close transaction
    def close_transaction(self, officerremarktext):
        iframe_id = "transactionContent-iframe"
        self.driver.switch_to.frame(iframe_id)
        close_transaction = self.driver.find_element(By.ID, "edit_tran_btn_approve")
        self.driver.execute_script("arguments[0].click();", close_transaction)
        time.sleep(5)
        enter_remark = self.driver.find_element(By.ID, "text_accept")
        enter_remark.send_keys(officerremarktext)
        time.sleep(5)
        submit_remark = self.driver.find_element(By.XPATH, '//*[@id="remarkPopover_accept"]/div[3]/a')
        self.driver.execute_script("arguments[0].click();", submit_remark)
        time.sleep(5)

    def finalize_the_transaction(self, officerremarktext):
        self.transaction_to_be_closed()
        # self.open_transaction_tab()
        self.close_transaction(officerremarktext)
