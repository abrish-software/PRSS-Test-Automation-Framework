import time

from selenium.webdriver.common.by import By

from base.base_driver import BaseDriver


class LoadParcel(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        # self.wait = wait
        self.waitforaddparcel = BaseDriver(self.driver)

    def load_parcel(self):
        load_parcel_info = self.driver.find_element(By.XPATH, "//button[normalize-space()='Load Parcel']")
        self.driver.execute_script("arguments[0].click();", load_parcel_info)
        time.sleep(5)

    def search_Holding(self, firstname, fathername, gfname):
        first_name = self.driver.find_element(By.ID, "sea_name")
        father_name = self.driver.find_element(By.ID, "sea_father")
        gf_name = self.driver.find_element(By.ID, "sea_gfather")
        search_button = self.driver.find_element(By.XPATH, '//*[@id="sea_form"]/div[2]/button')
        # first_name.send_keys(firstname)
        self.driver.execute_script("arguments[0].value = arguments[1];", first_name, firstname)
        father_name.send_keys(fathername)
        gf_name.send_keys(gfname)
        self.driver.execute_script("arguments[0].click();", search_button)
        time.sleep(10)

    def add_parcel(self):
        self.driver.execute_script("arguments[0].click();",
                                   self.waitforaddparcel.wait_until_presence_of_element_located(By.XPATH,
                                                                                                '//*['
                                                                                                '@id="total_result'
                                                                                                '"]/table/tbody/tr['
                                                                                                '1]/td/table/thead/tr'
                                                                                                '/td['
                                                                                                '5]/div/a[2]'))
        time.sleep(5)

    def next_button(self):
        button_next = self.driver.find_element(By.ID, "nextToSecond")
        self.driver.execute_script("arguments[0].click();", button_next)
        time.sleep(5)

    def load_parcel_infromation(self, firstname, fathername, gfname):
        self.load_parcel()
        self.search_Holding(firstname, fathername, gfname)
        self.add_parcel()
        self.next_button()
