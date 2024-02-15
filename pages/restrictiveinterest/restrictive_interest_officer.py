import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from base.base_driver import BaseDriver
from utilities.add_id_info import IdInfo
from utilities.add_new_holder_info import IdNewHolder
from utilities.application_description import AppDesc
from utilities.load_parcel import LoadParcel
from utilities.marital_status import MaritalStatus
from utilities.third_party_info import ThirdParty


class RestrictiveInterestOfficer(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.appdesc = AppDesc(self.driver)
        self.loadparcel = LoadParcel(self.driver)
        self.idinfo = IdInfo(self.driver)
        self.maritalstatus = MaritalStatus(self.driver)
        self.waitforpresence = BaseDriver(self.driver)
        self.addparty = ThirdParty(self.driver)

    def select_restrictive_interest(self):
        time.sleep(5)
        restrictive_interest_transaction = self.driver.find_element(By.XPATH, "//p[normalize-space()='Restrictive "
                                                                              "Interest']")
        self.driver.execute_script("arguments[0].click();",  restrictive_interest_transaction)
        time.sleep(5)

    def restrictive_interest_app_description(self, riapplicationdescription):
        self.appdesc.application_description(riapplicationdescription)

    def load_parcel(self, firstname, fathername, gfname):
        self.loadparcel.load_parcel_infromation(firstname, fathername, gfname)

    # def next_to_second(self):
    #     self.loadparcel.next_button()
    def add_id_info(self, idfile, idtext):
        add_id_info = self.driver.find_element(By.ID, "add_id")
        self.driver.execute_script("arguments[0].click();", add_id_info)
        add_id_file = self.driver.find_element(By.ID, "id_file")
        add_id_file.send_keys(idfile)
        time.sleep(5)
        select_id_type = self.driver.find_element(By.ID, "id_type")
        select_id_dd = Select(select_id_type)
        select_id_dd.select_by_index(1)
        time.sleep(5)
        add_id_text = self.driver.find_element(By.ID, "id_text")
        add_id_text.send_keys(idtext)
        time.sleep(5)
        add_id_content = self.driver.find_element(By.XPATH, "//div[@id='add_id_content']//a[@class='btn btn-nrlais' "
                                                            "and text()='Add']")
        self.driver.execute_script("arguments[0].click();", add_id_content)
        # add_id_content.send_keys(Keys.ENTER)
        time.sleep(5)

    def add_pom_info(self, pocfile, pocreference, pocdescription):
        marriage_proof = self.driver.find_element(By.XPATH, '//td[@id="pom_btn"]/a[@id="add_id"]')
        self.driver.execute_script("arguments[0].click();", marriage_proof)
        time.sleep(5)
        pom_file = self.driver.find_element(By.ID, "pom_file")
        pom_file.send_keys(pocfile)
        time.sleep(5)
        pom_reference = self.driver.find_element(By.XPATH, '//div//input[@type="text" and @id="pom_ref"]')
        pom_reference.send_keys(pocreference)
        time.sleep(5)
        pom_description = self.driver.find_element(By.XPATH, '//div//input[@type="text" and @id="pom_text"]')
        pom_description.send_keys(pocdescription)
        time.sleep(5)
        save_pom = self.driver.find_element(By.XPATH, "//div[@id='add_pom_content']//a[@class='btn btn-nrlais' and "
                                                      "text()='Add']")
        self.driver.execute_script("arguments[0].click();", save_pom)
        time.sleep(5)

    def next_to_third(self):
        go_to_third = self.driver.find_element(By.ID, 'nextToThird')
        time.sleep(5)
        self.driver.execute_script("arguments[0].click();", go_to_third)
        time.sleep(10)

    def select_parcel(self):
        parcel = self.driver.find_element(By.XPATH, "//input[@type='checkbox'][@field='select']")
        self.driver.execute_script("arguments[0].click();", parcel)
        time.sleep(5)

    def next_to_fourth(self):
        go_to_fourth = self.driver.find_element(By.XPATH, '//*[@id="step-3"]/div/div[2]/div/button')
        self.driver.execute_script("arguments[0].click();", go_to_fourth)
        time.sleep(5)

    def add_third_party(self, thpfname, thpfathername, thpgfname,  thpaddress, uploadid, idreference):
        self.addparty.add_third_party(thpfname, thpfathername, thpgfname,  thpaddress, uploadid, idreference)

    def next_to_fifth(self):
        go_to_fifth = self.driver.find_element(By.ID, 'doc_nextbtn')
        self.driver.execute_script("arguments[0].click();", go_to_fifth)
        time.sleep(5)

    def select_restriction_type(self):
        restriction_type = self.driver.find_element(By.ID, "restriction_type")
        select_restriction_dd = Select(restriction_type)
        select_restriction_dd.select_by_index(1)
        time.sleep(5)

    def restriction_end_date(self):
        end_date = self.driver.find_element(By.ID, "restrictive_interest_date_end")
        end_date.send_keys(Keys.RETURN)
        time.sleep(5)
        select_year = self.driver.find_element(By.ID, "etdc_year_et")
        year_dd = Select(select_year)
        default_year = int(year_dd.first_selected_option.text)
        next_year = default_year + 1
        year_dd.select_by_visible_text(str(next_year))
        self.driver.execute_script("arguments[0].selectedIndex = arguments[0].selectedIndex + 1;", select_year)
        time.sleep(5)
        select_date = self.driver.find_element(By.XPATH, "//td[@class='etdc_day' and text()='24']")
        self.driver.execute_script("arguments[0].click();", select_date)
        time.sleep(5)

    def add_agreement_doc(self, agreementdoc, rireference, ridescription):
        add_doc = self.driver.find_element(By.ID, "restrictive_interest_agreement_doc")
        add_doc.send_keys(agreementdoc)
        time.sleep(5)
        add_reference = self.driver.find_element(By.ID, "restrictive_interest_agreement_doc_ref")
        add_reference.send_keys(rireference)
        time.sleep(5)
        add_description = self.driver.find_element(By.ID, "restrictive_interest_agreement_disc")
        add_description.send_keys(ridescription)
        time.sleep(5)

    def next_to_sixth(self):
        go_to_sixth = self.driver.find_element(By.ID, "doc_nextbtn")
        self.driver.execute_script("arguments[0].click();", go_to_sixth)
        time.sleep(5)

    def add_court_order(self, courtdoc,courtdocreference, courtdocdescription):
        court_doc = self.driver.find_element(By.XPATH, '//*[@id="row_1"]/td[5]/a')
        self.driver.execute_script("arguments[0].click();", court_doc)
        time.sleep(5)
        upload_doc = self.driver.find_element(By.ID, "upload_doc_req")
        add_doc_ref = self.driver.find_element(By.ID, "doc_reference_req")
        add_doc_description = self.driver.find_element(By.ID, "doc_description_req")
        add_req_documents = self.driver.find_element(By.CSS_SELECTOR, "#add_req_document > div > div > "
                                                                      "div.modal-footer > div > button")
        # next_to_save = self.driver.find_element(By.CSS_SELECTOR, "button#doc_nextbtn")
        upload_doc.send_keys(courtdoc)
        time.sleep(5)
        add_doc_ref.send_keys(courtdocreference)
        time.sleep(5)
        add_doc_description.send_keys(courtdocdescription)
        time.sleep(5)
        # add_req_documents.click()
        self.driver.execute_script("arguments[0].click();", add_req_documents)
        # add_req_documents.send_keys(Keys.ENTER)
        time.sleep(5)

    def add_LHC(self, lhc, lhcreference, lhcdescription):
        court_doc = self.driver.find_element(By.XPATH, '//*[@id="row_2"]/td[5]/a')
        self.driver.execute_script("arguments[0].click();", court_doc)
        time.sleep(5)
        upload_doc = self.driver.find_element(By.ID, "upload_doc_req")
        add_doc_ref = self.driver.find_element(By.ID, "doc_reference_req")
        add_doc_description = self.driver.find_element(By.ID, "doc_description_req")
        add_req_documents = self.driver.find_element(By.CSS_SELECTOR, "#add_req_document > div > div > "
                                                                      "div.modal-footer > div > button")
        # next_to_save = self.driver.find_element(By.CSS_SELECTOR, "button#doc_nextbtn")
        upload_doc.send_keys(lhc)
        time.sleep(5)
        add_doc_ref.send_keys(lhcreference)
        time.sleep(5)
        add_doc_description.send_keys(lhcdescription)
        time.sleep(5)
        # add_req_documents.click()
        self.driver.execute_script("arguments[0].click();", add_req_documents)
        # add_req_documents.send_keys(Keys.ENTER)
        time.sleep(5)

    def next_to_final(self):
        next_to_final = self.driver.find_element(By.ID, "doc_nextbtn")
        self.driver.execute_script("arguments[0].click();", next_to_final)
        time.sleep(5)

    def save_transaction(self):
        register_transaction = self.driver.find_element(By.ID, 'restrictive_interest_save_btn')

        self.driver.execute_script("arguments[0].scrollIntoView();", register_transaction)
        self.driver.execute_script("arguments[0].click();",
                                   self.waitforpresence.wait_until_element_to_be_clickable(By.ID,
                                                                                           'restrictive_interest_save_btn'))
        time.sleep(10)

        # click on ok button
        click_ok = self.driver.find_element(By.XPATH, "//button[@data-bb-handler='ok']")
        self.driver.execute_script("arguments[0].click();", click_ok)
        time.sleep(3)

    def register_restrictive_interest_transaction(self, riapplicationdescription,
                                firstname, fathername, gfname, idfile,
                                  idtext, pocfile, pocref, poctext,thpfname, thpfathername,
                                thpgfname,  thpaddress, uploadid, idreference,
                                agreementdoc, rireference, ridescription,
                                courtdoc,courtdocreference, courtdocdescription,
                                lhc, lhcreference, lhcdescription ):

        self.select_restrictive_interest()
        self.restrictive_interest_app_description(riapplicationdescription)
        self.load_parcel(firstname, fathername, gfname)
        self.add_id_info(idfile, idtext)
        self.add_pom_info(pocfile, pocref, poctext)
        self.next_to_third()
        self.select_parcel()
        self.next_to_fourth()
        self.add_third_party(thpfname, thpfathername, thpgfname,  thpaddress, uploadid, idreference)
        self.next_to_fifth()
        self.select_restriction_type()
        self.restriction_end_date()
        self.add_agreement_doc(agreementdoc, rireference, ridescription)
        self.next_to_sixth()
        self.add_court_order(courtdoc,courtdocreference, courtdocdescription)
        self.add_LHC(lhc, lhcreference, lhcdescription)
        self.next_to_final()
        self.save_transaction()