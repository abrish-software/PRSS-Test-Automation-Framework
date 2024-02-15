import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from base.base_driver import BaseDriver
from utilities.application_description import AppDesc
from utilities.load_parcel import LoadParcel


class BoundaryOfficer(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.waitforaddparcel = BaseDriver(self.driver)
        self.appdesc = AppDesc(self.driver)
        self.loadparcel = LoadParcel(self.driver)

    def select_boundary_correction(self):
        time.sleep(5)
        boundary_correction = self.driver.find_element(By.XPATH, '//*[@id="transaction_menu"]/div[1]/article/a')
        self.driver.execute_script("arguments[0].click();", boundary_correction)
        time.sleep(5)

    def boundary_application_description(self, bapplicationdescription):
        self.appdesc.application_description(bapplicationdescription)

    def load_parcel(self, firstname, fathername, gfname):
        self.loadparcel.load_parcel_infromation(firstname, fathername, gfname)

    def add_marital_status(self, pocfile, pocref, poctext):
        add_marital_info = self.driver.find_element(By.XPATH, '//td[@id="pom_btn"]/a[@class="btn btn-nrlais popper"]')
        add_poc_file = self.driver.find_element(By.ID, "pom_file")
        add_poc_reference = self.driver.find_element(By.CSS_SELECTOR, "input#pom_ref")
        add_poc_text = self.driver.find_element(By.CSS_SELECTOR, "input#pom_text")
        add_poc_content = self.driver.find_element(By.XPATH, "//a[@class='btn btn-nrlais' and "
                                                             "@href=\"javascript:applicantPicker.validateAndSavePOM("
                                                             ")\"]")

        self.driver.execute_script("arguments[0].click();", add_marital_info)
        time.sleep(5)
        add_poc_file.send_keys(pocfile)
        time.sleep(5)
        add_poc_reference.send_keys(pocref)
        time.sleep(5)
        add_poc_text.send_keys(poctext)
        time.sleep(5)
        self.driver.execute_script("arguments[0].click();", add_poc_content)
        time.sleep(5)

    def add_ID(self, idfile, idtext):
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

    def next_to_third(self):
        go_to_third = self.driver.find_element(By.ID, "nextToThird")
        self.driver.execute_script("arguments[0].click();", go_to_third)
        time.sleep(5)

    def select_parcel(self):
        select_parcel_info = self.driver.find_element(By.XPATH, "//input[@type='checkbox' and @field='select']")
        time.sleep(5)
        self.driver.execute_script("arguments[0].click();", select_parcel_info)
        time.sleep(5)
        next_to_fourth = self.driver.find_element(By.CSS_SELECTOR, "button#doc_nextbtn")
        time.sleep(5)
        self.driver.execute_script("arguments[0].click();", next_to_fourth)
        time.sleep(5)
        next_to_holding = self.driver.find_element(By.ID, "doc_nextbtn")
        self.driver.execute_script("arguments[0].click();", next_to_holding)
        time.sleep(5)

    # add land holding certeficate
    def add_holding(self, uploadLHC, addLHCreference, addLHCdescription):
        add_LHC = self.driver.find_element(By.XPATH, '//*[@id="row_1"]/td[5]/a')
        upload_doc = self.driver.find_element(By.ID, "upload_doc_req")
        add_doc_ref = self.driver.find_element(By.ID, "doc_reference_req")
        add_doc_description = self.driver.find_element(By.ID, "doc_description_req")
        add_req_documents = self.driver.find_element(By.CSS_SELECTOR, "#add_req_document > div > div > "
                                                                      "div.modal-footer > div > button")
        next_to_save = self.driver.find_element(By.CSS_SELECTOR, "button#doc_nextbtn")

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
        time.sleep(10)
        self.driver.execute_script("arguments[0].click();", next_to_save)
        time.sleep(5)

    # save_transactipon
    def save_transaction(self):
        reg_transaction = self.driver.find_element(By.ID, "Save_transaction")
        self.driver.execute_script("arguments[0].click();", reg_transaction)
        time.sleep(10)

        # click on ok button
        click_ok = self.driver.find_element(By.XPATH, "//button[@class='btn btn-primary']")
        self.driver.execute_script("arguments[0].click();", click_ok)
        time.sleep(3)

    # register boundary correction transaction
    def register_boundary_correction(self, bapplicationdescription, firstname, fathername,
                                     gfname, pocfile, pocref, poctext, idfile, idtext, uploadLHC, addLHCreference,
                                     addLHCdescription):
        self.select_boundary_correction()
        self.boundary_application_description(bapplicationdescription)
        self.load_parcel(firstname, fathername, gfname)
        self.add_marital_status(pocfile, pocref, poctext)
        self.add_ID(idfile, idtext)
        self.next_to_third()
        self.select_parcel()
        self.add_holding(uploadLHC, addLHCreference, addLHCdescription)
        self.save_transaction()
