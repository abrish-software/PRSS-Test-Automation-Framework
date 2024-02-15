import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_driver import BaseDriver


class WifeParty(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wp = BaseDriver(self.driver)

    # def select_special_case(self):
    #     time.sleep(5)
    #     special_case = self.driver.find_element(By.XPATH, "//p[normalize-space()='Special Case']")
    #     self.driver.execute_script("arguments[0].click();", special_case)
    #     time.sleep(5)
    #
    # # select Kebele
    # def select_kebele(self):
    #     # select kebele
    #     select_kebele = self.driver.find_element(By.ID, "special_case_kebele")
    #     kebele_dd = Select(select_kebele)
    #     kebele_dd.select_by_index(3)
    #     time.sleep(2)
    #
    # # fill in the application description and click next button
    # def application_description(self, applicationdescription):
    #     app_d = self.driver.find_element(By.ID, "app_description")
    #     app_d.send_keys(applicationdescription)
    #     time.sleep(5)
    #     next_b = self.driver.find_element(By.ID, "nextToSecond")
    #     self.driver.execute_script("arguments[0].click();", next_b)
    #     time.sleep(5)

    # click on Add holders button to add holder information
    def add_wife_info(self, wfirstname, wfathername, wgfname):
        # self.driver.execute_script("arguments[0].click();", self.wp.wait_until_presence_of_element_located(By.ID,
        #                                                                                                    "special_case_beneficiary_add"))
        #
        # # Add holder Information
        # time.sleep(5)
        add_first_name = self.driver.find_element(By.ID, "party_firstname")
        add_first_name.send_keys(wfirstname)
        time.sleep(3)
        add_father_name = self.driver.find_element(By.ID, "party_fathername")
        add_father_name.send_keys(wfathername)
        time.sleep(3)
        add_gfather_name = self.driver.find_element(By.ID, "party_gfathername")
        add_gfather_name.send_keys(wgfname)
        time.sleep(3)

    def select_gender(self):
        gender = self.driver.find_element(By.ID, "party_sex_female")
        self.driver.execute_script("arguments[0].click();", gender)
        time.sleep(2)

    # click the holder birth information
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

    # select marital_status and family role
    def marital_status(self):
        select_marital_status = self.driver.find_element(By.ID, "party_martial_status")
        marital_dd = Select(select_marital_status)
        marital_dd.select_by_index(3)
        time.sleep(2)

        select_family_role = self.driver.find_element(By.ID, "party_familyr")
        family_dd = Select(select_family_role)
        family_dd.select_by_index(2)
        time.sleep(2)

    # fill the address
    def holder_address(self, waddress):
        holder_address = self.driver.find_element(By.ID, "parcel_form_person_address")
        holder_address.send_keys(waddress)

    # select disability information
    def disability_info(self):
        disability = self.driver.find_element(By.ID, "party_phyimpairme")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", disability)
        disability_dd = Select(disability)
        disability_dd.select_by_index(0)
        time.sleep(2)

    # select family status
    def family_status(self):
        orphan = self.driver.find_element(By.ID, "party_isorphan")
        orphan_dd = Select(orphan)
        orphan_dd.select_by_index(0)
        time.sleep(5)

    # add share information
    def share_information(self, wshare_info):
        share = self.driver.find_element(By.ID, "party_share")
        share.clear()  # This line clears the existing text in the field
        share.send_keys(wshare_info)
        time.sleep(5)

    # click on attachment and attach Id information
    def Id_Information(self, wuploadid, widreference):
        # attachment = WebDriverWait(self.driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "//li[@id='special_case_beneficiaries_party_picker_attachement-tab"
        #                                           "']/a"))
        # )
        self.driver.execute_script("arguments[0].click();", self.wp.wait_until_presence_of_element_located(By.XPATH,
                                                                                                           "//a["
                                                                                                           "normalize"
                                                                                                           "-space("
                                                                                                           ")='Attachment']"))
        # attach ID
        attach_id = self.driver.find_element(By.ID, "id_doc")
        attach_id.send_keys(wuploadid)
        time.sleep(3)
        # add reference for the ID
        fill_id_reference = self.driver.find_element(By.ID, "id_doc_ref")
        self.driver.execute_script("arguments[0].scrollIntoView();", fill_id_reference)
        time.sleep(3)
        fill_id_reference.send_keys(widreference)

        # save the information
        save_button = self.driver.find_element(By.XPATH, "//button[normalize-space()='Save']")
        self.driver.execute_script("arguments[0].click();", save_button)
        time.sleep(5)

        # click next button
        # next_button = self.driver.find_element(By.XPATH,
        #                                        "//div[@id='step-holders']//i[@class='fa fa-angle-double-right']")
        # self.driver.execute_script("arguments[0].click();", next_button)
        # time.sleep(5)

    # # add claim resolution document
    # def claim_resolution(self, uploadclaim, claimreference, claimdescription):
    #     add_claim = self.driver.find_element(By.XPATH, '//*[@id="row_1"]/td[5]/a')
    #     self.driver.execute_script("arguments[0].click();", add_claim)
    #     time.sleep(5)
    #     attach_claim = self.driver.find_element(By.ID, "upload_doc_req")
    #     attach_claim.send_keys(uploadclaim)
    #     time.sleep(5)
    #
    #     # add document reference
    #     add_docr = self.driver.find_element(By.ID, "doc_reference_req")
    #     add_docr.send_keys(claimreference)
    #     time.sleep(5)
    #
    #     # add document description
    #     add_docd = self.driver.find_element(By.ID, "doc_description_req")
    #     add_docd.send_keys(claimdescription)
    #     time.sleep(10)
    #
    #     # add claim resolution doc
    #     add_CR = self.driver.find_element(By.XPATH, "//button[@class='btn btn-nrlais' and "
    #                                                 "@onclick='documentPicker.validateAndSaveDocument()']")
    #     self.driver.execute_script("arguments[0].click();", add_CR)
    #     time.sleep(5)
    #
    # # upload proof of holding
    # def holding_proof(self, uploadholding, holdingreference, holdingdescription):
    #
    #     # click on + button
    #     click_upload_id = self.driver.find_element(By.XPATH, '//*[@id="row_2"]/td[5]/a/i')
    #     self.driver.execute_script("arguments[0].click();", click_upload_id)
    #     time.sleep(5)
    #
    #     upload_proofh = self.driver.find_element(By.ID, "upload_doc_req")
    #     upload_proofh.send_keys(uploadholding)
    #     time.sleep(5)
    #
    #     # add reference
    #     add_r = self.driver.find_element(By.ID, "doc_reference_req")
    #     add_r.send_keys(holdingreference)
    #     time.sleep(5)
    #
    #     # add_description_document
    #     add_description = self.driver.find_element(By.ID, "doc_description_req")
    #     add_description.send_keys(holdingdescription)
    #     time.sleep(5)
    #
    #     # add proof of holding
    #     add_POH = self.driver.find_element(By.CSS_SELECTOR,
    #                                        "button.btn.btn-nrlais[onclick='documentPicker.validateAndSaveDocument()']")
    #     self.driver.execute_script("arguments[0].click();", add_POH)
    #     time.sleep(3)
    #     # click next button
    #     next_b = self.driver.find_element(By.ID, 'doc_nextbtn')
    #     self.driver.execute_script("arguments[0].click();", next_b)
    #     time.sleep(3)
    #
    # def click_on_reg_transaction(self):
    #     reg_t = self.driver.find_element(By.ID, 'save_transaction')
    #     self.driver.execute_script("arguments[0].click();", reg_t)
    #     time.sleep(6)
    #
    #     # click on ok button
    #     click_ok = self.driver.find_element(By.XPATH, "//button[@class='btn btn-primary']")
    #     self.driver.execute_script("arguments[0].click();", click_ok)
    #     time.sleep(3)
    #
    # # save special case transaction for one holder
    def register_wife_Information(self, wfirstname, wfathername, wgfname, whaddress, wshareinfo, wuploadid,
                                  widreference):
        # self.select_special_case()
        # self.select_kebele()
        # self.application_description(appdescription)
        self.add_wife_info(wfirstname, wfathername, wgfname)
        self.select_gender()
        self.add_DOB()
        self.marital_status()
        self.holder_address(whaddress)
        self.disability_info()
        self.family_status()
        self.share_information(wshareinfo)
        self.Id_Information(wuploadid, widreference)
        # self.claim_resolution(claimupload, claimrefrence, claimdescription)
        # self.holding_proof(uploadholding, holdingreference, holdingdescription)
        # self.click_on_reg_transaction()
    #
    #
