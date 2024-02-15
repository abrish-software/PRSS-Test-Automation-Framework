import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from base.base_driver import BaseDriver
from selenium.webdriver.support import expected_conditions as EC


class ThirdParty(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        # self.wait = wait
        self.waitforaddparcel = BaseDriver(self.driver)

    def add_holder_profile(self, fname, fathername, gfname):
        add_holder = self.driver.find_element(By.ID, "restrictive_interest_add")
        self.driver.execute_script("arguments[0].click();", add_holder)
        # Add holder Information
        time.sleep(5)
        add_first_name = self.driver.find_element(By.ID, "party_firstname")
        add_first_name.send_keys(fname)
        time.sleep(3)
        add_father_name = self.driver.find_element(By.ID, "party_fathername")
        add_father_name.send_keys(fathername)
        time.sleep(3)
        add_gfather_name = self.driver.find_element(By.ID, "party_gfathername")
        add_gfather_name.send_keys(gfname)
        time.sleep(3)

    def add_DOB(self):
        element = self.driver.find_element(By.ID, "party_dateOfBirth")
        element.send_keys(Keys.RETURN)
        time.sleep(5)

        select_year = self.driver.find_element(By.ID, "etdc_year_et")
        year_dd = Select(select_year)
        year_dd.select_by_index(1)
        time.sleep(2)

        # select date
        select_date = self.driver.find_element(By.XPATH, '//*[@id="body"]/div[21]/div/div[1]/table/tbody/tr[4]/td[1]')
        select_date.click()
        time.sleep(5)

    def marital_status(self):
        select_marital_status = self.driver.find_element(By.ID, "party_martial_status")
        marital_dd = Select(select_marital_status)
        marital_dd.select_by_index(2)
        time.sleep(2)

        select_family_role = self.driver.find_element(By.ID, "party_familyr")
        family_dd = Select(select_family_role)
        family_dd.select_by_index(3)
        time.sleep(2)

    def holder_address(self, address):
        holder_address = self.driver.find_element(By.ID, "parcel_form_person_address")
        holder_address.send_keys(address)

    # select disability information
    def disability_info(self):
        disability = self.driver.find_element(By.ID, "party_phyimpairme")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", disability)
        disability_dd = Select(disability)
        disability_dd.select_by_index(0)
        time.sleep(2)

    def family_status(self):
        orphan = self.driver.find_element(By.ID, "party_isorphan")
        orphan_dd = Select(orphan)
        orphan_dd.select_by_index(0)
        time.sleep(5)

        # click on attachment and attach Id information

    def Id_Information(self, uploadid, idreference):
        attachment = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH,  "//a[normalize-space()='Attachment']"))
        )
        self.driver.execute_script("arguments[0].click();", attachment)

        # attach ID
        attach_id = self.driver.find_element(By.ID, "id_doc")
        attach_id.send_keys(uploadid)

        # add reference for the ID
        fill_id_reference = self.driver.find_element(By.ID, "id_doc_ref")
        self.driver.execute_script("arguments[0].scrollIntoView();", fill_id_reference)
        time.sleep(3)
        fill_id_reference.send_keys(idreference)

    def save_third_party_info(self):
        save_button = self.driver.find_element(By.XPATH, "//button[normalize-space()='Save']")
        self.driver.execute_script("arguments[0].click();", save_button)
        time.sleep(5)
        #
        # # click next button
        # next_button = self.driver.find_element(By.XPATH,
        #                                        "//div[@id='step-holders']//i[@class='fa fa-angle-double-right']")
        # self.driver.execute_script("arguments[0].click();", next_button)
        # time.sleep(5)

    # def add_pom(self, pomdoc, add_pom_ref):
    #     add_pom_doc = self.driver.find_element(By.XPATH, "//input[@id='pom_doc']")
    #     add_pom_doc.send_keys(pomdoc)
    #     time.sleep(5)
    #     add_pom_reference = self.driver.find_element(By.ID, "pom_doc_ref")
    #     add_pom_reference.send_keys(add_pom_ref)
    #     time.sleep(5)
    #     save_holder_info = self.driver.find_element(By.XPATH,
    #                                                 "//button[contains(@onclick, 'partyPicker.validateAndSaveParty')]")
    #     self.driver.execute_script("arguments[0].click();", save_holder_info)
    #     time.sleep(5)

    def add_third_party(self, fname, fathername, gfname,  address, uploadid, idreference):
        self.add_holder_profile(fname, fathername, gfname)
        self.add_DOB()
        self.marital_status()
        self.holder_address(address)
        self.disability_info()
        self.family_status()
        self.Id_Information(uploadid, idreference)
        self.save_third_party_info()
        # self.add_pom(pomdoc,add_pom_ref)



