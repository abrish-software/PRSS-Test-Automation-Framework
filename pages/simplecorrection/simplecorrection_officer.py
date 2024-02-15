import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from base.base_driver import BaseDriver
from utilities.add_wife import WifeParty
from utilities.application_description import AppDesc
from utilities.load_parcel import LoadParcel


class SimpCorrectionOfficer(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.waitforelement = BaseDriver(self.driver)
        self.appdesc = AppDesc(self.driver)
        self.loadparcel = LoadParcel(self.driver)
        self.wifeinfo = WifeParty(self.driver)

    def select_simple_correction_transaction(self):
        time.sleep(5)
        simple_correction_transaction = self.driver.find_element(By.XPATH, "//p[normalize-space()='17']")
        self.driver.execute_script("arguments[0].click();", simple_correction_transaction)
        time.sleep(5)

    # def select_kebele(self):
    #     kebele = self.driver.find_element(By.ID, "app_kebele")
    #     kebele_dd = Select(kebele)
    #     kebele_dd.select_by_index(3)
    #     time.sleep(2)

    def simp_correction_application_description(self, sapplicationdescription):
        self.appdesc.application_description(sapplicationdescription)
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

    def applicant_id_info(self, idfile, idtext):
        self.driver.implicitly_wait(100)
        add_id_info = self.driver.find_element(By.XPATH, '//td[@id="idrep_btn"]/a[@id="add_id"]')
        add_id_file = self.driver.find_element(By.ID, "id_file")
        select_id_type = self.driver.find_element(By.ID, "id_type")
        add_id_text = self.driver.find_element(By.ID, "id_text")
        add_id_content = self.driver.find_element(By.XPATH, "//a[@class='btn btn-nrlais' and "
                                                            "@href='javascript:applicantPicker.validateAndSaveID()']")
        time.sleep(5)
        self.driver.execute_script("arguments[0].click();", add_id_info)
        time.sleep(5)
        add_id_file.send_keys(idfile)
        time.sleep(5)
        select_id_dd = Select(select_id_type)
        select_id_dd.select_by_index(1)
        time.sleep(5)
        add_id_text.send_keys(idtext)
        time.sleep(5)
        self.driver.execute_script("arguments[0].click();", add_id_content)
        time.sleep(5)

    def applicant_POM_info(self, pomfile, pomreference, pomdescription):
        marriage_proof = self.driver.find_element(By.XPATH, '//td[@id="pom_btn"]/a[@id="add_id"]')
        self.driver.execute_script("arguments[0].click();", marriage_proof)
        time.sleep(5)
        pom_file = self.driver.find_element(By.ID, "pom_file")
        pom_file.send_keys(pomfile)
        time.sleep(5)
        pom_reference = self.driver.find_element(By.XPATH, '//div//input[@type="text" and @id="pom_ref"]')
        pom_reference.send_keys(pomreference)
        time.sleep(5)
        pom_description = self.driver.find_element(By.XPATH, '//div//input[@type="text" and @id="pom_text"]')
        pom_description.send_keys(pomdescription)
        time.sleep(5)
        save_pom = self.driver.find_element(By.XPATH, '//*[@id="add_pom_content"]/div/div/div[3]/div/a')
        self.driver.execute_script("arguments[0].click();", save_pom)
        time.sleep(5)

    def next_to_third(self):
        go_to_third = self.driver.find_element(By.ID, 'doc_nextbtn')
        self.driver.execute_script("arguments[0].click();", go_to_third)
        time.sleep(5)

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

    def next_to_final(self):
        go_to_fourth = self.driver.find_element(By.ID, "doc_nextbtn")
        self.driver.execute_script("arguments[0].click();", go_to_fourth)
        time.sleep(5)

    def save_transaction(self):
        reg_transaction = self.driver.find_element(By.XPATH, "//div[@class='align-right']//button[@id='doc_nextbtn']")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", reg_transaction)
        time.sleep(5)
        self.driver.execute_script("arguments[0].click();", self.waitforelement.wait_until_element_to_be_clickable(By.XPATH,
                                                                                                                   "//div[@class='align-right']//button[@id='doc_nextbtn']"))
        time.sleep(10)

        # click on ok button
        click_ok = self.driver.find_element(By.XPATH, "//button[@class='btn btn-primary']")
        self.driver.execute_script("arguments[0].click();", click_ok)
        time.sleep(3)

    # register boundary correction transaction
    def register_simple_correction_transaction(self, sapplicationdescription, firstname, fathername,
                                               gfname, idfile, idtext, pomfile, pomreference, pomdescription,
                                               uploadLHC, addLHCreference, addLHCdescription):
        self.select_simple_correction_transaction()
        self.simp_correction_application_description(sapplicationdescription)
        self.load_parcel(firstname, fathername, gfname)
        self.applicant_id_info(idfile, idtext)
        self.applicant_POM_info(pomfile, pomreference, pomdescription)
        self.next_to_third()
        self.add_holding(uploadLHC, addLHCreference, addLHCdescription)
        self.next_to_final()
        self.save_transaction()
