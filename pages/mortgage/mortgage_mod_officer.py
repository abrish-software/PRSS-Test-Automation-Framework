import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from base.base_driver import BaseDriver
from utilities.application_description import AppDesc
from utilities.load_parcel import LoadParcel
from utilities.tenant_info import TenantInfo


class MortgageModOfficer(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.waitforaddparcel = BaseDriver(self.driver)
        self.appdesc = AppDesc(self.driver)
        self.loadparcel = LoadParcel(self.driver)
        self.tenant = TenantInfo(self.driver)

    def select_mortgage_modification_transaction(self):
        mortgage_transaction = self.driver.find_element(By.XPATH, "//p[normalize-space()='10']")
        self.driver.execute_script("arguments[0].click();", mortgage_transaction)
        time.sleep(3)
        mortgage_mod_transaction = self.driver.find_element(By.XPATH, "//a[normalize-space()='Modify Mortgage']")
        self.driver.execute_script("arguments[0].click();", mortgage_mod_transaction)
        time.sleep(5)

    def mortgage_mod_application_description(self, mmapplicationdescription):
        self.appdesc.application_description(mmapplicationdescription)
        # bapp_d = self.driver.find_element(By.ID, "app_description")
        # bapp_d.send_keys(bapplicationdescription)
        # time.sleep(5)
        # next_b = self.driver.find_element(By.ID, "nextToSecond")
        # self.driver.execute_script("arguments[0].click();", next_b)
        # time.sleep(5)

    def load_parcel_info(self, firstname, fathername, gfname):
        self.loadparcel.load_parcel_infromation(firstname, fathername, gfname)

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
        go_to_third = self.driver.find_element(By.ID, 'nextToThird')
        self.driver.execute_script("arguments[0].click();", go_to_third)
        time.sleep(5)

    def select_mortgage(self):
        parcel = self.driver.find_element(By.XPATH, "//td/input[@type='checkbox' and @field='select']")
        self.driver.execute_script("arguments[0].click();", parcel)
        time.sleep(5)

    def next_to_fourth(self):
        go_to_fourth = self.driver.find_element(By.ID, 'nextToFourth')
        self.driver.execute_script("arguments[0].click();", go_to_fourth)
        time.sleep(5)

    # def add_financial_inst(self, fname, fphone, faddress, fdesc): financial_inst = self.driver.find_element(By.ID,
    # "fi_instituation_add") self.driver.execute_script("arguments[0].click();", financial_inst) time.sleep(5)
    # financial_inst_name = self.driver.find_element(By.ID, "financial_instituation_name")
    # financial_inst_name.send_keys(fname) time.sleep(3) financial_inst_phone = self.driver.find_element(By.ID,
    # "financial_institution_phone") financial_inst_phone.send_keys(fphone) time.sleep(3) financial_inst_address =
    # self.driver.find_element(By.ID, "financial_institution_address") financial_inst_address.send_keys(faddress)
    # time.sleep(3) financial_inst_descr = self.driver.find_element(By.ID, "financial_institution_description")
    # self.driver.execute_script("arguments[0].scrollIntoView(true);", financial_inst_descr) time.sleep(2)
    # financial_inst_descr.send_keys(fdesc) time.sleep(5) save_profile = self.driver.find_element(By.XPATH,
    # "//button[contains(@class, 'btn-nrlais') and text()='Save']") self.driver.execute_script("arguments[0].click(
    # );", save_profile) time.sleep(3)

    def mortgage_amount(self, mortgageamount):
        add_amount = self.driver.find_element(By.ID, "txt_amount")
        add_amount.clear()
        add_amount.send_keys(mortgageamount)
        time.sleep(5)

    def next_to_fifth(self):
        go_to_fifth = self.driver.find_element(By.ID, "nextToFiveth")
        self.driver.execute_script("arguments[0].click();", go_to_fifth)
        time.sleep(3)

    def add_blocking_letter(self, uploadBL, BLreference, BLdescription):
        add_BL = self.driver.find_element(By.XPATH, '//*[@id="row_1"]/td[5]/a')
        upload_doc = self.driver.find_element(By.ID, "upload_doc_req")
        add_doc_ref = self.driver.find_element(By.ID, "doc_reference_req")
        add_doc_description = self.driver.find_element(By.ID, "doc_description_req")
        add_req_documents = self.driver.find_element(By.CSS_SELECTOR, "#add_req_document > div > div > "
                                                                      "div.modal-footer > div > button")
        # next_to_save = self.driver.find_element(By.CSS_SELECTOR, "button#doc_nextbtn")
        self.driver.execute_script("arguments[0].click();", add_BL)
        time.sleep(5)
        upload_doc.send_keys(uploadBL)
        time.sleep(5)
        add_doc_ref.send_keys(BLreference)
        time.sleep(5)
        add_doc_description.send_keys(BLdescription)
        time.sleep(5)
        # add_req_documents.click()
        self.driver.execute_script("arguments[0].click();", add_req_documents)
        # add_req_documents.send_keys(Keys.ENTER)
        time.sleep(5)

    def next_to_final(self):
        go_to_final = self.driver.find_element(By.XPATH, '//*[@id="step-5"]/div/div[1]/div/button[2]')
        self.driver.execute_script("arguments[0].click();", go_to_final)
        time.sleep(5)

    def save_transaction(self):
        reg_transaction = self.driver.find_element(By.ID, "doc_nextbtn")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", reg_transaction)
        time.sleep(5)
        self.driver.execute_script("arguments[0].click();", reg_transaction)
        time.sleep(10)

        # click on ok button
        click_ok = self.driver.find_element(By.XPATH, "//button[@class='btn btn-primary']")
        self.driver.execute_script("arguments[0].click();", click_ok)
        time.sleep(3)

    def register_mortgage_mod_transaction(self, mmapplicationdescription, firstname, fathername,
                                          gfname, idfile, idtext, pomfile, pomreference, pomdescription,
                                          mortgageamount, uploadBL,
                                          BLreference, BLdescription):
        self.select_mortgage_modification_transaction()
        self.mortgage_mod_application_description(mmapplicationdescription)
        self.load_parcel_info(firstname, fathername, gfname)
        self.applicant_id_info(idfile, idtext)
        self.applicant_POM_info(pomfile, pomreference, pomdescription)
        self.next_to_third()
        self.select_mortgage()
        self.next_to_fourth()
        self.mortgage_amount(mortgageamount)
        self.next_to_fifth()
        self.add_blocking_letter(uploadBL, BLreference, BLdescription)
        self.next_to_final()
        self.save_transaction()
