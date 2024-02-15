import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from base.base_driver import BaseDriver
from utilities.add_wife import WifeParty
from utilities.application_description import AppDesc
from utilities.load_parcel import LoadParcel


class SplitOfficer(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.waitforaddparcel = BaseDriver(self.driver)
        self.appdesc = AppDesc(self.driver)
        self.loadparcel = LoadParcel(self.driver)
        self.wifeinfo = WifeParty(self.driver)

    def select_split_transaction(self):
        time.sleep(5)
        split_transaction = self.driver.find_element(By.XPATH, "//p[normalize-space()='Split Parcel']")
        self.driver.execute_script("arguments[0].click();", split_transaction)
        time.sleep(5)

    # def select_kebele(self):
    #     kebele = self.driver.find_element(By.ID, "app_kebele")
    #     kebele_dd = Select(kebele)
    #     kebele_dd.select_by_index(3)
    #     time.sleep(2)

    def split_application_description(self, sapplicationdescription):
        self.appdesc.application_description(sapplicationdescription)
        # bapp_d = self.driver.find_element(By.ID, "app_description")
        # bapp_d.send_keys(bapplicationdescription)
        # time.sleep(5)
        # next_b = self.driver.find_element(By.ID, "nextToSecond")
        # self.driver.execute_script("arguments[0].click();", next_b)
        # time.sleep(5)

    def load_parcel(self, firstname):
        self.loadparcel.load_parcel()
        first_name = self.driver.find_element(By.ID, "sea_name")
        first_name.send_keys(firstname)
        select_kebele = self.driver.find_element(By.ID, "sea_kebele")
        kebele_dd = Select(select_kebele)
        kebele_dd.select_by_index(3)
        time.sleep(2)
        search_button = self.driver.find_element(By.XPATH, '//*[@id="sea_form"]/div[2]/button')
        self.driver.execute_script("arguments[0].click();", search_button)
        time.sleep(10)
        self.loadparcel.add_parcel()

    def next_to_second(self):
        self.loadparcel.next_button()

    def first_holder_id_info(self, fhidfile, fhidtext):
        self.driver.implicitly_wait(100)
        add_id_info = self.driver.find_element(By.XPATH, '//tr[1]/td[@id="idrep_btn"]/a')
        add_id_file = self.driver.find_element(By.ID, "id_file")
        select_id_type = self.driver.find_element(By.ID, "id_type")
        add_id_text = self.driver.find_element(By.ID, "id_text")
        add_id_content = self.driver.find_element(By.XPATH, "//a[@class='btn btn-nrlais' and "
                                                            "@href='javascript:applicantPicker.validateAndSaveID()']")
        time.sleep(5)
        self.driver.execute_script("arguments[0].click();", add_id_info)
        time.sleep(5)
        add_id_file.send_keys(fhidfile)
        time.sleep(5)
        select_id_dd = Select(select_id_type)
        select_id_dd.select_by_index(1)
        time.sleep(5)
        add_id_text.send_keys(fhidtext)
        time.sleep(5)
        self.driver.execute_script("arguments[0].click();", add_id_content)
        time.sleep(5)

    def second_holder_id_info(self, shidfile, shidtext):
        self.driver.implicitly_wait(100)
        add_id_info = self.driver.find_element(By.XPATH, '//tr[2]/td[@id="idrep_btn"]/a')
        add_id_file = self.driver.find_element(By.ID, "id_file")
        select_id_type = self.driver.find_element(By.ID, "id_type")
        add_id_text = self.driver.find_element(By.ID, "id_text")
        add_id_content = self.driver.find_element(By.XPATH, "//a[@class='btn btn-nrlais' and "
                                                            "@href='javascript:applicantPicker.validateAndSaveID()']")
        time.sleep(5)
        self.driver.execute_script("arguments[0].click();", add_id_info)
        time.sleep(5)
        add_id_file.send_keys(shidfile)
        time.sleep(5)
        select_id_dd = Select(select_id_type)
        select_id_dd.select_by_index(1)
        time.sleep(5)
        add_id_text.send_keys(shidtext)
        time.sleep(5)
        self.driver.execute_script("arguments[0].click();", add_id_content)
        time.sleep(5)

    def next_to_third_page(self):
        go_to_third = self.driver.find_element(By.ID, "nextToThird")
        self.driver.execute_script("arguments[0].click();", go_to_third)
        time.sleep(5)

    def next_to_fourth_page(self):
        go_to_fourth = self.driver.find_element(By.XPATH, '//*[@id="step-3"]/div/div[2]/div/button')
        self.driver.execute_script("arguments[0].click();", go_to_fourth)
        time.sleep(5)

    # def add_divorce_proof(self, divorcefile, divorceref, divorcedesc):
    #     add_proof = self.driver.find_element(By.XPATH, '//*[@id="row_1"]/td[5]/a')
    #     self.driver.execute_script("arguments[0].click();", add_proof)
    #     time.sleep(5)
    #     upload_divorce = self.driver.find_element(By.ID, "upload_doc_req")
    #     add_div_ref = self.driver.find_element(By.ID, "doc_reference_req")
    #     add_div_description = self.driver.find_element(By.ID, "doc_description_req")
    #     add_div_documents = self.driver.find_element(By.CSS_SELECTOR, "#add_req_document > div > div > "
    #                                                                   "div.modal-footer > div > button")
    #     upload_divorce.send_keys(divorcefile)
    #     time.sleep(5)
    #     add_div_ref.send_keys(divorceref)
    #     time.sleep(5)
    #     add_div_description.send_keys(divorcedesc)
    #     time.sleep(5)
    #     # add_req_documents.click()
    #     self.driver.execute_script("arguments[0].click();", add_div_documents)
    #     # add_req_documents.send_keys(Keys.ENTER)
    #     time.sleep(5)
    #     # self.driver.execute_script("arguments[0].click();", next_to_save)
    #     # time.sleep(5)
    #
    # def add_claim(self, crfile, crreference, crdescription):
    #     claim_resolution = self.driver.find_element(By.XPATH, '//*[@id="row_2"]/td[5]/a')
    #     self.driver.execute_script("arguments[0].click();", claim_resolution)
    #     time.sleep(5)
    #     claim_file = self.driver.find_element(By.ID, "upload_doc_req")
    #     claim_file.send_keys(crfile)
    #     time.sleep(5)
    #     claim_reference = self.driver.find_element(By.ID, "doc_reference_req")
    #     claim_reference.send_keys(crreference)
    #     time.sleep(5)
    #     claim_description = self.driver.find_element(By.ID, "doc_description_req")
    #     claim_description.send_keys(crdescription)
    #     time.sleep(5)
    #     save_claim = self.driver.find_element(By.XPATH, '//*[@id="add_req_document"]/div/div/div[3]/div/button')
    #     self.driver.execute_script("arguments[0].click();", save_claim)
    #     time.sleep(5)

    def add_holding(self, uploadLHC, addLHCreference, addLHCdescription):
        add_LHC = self.driver.find_element(By.XPATH, '//*[@id="row_1"]/td[5]/a')
        upload_doc = self.driver.find_element(By.ID, "upload_doc_req")
        add_doc_ref = self.driver.find_element(By.ID, "doc_reference_req")
        add_doc_description = self.driver.find_element(By.ID, "doc_description_req")
        add_req_documents = self.driver.find_element(By.CSS_SELECTOR, "#add_req_document > div > div > "
                                                                      "div.modal-footer > div > button")
        # next_to_save = self.driver.find_element(By.CSS_SELECTOR, "button#doc_nextbtn")
        self.driver.execute_script("arguments[0].click();", add_LHC)
        time.sleep(5)
        upload_doc.send_keys(uploadLHC)
        time.sleep(5)
        add_doc_ref.send_keys(addLHCreference)
        time.sleep(5)
        add_doc_description.send_keys(addLHCdescription)
        time.sleep(5)
        # add_req_documents.click()
        self.driver.execute_script("arguments[0].click();", add_req_documents)
        # add_req_documents.send_keys(Keys.ENTER)
        time.sleep(5)

    def to_final_step(self):
        final = self.driver.find_element(By.ID, "doc_nextbtn")
        self.driver.execute_script("arguments[0].click();", final)
        time.sleep(5)

    def save_transaction(self):
        reg_transaction = self.driver.find_element(By.ID, "button_save_transaction")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", reg_transaction)
        time.sleep(5)
        self.driver.execute_script("arguments[0].click();", reg_transaction)
        time.sleep(10)

        # click on ok button
        click_ok = self.driver.find_element(By.XPATH, "//button[@class='btn btn-primary']")
        self.driver.execute_script("arguments[0].click();", click_ok)
        time.sleep(3)

    # register boundary correction transaction
    def register_split_transaction(self, sapplicationdescription, firstname, fhidfile, fhidtext,
                                     shidfile, shidtext, uploadLHC, addLHCreference, addLHCdescription):
        self.select_split_transaction()
        self.split_application_description(sapplicationdescription)
        self.load_parcel(firstname)
        self.next_to_second()
        self.first_holder_id_info(fhidfile, fhidtext)
        self.second_holder_id_info(shidfile, shidtext)
        self.next_to_third_page()
        self.next_to_fourth_page()
        self.add_holding(uploadLHC, addLHCreference, addLHCdescription)
        self.to_final_step()
        self.save_transaction()

