import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait

from base.base_driver import BaseDriver


class CloseTransaction(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        # self.wait = wait

    # click on the transaction to be closed
    def transaction_to_be_closed(self):
        self.driver.refresh()
        time.sleep(5)
        tc = BaseDriver(self.driver)
        self.driver.execute_script("arguments[0].scrollIntoView();", tc.wait_until_presence_of_element_located(By.XPATH,
                                                                                                               "//table[@id='transcation_table']/tbody/tr[1]"))  # Ensure the element is in view
        self.driver.execute_script("arguments[0].click();", tc.wait_until_presence_of_element_located(By.XPATH,
                                                                                                      "//table[@id='transcation_table']/tbody/tr[1]"))
        time.sleep(3)

    # click on certefication tab
    def open_certefication_tab(self):
        iframe_element = self.driver.find_element(By.ID, "transactionContent-iframe")
        self.driver.switch_to.frame(iframe_element)
        land_certeficate = self.driver.find_element(By.XPATH, "//a[normalize-space()='Certificate']")
        self.driver.execute_script("arguments[0].click();", land_certeficate)
        time.sleep(3)
        open_certeficate = self.driver.find_element(By.XPATH, '//*[@id="view-content"]/div/div[2]/div[2]/a')
        self.driver.execute_script("arguments[0].click();", open_certeficate)
        time.sleep(5)

    # close the certeficate window
    def close_certefication_window(self):
        cw = BaseDriver(self.driver)
        self.driver.execute_script("arguments[0].click();", cw.wait_until_element_to_be_clickable(By.XPATH,
                                                                                                  '//*['
                                                                                                  '@id'
                                                                                                  '="document_preview_modal"]/div/div/div[1]/button[1]'))
        time.sleep(3)

    # click on open transaction
    def open_transaction_tab(self):
        ot = BaseDriver(self.driver)
        self.driver.execute_script("arguments[0].click();", ot.wait_until_element_to_be_clickable(By.XPATH,
                                                                                                  '//*[@id="view'
                                                                                                  '-content"]/div'
                                                                                                  '/div[1]/div/a[1]'))
        time.sleep(3)

    # click on close transaction
    def close_transaction(self):
        close_transaction = self.driver.find_element(By.ID, "edit_tran_btn_approve")
        self.driver.execute_script("arguments[0].click();", close_transaction)
        time.sleep(5)

    #  attach title deed
    def attach_title_deed(self, titledeed):
        attach_title_deed = self.driver.find_element(By.XPATH, "//input[@type='file']")
        attach_title_deed.send_keys(titledeed)
        time.sleep(15)

    # close the title deed issue
    def close_title_deed(self):
        close_title_deed_issue = self.driver.find_element(By.ID, "issueTitleDeedAndClose")
        self.driver.execute_script("arguments[0].click();", close_title_deed_issue)
        time.sleep(10)

        # switch to default content and close the driver
        # self.driver.switch_to.default_content()

    def finalize_the_transaction(self, titledeed):
        self.transaction_to_be_closed()
        self.open_certefication_tab()
        self.close_certefication_window()
        self.open_transaction_tab()
        self.close_transaction()
        self.attach_title_deed(titledeed)
        self.close_title_deed()

