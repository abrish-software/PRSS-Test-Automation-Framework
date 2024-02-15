import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from base.base_driver import BaseDriver
from utilities.application_description import AppDesc
from utilities.load_parcel import LoadParcel
from utilities.share_cropper_info import ShareCrpperInfo


class ShareCroppRegOfficer(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.waitforaddparcel = BaseDriver(self.driver)
        self.appdesc = AppDesc(self.driver)
        self.loadparcel = LoadParcel(self.driver)
        self.sharecropper = ShareCrpperInfo(self.driver)

    def select_share_cropping(self):
        time.sleep(5)
        share_cropping = self.driver.find_element(By.XPATH, "//p[normalize-space()='Share Cropping']")
        self.driver.execute_script("arguments[0].click();", share_cropping)
        time.sleep(5)

    def share_cropping_application_description(self, shapplicationdescription):
        self.appdesc.application_description(shapplicationdescription)
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

    def assign_parcel(self):
        parcel = self.driver.find_element(By.XPATH, "//td/input[@type='checkbox' and @field='select']")
        self.driver.execute_script("arguments[0].click();", parcel)
        time.sleep(5)

    def next_to_fourth(self):
        go_to_fourth = self.driver.find_element(By.XPATH, '//*[@id="step-3"]/div/div[2]/div/button')
        self.driver.execute_script("arguments[0].click();", go_to_fourth)
        time.sleep(5)

    def add_share_cropper(self, shcfname, shcfathername, shcgfname, shcaddress, uploadid, idreference):
        self.sharecropper.add_share_cropper(shcfname, shcfathername, shcgfname, shcaddress, uploadid, idreference)

    def next_to_fifth(self):
        go_to_fifth = self.driver.find_element(By.ID, "doc_nextbtn")
        self.driver.execute_script("arguments[0].click();", go_to_fifth)
        time.sleep(5)

    # def add_rent_value(self, rentvalue):
    #     rent_value = self.driver.find_element(By.ID, "rent_value")
    #     rent_value.send_keys(rentvalue)
    #     time.sleep(5)

    def share_cropping_end_date(self):
        end_date = self.driver.find_element(By.ID, "share_cropping_date_end")
        end_date.send_keys(Keys.RETURN)
        time.sleep(5)
        # default_year = 2016
        select_year = self.driver.find_element(By.ID, "etdc_year_et")
        year_dd = Select(select_year)
        default_year = int(year_dd.first_selected_option.text)
        next_year = default_year + 1
        year_dd.select_by_visible_text(str(next_year))
        # default_year_index = year_dd.options.index(year_dd.first_selected_option)
        # next_year_index = default_year_index + 1
        # year_dd.select_by_index(next_year_index)
        # last_index = len(year_dd.options) - 1
        # year_dd.select_by_index(last_index)
        self.driver.execute_script("arguments[0].selectedIndex = arguments[0].selectedIndex + 1;", select_year)
        time.sleep(5)
        select_date = self.driver.find_element(By.XPATH, "//td[@class='etdc_day' and text()='24']")
        self.driver.execute_script("arguments[0].click();", select_date)
        time.sleep(5)

    def add_agreement_doc(self, agreementdoc, shcreference, shcdescription):
        add_doc = self.driver.find_element(By.ID, "share_cropping_agreement_doc")
        add_doc.send_keys(agreementdoc)
        time.sleep(5)
        add_reference = self.driver.find_element(By.ID, "share_cropping_agreement_doc_ref")
        add_reference.send_keys(shcreference)
        time.sleep(5)
        add_description = self.driver.find_element(By.ID, "share_cropping_agreement_disc")
        add_description.send_keys(shcdescription)
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
        reg_transaction = self.driver.find_element(By.ID, "save_transaction")
        self.driver.execute_script("arguments[0].scrollIntoView(true);", reg_transaction)
        time.sleep(5)
        self.driver.execute_script("arguments[0].click();", reg_transaction)
        time.sleep(10)

        # click on ok button
        click_ok = self.driver.find_element(By.XPATH, "//button[@class='btn btn-primary']")
        self.driver.execute_script("arguments[0].click();", click_ok)
        time.sleep(3)

    def register_share_cropping_transaction(self, shapplicationdescription, firstname, fathername,
                                            gfname, idfile, idtext, pomfile,
                                            pomreference, pomdescription,
                                            shcfname, shcfathername, shcgfname, shcaddress,
                                            uploadid, idreference, agreementdoc,
                                            shcreference, shcdescription, uploadLHC,
                                            addLHCreference, addLHCdescription):
        self.select_share_cropping()
        self.share_cropping_application_description(shapplicationdescription)
        self.load_parcel_info(firstname, fathername, gfname)
        self.applicant_id_info(idfile, idtext)
        self.applicant_POM_info(pomfile, pomreference, pomdescription)
        self.next_to_third()
        self.assign_parcel()
        self.next_to_fourth()
        self.add_share_cropper(shcfname, shcfathername, shcgfname, shcaddress, uploadid, idreference)
        self.next_to_fifth()
        self.share_cropping_end_date()
        self.add_agreement_doc(agreementdoc, shcreference, shcdescription)
        self.next_to_sixth()
        self.add_holding(uploadLHC, addLHCreference, addLHCdescription)
        self.next_to_final()
        self.save_transaction()
