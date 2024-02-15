import time

import pyautogui
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait

from base.base_driver import BaseDriver
from utilities.expert_role import Expert


class ExOfficioExpert(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.expert = Expert(self.driver)
        self.sp = BaseDriver(self.driver)
        # self.wait = wait

    # click on the transaction to send it to supervisor
    def Click_On_ExOffio(self):
        # element_locator = (By.XPATH, "//table[@id='transcation_table']/tbody/tr[1]")
        # element = sp.wait_until_presence_of_element_located(element_locator)

        # Scroll the element into view
        # self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.driver.execute_script("arguments[0].click();", self.sp.wait_until_presence_of_element_located(By.XPATH,
                                                                                                           "//table["
                                                                                                           "@id"
                                                                                                           "='transcation_table']/tbody/tr[1]"))
        time.sleep(5)

    # wait until spatial_op officer inputs spatial data and send to supervisor button is accessible
    def manipulate_holding(self, ortho):
        iframe_id = "transactionContent-iframe"
        self.driver.switch_to.frame(iframe_id)
        click_on_manipulate = self.driver.find_element(By.ID, "edit_tran_btn")
        self.driver.execute_script("arguments[0].click();", click_on_manipulate)
        time.sleep(5)
        click_on_edit = self.driver.find_element(By.XPATH, '//*[@id="parcels_table_parcel_list"]/tr/td[7]/a[2]')
        self.driver.execute_script("arguments[0].click();", click_on_edit)
        time.sleep(5)
        add_ortho = self.driver.find_element(By.ID, "parcel_orthograph")
        add_ortho.clear()
        add_ortho.send_keys(ortho)
        time.sleep(5)
        select_acq_year = self.driver.find_element(By.ID, "parcel_acquisitionYear")
        select_year_dd = Select(select_acq_year)
        select_year_dd.select_by_index(1)
        time.sleep(5)
        select_soil_fertility = self.driver.find_element(By.ID, "parcel_soilFertility")
        select_soil_dd = Select(select_soil_fertility)
        select_soil_dd.select_by_index(2)
        time.sleep(5)
        save_parcel_button = self.driver.find_element(By.XPATH,
                                                      "//button[contains(@class, 'btn-nrlais')][contains(@onclick, "
                                                      "'validateAndSaveParcel')]")

        self.driver.execute_script("arguments[0].click();", save_parcel_button)
        time.sleep(5)
        # pyautogui.press('enter')
        try:
            alert = WebDriverWait(self.driver, 20).until(EC.alert_is_present())
            alert.accept()
        finally:
            # Make sure to switch back to the default content after handling the alert
            self.driver.switch_to.default_content()
        time.sleep(5)

    def view_application(self):
        go_to_mainpage = self.driver.find_element(By.ID, "go_to_application")
        self.driver.execute_script("arguments[0].click();", go_to_mainpage)
        time.sleep(5)

    def send_to_supervisor(self, expertremarktxt):
        # self.expert.send_to_supervisor_for_approval(expertremarktxt)
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

    def send_to_supervisor_for_approval(self, ortho, expertremarktext):
        self.Click_On_ExOffio()
        self.manipulate_holding(ortho)
        self.view_application()
        self.send_to_supervisor(expertremarktext)
