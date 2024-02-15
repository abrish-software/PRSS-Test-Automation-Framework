import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from base.base_driver import BaseDriver
from utilities.add_new_holder_info import IdNewHolder
from utilities.add_wife import WifeParty
from utilities.application_description import AppDesc
from utilities.load_parcel import LoadParcel
from utilities.third_party_info import ThirdParty


class ServitudeOfficer(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.waitforelement = BaseDriver(self.driver)
        self.appdesc = AppDesc(self.driver)
        self.loadparcel = LoadParcel(self.driver)
        self.thirdparty = ThirdParty(self.driver)

    def select_servitude_transaction(self):
        time.sleep(5)
        servitude_transaction = self.driver.find_element(By.XPATH, '//*[@id="transaction_menu"]/div[15]/article/a')
        self.driver.execute_script("arguments[0].click();", servitude_transaction)
        time.sleep(5)

    # def select_kebele(self):
    #     kebele = self.driver.find_element(By.ID, "app_kebele")
    #     kebele_dd = Select(kebele)
    #     kebele_dd.select_by_index(3)
    #     time.sleep(2)

    def servitude_application_description(self, sapplicationdescription):
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

    def select_parcel(self):
        parcel = self.driver.find_element(By.XPATH, "//td/input[@type='checkbox']")
        self.driver.execute_script("arguments[0].click();", parcel)
        time.sleep(5)

    def next_to_fourth(self):
        go_to_fourth = self.driver.find_element(By.XPATH, '//*[@id="step-3"]/div/div[2]/div/button')
        self.driver.execute_script("arguments[0].click();", go_to_fourth)
        time.sleep(5)

    def add_third_party(self, pfname, pfathername, pgfname, address, uploadid, idreference):
        self.thirdparty.add_third_party(pfname, pfathername, pgfname, address, uploadid, idreference)

    def next_to_fifth(self):
        go_to_fifth = self.driver.find_element(By.ID, "doc_nextbtn")
        self.driver.execute_script("arguments[0].click();", go_to_fifth)
        time.sleep(5)

    def servitude_detail(self):
        restriction_type = self.driver.find_element(By.ID, "restriction_type")
        restriction_dd = Select(restriction_type)
        restriction_dd.select_by_index(2)
        time.sleep(5)

    def restriction_end_date(self):
        end_date = self.driver.find_element(By.ID, "restrictive_interest_date_end")
        end_date.send_keys(Keys.RETURN)
        time.sleep(5)
        select_year = self.driver.find_element(By.ID, "etdc_year_et")
        year_dd = Select(select_year)
        last_index = len(year_dd.options) - 1
        year_dd.select_by_index(last_index)
        self.driver.execute_script("arguments[0].selectedIndex = arguments[0].options.length - 1;", select_year)
        time.sleep(5)
        select_date = self.driver.find_element(By.XPATH, "//td[@class='etdc_day' and text()='19']")
        self.driver.execute_script("arguments[0].click();", select_date)
        time.sleep(5)

    def next_to_sixth(self):
        go_to_sixth = self.driver.find_element(By.ID, "doc_nextbtn")
        self.driver.execute_script("arguments[0].click();", go_to_sixth)
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
        go_to_final = self.driver.find_element(By.ID, "doc_nextbtn")
        self.driver.execute_script("arguments[0].click();", go_to_final)
        time.sleep(5)

    def save_transaction(self):
        reg_transaction = self.driver.find_element(By.ID, "restrictive_interest_save_btn")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", reg_transaction)
        time.sleep(5)
        self.driver.execute_script("arguments[0].click();", reg_transaction)
        time.sleep(10)

        # click on ok button
        click_ok = self.driver.find_element(By.XPATH, "//button[@class='btn btn-primary']")
        self.driver.execute_script("arguments[0].click();", click_ok)
        time.sleep(3)

    # register boundary correction transaction
    def register_servitude_transaction(self, sapplicationdescription, firstname, fathername,
                                       gfname, idfile, idtext, pomfile,
                                       pomreference, pomdescription, pfname,
                                       pfathername, pgfname, address,
                                       uploadid, idreference, uploadLHC,
                                       addLHCreference, addLHCdescription):
        self.select_servitude_transaction()
        self.servitude_application_description(sapplicationdescription)
        self.load_parcel(firstname, fathername, gfname)
        self.applicant_id_info(idfile, idtext)
        self.applicant_POM_info(pomfile, pomreference, pomdescription)
        self.next_to_third()
        self.select_parcel()
        self.next_to_fourth()
        self.add_third_party(pfname, pfathername, pgfname, address, uploadid, idreference)
        self.next_to_fifth()
        self.servitude_detail()
        self.restriction_end_date()
        self.next_to_sixth()
        self.add_holding(uploadLHC, addLHCreference, addLHCdescription)
        self.next_to_final()
        self.save_transaction()
