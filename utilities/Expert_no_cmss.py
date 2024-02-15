import time

from selenium.webdriver.common.by import By

from base.base_driver import BaseDriver


class ExpertNoCMSS(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        # self.wait = wait

    # click on the transaction to send it to supervisor
    def Click_On_Transaction(self):
        sp = BaseDriver(self.driver)
        # element_locator = (By.XPATH, "//table[@id='transcation_table']/tbody/tr[1]")
        # element = sp.wait_until_presence_of_element_located(element_locator)

        # Scroll the element into view
        # self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.driver.execute_script("arguments[0].click();", sp.wait_until_presence_of_element_located(By.XPATH,
                                                                                                      "//table["
                                                                                                      "@id"
                                                                                                      "='transcation_table']/tbody/tr[1]"))
        time.sleep(5)

    def send_to_supervisor(self, expertremarktxt):
        iframe_id = "transactionContent-iframe"
        self.driver.switch_to.frame(iframe_id)
        send_to_s = self.driver.find_element(By.XPATH, "//button[@id='edit_tran_btn_approve']")
        self.driver.execute_script("arguments[0].click();", send_to_s)
        time.sleep(5)
        enter_remark = self.driver.find_element(By.ID, "text_accept")
        enter_remark.send_keys(expertremarktxt)
        time.sleep(5)
        submit_remark = self.driver.find_element(By.XPATH, '//*[@id="remarkPopover_accept"]/div[3]/a')
        self.driver.execute_script("arguments[0].click();", submit_remark)
        time.sleep(5)

    def send_to_supervisor_for_approval(self, expertremarktext):
        self.Click_On_Transaction()
        self.send_to_supervisor(expertremarktext)
