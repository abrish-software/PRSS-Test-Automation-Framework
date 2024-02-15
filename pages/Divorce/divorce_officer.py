import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from base.base_driver import BaseDriver
from utilities.add_wife import WifeParty
from utilities.application_description import AppDesc
from utilities.load_parcel import LoadParcel


class DivorceOfficer(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.waitforaddparcel = BaseDriver(self.driver)
        self.appdesc = AppDesc(self.driver)
        self.loadparcel = LoadParcel(self.driver)
        self.wifeinfo = WifeParty(self.driver)

    def select_divorce_transaction(self):
        time.sleep(5)
        divorce_transaction = self.driver.find_element(By.XPATH, "//p[normalize-space()='03']")
        self.driver.execute_script("arguments[0].click();", divorce_transaction)
        time.sleep(5)

    # def select_kebele(self):
    #     kebele = self.driver.find_element(By.ID, "app_kebele")
    #     kebele_dd = Select(kebele)
    #     kebele_dd.select_by_index(3)
    #     time.sleep(2)

    def divorce_application_description(self, dapplicationdescription):
        self.appdesc.application_description(dapplicationdescription)
        # bapp_d = self.driver.find_element(By.ID, "app_description")
        # bapp_d.send_keys(bapplicationdescription)
        # time.sleep(5)
        # next_b = self.driver.find_element(By.ID, "nextToSecond")
        # self.driver.execute_script("arguments[0].click();", next_b)
        # time.sleep(5)

    def load_parcel(self, firstname, fathername, gfname):
        self.loadparcel.load_parcel_infromation(firstname, fathername, gfname)

    # def next_to_second(self):
    #     go_to_second = self.driver.find_element(By.ID, "nextToSecond")
    #     self.driver.execute_script("arguments[0].click();", go_to_second)

    # def add_husband_id(self):

    # def husband_information(self, hfirstname, hfathername, hgfname):
    #     husband_info = self.driver.find_element(By.ID, "pick_husband_btn")
    #     self.driver.execute_script("arguments[0].click();", husband_info)
    #     time.sleep(5)
    #     self.loadparcel.search_Holding(hfirstname, hfathername, hgfname)
    #     self.loadparcel.add_parcel()
    #     time.sleep(5)
    #     select_husband = self.driver.find_element(By.ID, "ap_select")
    #     self.driver.execute_script("arguments[0].click();", select_husband)
    #     time.sleep(3)

    def husband_id_info(self, hidfile, hidtext):
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
        add_id_file.send_keys(hidfile)
        time.sleep(5)
        select_id_dd = Select(select_id_type)
        select_id_dd.select_by_index(1)
        time.sleep(5)
        add_id_text.send_keys(hidtext)
        time.sleep(5)
        self.driver.execute_script("arguments[0].click();", add_id_content)
        time.sleep(5)

    def wife_id_info(self, widfile, widtext):
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
        add_id_file.send_keys(widfile)
        time.sleep(5)
        select_id_dd = Select(select_id_type)
        select_id_dd.select_by_index(1)
        time.sleep(5)
        add_id_text.send_keys(widtext)
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

    def add_divorce_proof(self, divorcefile, divorceref, divorcedesc):
        add_proof = self.driver.find_element(By.XPATH, '//*[@id="row_1"]/td[5]/a')
        self.driver.execute_script("arguments[0].click();", add_proof)
        time.sleep(5)
        upload_divorce = self.driver.find_element(By.ID, "upload_doc_req")
        add_div_ref = self.driver.find_element(By.ID, "doc_reference_req")
        add_div_description = self.driver.find_element(By.ID, "doc_description_req")
        add_div_documents = self.driver.find_element(By.CSS_SELECTOR, "#add_req_document > div > div > "
                                                                      "div.modal-footer > div > button")
        upload_divorce.send_keys(divorcefile)
        time.sleep(5)
        add_div_ref.send_keys(divorceref)
        time.sleep(5)
        add_div_description.send_keys(divorcedesc)
        time.sleep(5)
        # add_req_documents.click()
        self.driver.execute_script("arguments[0].click();", add_div_documents)
        # add_req_documents.send_keys(Keys.ENTER)
        time.sleep(5)
        # self.driver.execute_script("arguments[0].click();", next_to_save)
        # time.sleep(5)

    def add_claim(self, crfile, crreference, crdescription):
        claim_resolution = self.driver.find_element(By.XPATH, '//*[@id="row_2"]/td[5]/a')
        self.driver.execute_script("arguments[0].click();", claim_resolution)
        time.sleep(5)
        claim_file = self.driver.find_element(By.ID, "upload_doc_req")
        claim_file.send_keys(crfile)
        time.sleep(5)
        claim_reference = self.driver.find_element(By.ID, "doc_reference_req")
        claim_reference.send_keys(crreference)
        time.sleep(5)
        claim_description = self.driver.find_element(By.ID, "doc_description_req")
        claim_description.send_keys(crdescription)
        time.sleep(5)
        save_claim = self.driver.find_element(By.XPATH, '//*[@id="add_req_document"]/div/div/div[3]/div/button')
        self.driver.execute_script("arguments[0].click();", save_claim)
        time.sleep(5)

    def add_holding(self, uploadLHC, addLHCreference, addLHCdescription):
        add_LHC = self.driver.find_element(By.XPATH, '//*[@id="row_3"]/td[5]/a')
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
        reg_transaction = self.driver.find_element(By.ID, "save_transaction")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", reg_transaction)
        time.sleep(5)
        self.driver.execute_script("arguments[0].click();", reg_transaction)
        time.sleep(10)

        # click on ok button
        click_ok = self.driver.find_element(By.XPATH, "//button[@class='btn btn-primary']")
        self.driver.execute_script("arguments[0].click();", click_ok)
        time.sleep(3)

    # register boundary correction transaction
    def register_divorce_transaction(self, dapplicationdescription, firstname, fathername,
                                     gfname, hidfile, hidtext,
                                     widfile, widtext, divorcefile, divorceref, divorcedesc,
                                     crfile, crreference, crdescription,
                                     uploadLHC, addLHCreference, addLHCdescription):
        self.select_divorce_transaction()
        self.divorce_application_description(dapplicationdescription)
        self.load_parcel(firstname, fathername, gfname)
        self.husband_id_info(hidfile, hidtext)
        self.wife_id_info(widfile, widtext)
        self.next_to_third_page()
        self.next_to_fourth_page()
        self.add_divorce_proof(divorcefile, divorceref, divorcedesc)
        self.add_claim(crfile, crreference, crdescription)
        self.add_holding(uploadLHC, addLHCreference, addLHCdescription)
        self.to_final_step()
        self.save_transaction()

