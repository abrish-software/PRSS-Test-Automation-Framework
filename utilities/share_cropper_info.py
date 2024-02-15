import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from base.base_driver import BaseDriver
from selenium.webdriver.support import expected_conditions as EC


class ShareCrpperInfo(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        # self.wait = wait
        self.waitforaddparcel = BaseDriver(self.driver)

    def add_share_cropper_profile(self, shcfname, shcfathername, shcgfname):
        add_holder = self.driver.find_element(By.ID, "share_cropping_tenant_add")
        self.driver.execute_script("arguments[0].click();", add_holder)
        # Add holder Information
        time.sleep(5)
        add_first_name = self.driver.find_element(By.ID, "party_firstname")
        add_first_name.send_keys(shcfname)
        time.sleep(3)
        add_father_name = self.driver.find_element(By.ID, "party_fathername")
        add_father_name.send_keys(shcfathername)
        time.sleep(3)
        add_gfather_name = self.driver.find_element(By.ID, "party_gfathername")
        add_gfather_name.send_keys(shcgfname)
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

    def holder_address(self, shcaddress):
        holder_address = self.driver.find_element(By.ID, "parcel_form_person_address")
        holder_address.send_keys(shcaddress)

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
            EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Attachment']"))
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

    def save_share_cropper_info(self):
        save_button = self.driver.find_element(By.XPATH, "//button[normalize-space()='Save']")
        self.driver.execute_script("arguments[0].click();", save_button)
        time.sleep(5)

    def add_share_cropper(self, shcfname, shcfathername, shcgfname, shcaddress, uploadid, idreference):
        self.add_share_cropper_profile(shcfname, shcfathername, shcgfname)
        self.add_DOB()
        self.marital_status()
        self.holder_address(shcaddress)
        self.disability_info()
        self.family_status()
        self.Id_Information(uploadid, idreference)
        self.save_share_cropper_info()
