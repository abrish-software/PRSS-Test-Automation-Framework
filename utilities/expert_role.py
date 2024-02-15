import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait

from base.base_driver import BaseDriver


class Expert(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        # self.wait = wait

    # click on the transaction to send it to supervisor
    def sendTo_Supervisor(self):
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

    # wait until spatial_op officer inputs spatial data and send to supervisor button is accessible
    def is_send_to_supervisor_visible(self):
        send_to_supervisor_locator = (By.ID, "edit_tran_btn_approve")
        try:
            # Switch to the iframe
            iframe_id1 = "transactionContent-iframe"
            self.driver.switch_to.frame(iframe_id1)
            send_to_s = self.driver.find_element(*send_to_supervisor_locator)
            return send_to_s.is_displayed()
        except NoSuchElementException:
            return False
        finally:
            # Switch back to the default content after interacting with the iframe
            self.driver.switch_to.default_content()

    # Set a maximum wait time
    def refresh_until_send_to_supervisor_visible(self):
        # refresh_button_locator = (By.XPATH, "//button[@class='btn btn-primary btn-circle']")
        max_wait_time = 300  # 300 seconds (5 minutes)
        current_wait_time = 0
        refresh_interval = 5  # 10 seconds
        rv = BaseDriver(self.driver)

        while current_wait_time < max_wait_time:
            # Click the refresh button
            # button_locator = (By.XPATH, "//button[@class='btn btn-primary btn-circle']")
            # Use the defined locator variable
            # element2 = rv.wait_until_element_to_be_clickable(button_locator)
            # Scroll the element into view and click
            self.driver.execute_script("arguments[0].click();", rv.wait_until_element_to_be_clickable(By.XPATH,
                                                                                                      "//button["
                                                                                                      "@class='btn "
                                                                                                      "btn-primary "
                                                                                                      "btn-circle']"))

            # Check if the "Send to Supervisor" button is visible
            if self.is_send_to_supervisor_visible():
                # If visible, click the button and break out of the loop
                iframe_id1 = "transactionContent-iframe"
                self.driver.switch_to.frame(iframe_id1)  # Switch to the iframe again
                # approve_button_locator = (By.ID, "edit_tran_btn_approve")
                # Use the defined locator variable
                # element3 = rv.wait_until_element_to_be_clickable(approve_button_locator)
                # Scroll the element into view and click
                self.driver.execute_script("arguments[0].click();", rv.wait_until_element_to_be_clickable(By.ID,
                                                                                                          "edit_tran_btn_approve"))
                break

            # Wait for the next iteration
            time.sleep(refresh_interval)
            current_wait_time += refresh_interval

        # Handle the case where the button did not appear within the specified time
        if current_wait_time >= max_wait_time:
            print("Timed out. The 'Send to Supervisor' button did not appear within the specified time.")

    # fill in the remark and click submit button
    def submit_to_supervisor(self, remarktext):
        remark_text = self.driver.find_element(By.ID, "text_accept")
        remark_text.send_keys(remarktext)
        time.sleep(5)

        # click on submit button
        submit_button = self.driver.find_element(By.XPATH, '//*[@id="remarkPopover_accept"]/div[3]/a')
        # submit_button.send_keys(Keys.RETURN)
        self.driver.execute_script("arguments[0].click();", submit_button)
        time.sleep(5)

        # switch to default content
        self.driver.switch_to.default_content()
        time.sleep(5)

    def send_to_supervisor_for_approval(self, remarktext):
        self.sendTo_Supervisor()
        self.is_send_to_supervisor_visible()
        self.refresh_until_send_to_supervisor_visible()
        self.submit_to_supervisor(remarktext)