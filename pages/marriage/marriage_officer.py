import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from base.base_driver import BaseDriver
from utilities.add_wife import WifeParty
from utilities.application_description import AppDesc
from utilities.load_parcel import LoadParcel


class MarriageOfficer(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.waitforaddparcel = BaseDriver(self.driver)
        self.appdesc = AppDesc(self.driver)
        self.loadparcel = LoadParcel(self.driver)
        self.wifeinfo = WifeParty(self.driver)

    def select_marriage_transaction(self):
        time.sleep(5)
        marriage_transaction = self.driver.find_element(By.XPATH, "//p[normalize-space()='Marriage']")
        self.driver.execute_script("arguments[0].click();", marriage_transaction)
        time.sleep(5)

    def select_kebele(self):
        kebele = self.driver.find_element(By.ID, "app_kebele")
        kebele_dd = Select(kebele)
        kebele_dd.select_by_index(3)
        time.sleep(2)

    def marriage_application_description(self, mapplicationdescription):
        self.appdesc.application_description(mapplicationdescription)
        # bapp_d = self.driver.find_element(By.ID, "app_description")
        # bapp_d.send_keys(bapplicationdescription)
        # time.sleep(5)
        # next_b = self.driver.find_element(By.ID, "nextToSecond")
        # self.driver.execute_script("arguments[0].click();", next_b)
        # time.sleep(5)

    def next_to_second(self):
        go_to_second = self.driver.find_element(By.ID, "nextToSecond")
        self.driver.execute_script("arguments[0].click();", go_to_second)

    def husband_information(self, hfirstname, hfathername, hgfname):
        husband_info = self.driver.find_element(By.ID, "pick_husband_btn")
        self.driver.execute_script("arguments[0].click();", husband_info)
        time.sleep(5)
        self.loadparcel.search_Holding(hfirstname, hfathername, hgfname)
        self.loadparcel.add_parcel()
        time.sleep(5)
        select_husband = self.driver.find_element(By.ID, "ap_select")
        self.driver.execute_script("arguments[0].click();", select_husband)
        time.sleep(3)

    def husband_id_info(self, hidfile, hidtext):
        self.driver.implicitly_wait(100)
        add_id_info = self.driver.find_element(By.ID, "add_id")
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

    def husband_share_info(self, husbandshare):
        husband_share = self.driver.find_element(By.ID, "ap_share")
        husband_share.clear()
        husband_share.send_keys(husbandshare)
        time.sleep(5)

    def add_husband_info(self):
        save_husband = self.driver.find_element(By.XPATH, "//button[@class='btn btn-nrlais' and text()='Done']")
        self.driver.execute_script("arguments[0].click();", save_husband)
        time.sleep(5)

    def husband_lhc(self, huploadLHC, haddLHCreference, haddLHCdescription):
        add_LHC = self.driver.find_element(By.XPATH, '//*[@id="row_1"]/td[5]/a')
        upload_doc = self.driver.find_element(By.ID, "upload_doc_req")
        add_doc_ref = self.driver.find_element(By.ID, "doc_reference_req")
        add_doc_description = self.driver.find_element(By.ID, "doc_description_req")
        add_req_documents = self.driver.find_element(By.CSS_SELECTOR, "#add_req_document > div > div > "
                                                                      "div.modal-footer > div > button")
        # next_to_save = self.driver.find_element(By.CSS_SELECTOR, "button#doc_nextbtn")
        self.driver.execute_script("arguments[0].click();", add_LHC)
        time.sleep(5)
        upload_doc.send_keys(huploadLHC)
        time.sleep(5)
        add_doc_ref.send_keys(haddLHCreference)
        time.sleep(5)
        add_doc_description.send_keys(haddLHCdescription)
        time.sleep(5)
        # add_req_documents.click()
        self.driver.execute_script("arguments[0].click();", add_req_documents)
        # add_req_documents.send_keys(Keys.ENTER)
        time.sleep(5)
        done_lhc = self.driver.find_element(By.XPATH, '//*[@id="pick_required_doc"]/div/div/div[3]/div/button')
        self.driver.execute_script("arguments[0].click();", done_lhc)
        time.sleep(5)
        # self.driver.execute_script("arguments[0].click();", next_to_save)
        # time.sleep(5)

    def select_parcel(self, sharedparcel):
        transfer_parcel = self.driver.find_element(By.XPATH, "//input[@type='checkbox' and @field='select']")
        self.driver.execute_script("arguments[0].click();", transfer_parcel)
        time.sleep(5)
        shared_parcel = self.driver.find_element(By.XPATH, "//input[contains(@class,'form-control') and @field='share']")
        shared_parcel.clear()
        shared_parcel.send_keys(sharedparcel)
        time.sleep(5)
        add_parcel = self.driver.find_element(By.XPATH, '//*[@id="select_transfer_parcel"]/div/div/div[3]/div/button')
        self.driver.execute_script("arguments[0].click();", add_parcel)
        time.sleep(5)

    def next_to_wife(self):
        nexttowife = self.driver.find_element(By.ID, "husbnad_parcel_btn")
        self.driver.execute_script("arguments[0].click();", nexttowife)

    def wife_info(self, wfirstname, wfathername, wgfname, whaddress, wshareinfo, wuploadid,
                  widreference):
        add_wife = self.driver.find_element(By.ID, "marriage_wife_party_add")
        self.driver.execute_script("arguments[0].click();", add_wife)
        time.sleep(5)
        self.wifeinfo.register_wife_Information(wfirstname, wfathername, wgfname, whaddress, wshareinfo, wuploadid,
                                                widreference)

    def fourth_page(self):
        next_to_fourth = self.driver.find_element(By.ID, "wife_parcel_btn")
        self.driver.execute_script("arguments[0].click();", next_to_fourth)
        time.sleep(5)

    def add_POM(self, pomfile, pomreference, pomdescription):
        marriage_proof = self.driver.find_element(By.XPATH, '//*[@id="row_1"]/td[5]/a')
        self.driver.execute_script("arguments[0].click();", marriage_proof)
        time.sleep(5)
        pom_file = self.driver.find_element(By.ID, "upload_doc_req")
        pom_file.send_keys( pomfile)
        time.sleep(5)
        pom_reference = self.driver.find_element(By.ID, "doc_reference_req")
        pom_reference.send_keys(pomreference)
        time.sleep(5)
        pom_description = self.driver.find_element(By.ID, "doc_description_req")
        pom_description.send_keys(pomdescription)
        time.sleep(5)
        save_pom = self.driver.find_element(By.XPATH, '//*[@id="add_req_document"]/div/div/div[3]/div/button')
        self.driver.execute_script("arguments[0].click();", save_pom)
        time.sleep(5)

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
    def register_marriage_transaction(self, mapplicationdescription, hfirstname,  hfathername,  hgfname,hidfile, hidtext,
                                      husbandshare,huploadLHC, haddLHCreference, haddLHCdescription, sharedparcel,
                                      wfirstname, wfathername, wgfname, whaddress, wshareinfo,
                                      wuploadid, widreference, pomfile, pomreference, pomdescription,crfile, crreference, crdescription):
        self.select_marriage_transaction()
        self.select_kebele()
        self.marriage_application_description(mapplicationdescription)
        self.next_to_second()
        self.husband_information(hfirstname,  hfathername,  hgfname)
        self.husband_id_info(hidfile, hidtext)
        self.husband_share_info(husbandshare)
        self.add_husband_info()
        self.husband_lhc(huploadLHC, haddLHCreference, haddLHCdescription)
        self.select_parcel(sharedparcel)
        self.next_to_wife()
        self.wife_info(wfirstname, wfathername, wgfname, whaddress, wshareinfo, wuploadid, widreference)
        self.fourth_page()
        self.add_POM(pomfile, pomreference, pomdescription)
        self.add_claim(crfile, crreference, crdescription)
        self.to_final_step()
        self.save_transaction()

