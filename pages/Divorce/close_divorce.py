import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait

from base.base_driver import BaseDriver


class CloseDivorce(BaseDriver):
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
        certefication_tab = self.driver.find_element(By.XPATH,
                                                     "//a[normalize-space()='Certificate']")
        self.driver.execute_script("arguments[0].click();", certefication_tab)
        time.sleep(5)
        first_land_certeficate = self.driver.find_element(By.XPATH,
                                                          '//div[@class="bhoechie-tab-content active"]/a[1]')
        self.driver.execute_script("arguments[0].click();", first_land_certeficate)
        time.sleep(3)
        # open_first_certeficate = self.driver.find_element(By.XPATH, '//*[@id="view-content"]/div/div[2]/div[2]/a')
        # self.driver.execute_script("arguments[0].click();", open_first_certeficate)
        # time.sleep(5)
        close_fc = BaseDriver(self.driver)
        self.driver.execute_script("arguments[0].click();", close_fc.wait_until_element_to_be_clickable(By.XPATH,
                                                                                                        '//button['
                                                                                                        '@class'
                                                                                                        '="close" and '
                                                                                                        '@data'
                                                                                                        '-dismiss'
                                                                                                        '="modal"]'))
        time.sleep(3)
        second_land_certeficate = self.driver.find_element(By.XPATH,
                                                           '//div[@class="bhoechie-tab-content active"]/a[2]')
        self.driver.execute_script("arguments[0].click();", second_land_certeficate)
        time.sleep(3)
        # open_second_certeficate = self.driver.find_element(By.XPATH, '//*[@id="view-content"]/div/div[2]/div[2]/a')
        # self.driver.execute_script("arguments[0].click();", open_second_certeficate)
        # time.sleep(5)
        close_sc = BaseDriver(self.driver)
        self.driver.execute_script("arguments[0].click();", close_sc.wait_until_element_to_be_clickable(By.XPATH,
                                                                                                        '//button['
                                                                                                        '@class'
                                                                                                        '="close" and '
                                                                                                        '@data'
                                                                                                        '-dismiss'
                                                                                                        '="modal"]'))
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
    def attach_title_deed(self, titledeed1, titledeed2):
        attach_first_title_deed = self.driver.find_element(By.XPATH, '//tr[1]/td[2]/input[@type="file"]')
        attach_first_title_deed.send_keys(titledeed1)
        time.sleep(10)
        attach_second_title_deed = self.driver.find_element(By.XPATH, '//tr[2]/td[2]/input[@type="file"]')
        attach_second_title_deed.send_keys(titledeed2)
        time.sleep(10)

    # close the title deed issue
    def close_title_deed(self):
        close_title_deed_issue = self.driver.find_element(By.ID, "issueTitleDeedAndClose")
        self.driver.execute_script("arguments[0].click();", close_title_deed_issue)
        time.sleep(10)

        # switch to default content and close the driver
        # self.driver.switch_to.default_content()

    def finalize_the_transaction(self, titledeed1,titledeed2):
        self.transaction_to_be_closed()
        self.open_certefication_tab()
        self.open_transaction_tab()
        self.close_transaction()
        self.attach_title_deed(titledeed1,titledeed2)
        self.close_title_deed()
