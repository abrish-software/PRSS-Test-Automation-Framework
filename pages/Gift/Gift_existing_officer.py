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


class GiftExistingOfficer(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.appdesc = AppDesc(self.driver)
        self.loadparcel = LoadParcel(self.driver)
        self.idinfo = IdInfo(self.driver)
        self.maritalstatus = MaritalStatus(self.driver)
        self.waitforpresence = BaseDriver(self.driver)
        self.addparty = IdNewHolder(self.driver)

    def select_gift_transaction(self):
        time.sleep(5)
        gift_transaction = self.driver.find_element(By.XPATH, '//*[@id="transaction_menu"]/div[7]/article/a')
        self.driver.execute_script("arguments[0].click();", gift_transaction)
        time.sleep(5)

    def refresh_page(self):
        self.driver.refresh()
        time.sleep(5)

    def gift_application_description(self, giftapplicationdescription):
        self.appdesc.application_description(giftapplicationdescription)

    def load_gift_parcel(self, gfirstname):
        self.loadparcel.load_parcel()
        first_name = self.driver.find_element(By.ID, "sea_name")
        first_name.send_keys(gfirstname)
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

    def giver_id_info(self, gidfile, gidtext):
        self.idinfo.id_info(gidfile, gidtext)

    def giver_marital_status(self, gpocfile, gpocref, gpoctext):
        self.maritalstatus.marital_status(gpocfile, gpocref, gpoctext)

    def select_parcel_to_transfer(self):
        select_parcel = self.driver.find_element(By.XPATH, "//input[@type='checkbox' and @field='select']")
        self.driver.execute_script("arguments[0].click();", select_parcel)
        time.sleep(5)
        next_to_fourth = self.driver.find_element(By.ID,
                                                  'nextToThird')
        self.driver.execute_script("arguments[0].click();", next_to_fourth)

    def add_existing_holding(self, rfirstname):
        click_on_add_existing = self.driver.find_element(By.ID, "pick_applicant_btn")
        self.driver.execute_script("arguments[0].click();", click_on_add_existing)
        first_name = self.driver.find_element(By.ID, "sea_name")
        first_name.send_keys(rfirstname)
        select_kebele = self.driver.find_element(By.ID, "sea_kebele")
        kebele_dd = Select(select_kebele)
        kebele_dd.select_by_index(3)
        time.sleep(2)
        search_button = self.driver.find_element(By.XPATH, '//*[@id="sea_form"]/div[2]/button')
        self.driver.execute_script("arguments[0].click();", search_button)
        time.sleep(5)
        self.loadparcel.add_parcel()

    def add_reciever_id_info(self, ridfile, ridtext):
        add_id_info = self.driver.find_element(By.ID, "add_id")
        self.driver.execute_script("arguments[0].click();", add_id_info)
        add_id_file = self.driver.find_element(By.ID, "id_file")
        add_id_file.send_keys(ridfile)
        time.sleep(5)
        select_id_type = self.driver.find_element(By.ID, "id_type")
        select_id_dd = Select(select_id_type)
        select_id_dd.select_by_index(1)
        time.sleep(5)
        add_id_text = self.driver.find_element(By.ID, "id_text")
        add_id_text.send_keys(ridtext)
        time.sleep(5)
        add_id_content = self.driver.find_element(By.XPATH, "//a[@class='btn btn-nrlais' and contains(@href, "
                                                            "'validateAndSaveID')]")
        self.driver.execute_script("arguments[0].click();", add_id_content)
        # add_id_content.send_keys(Keys.ENTER)
        time.sleep(5)

    def add_reciever_pom_info(self, rpocfile, rpocreference, rpocdescription):
        marriage_proof = self.driver.find_element(By.XPATH, '//td[@id="pom_btn"]/a[@id="add_id"]')
        self.driver.execute_script("arguments[0].click();", marriage_proof)
        time.sleep(5)
        pom_file = self.driver.find_element(By.ID, "pom_file")
        pom_file.send_keys(rpocfile)
        time.sleep(5)
        pom_reference = self.driver.find_element(By.XPATH, '//div//input[@type="text" and @id="pom_ref"]')
        pom_reference.send_keys(rpocreference)
        time.sleep(5)
        pom_description = self.driver.find_element(By.XPATH, '//div//input[@type="text" and @id="pom_text"]')
        pom_description.send_keys(rpocdescription)
        time.sleep(5)
        save_pom = self.driver.find_element(By.XPATH, "//a[@class='btn btn-nrlais' and contains(@href, "
                                                      "'validateAndSavePOM')]")
        self.driver.execute_script("arguments[0].click();", save_pom)
        # save_pom.click()
        # save_pom.send_keys(Keys.ENTER)
        time.sleep(5)

    def add_reciever_id_and_pom(self):
        add_all = self.driver.find_element(By.XPATH, "//button[@class='btn btn-nrlais' and text()='Done']")
        self.driver.execute_script("arguments[0].click();", add_all)
        time.sleep(5)

    def next_to_fifth(self):
        next_to_fifth = self.driver.find_element(By.ID, 'doc_nextbtn')
        time.sleep(5)
        self.driver.execute_script("arguments[0].click();", next_to_fifth)
        time.sleep(10)

    def next_to_sixth(self):
        next_to_sixth = self.driver.find_element(By.ID, 'doc_nextbtn')
        time.sleep(5)
        self.driver.execute_script("arguments[0].click();", next_to_sixth)
        time.sleep(10)

    # def construct_holding(self):
    #     click_on_construct = self.driver.find_element(By.ID, "gift_harmony_new_holding_add")
    #     self.driver.execute_script("arguments[0].click();", click_on_construct)
    #
    # def select_party(self):
    #     select_party_info = self.driver.find_element(By.XPATH,
    #                                                  "(//td[position()=6 and @class='align-right']/button)[2]")
    #     self.driver.execute_script("arguments[0].click();", select_party_info)
    #     time.sleep(10)
    #
    # def create_holding(self):
    #     click_create_holding = self.driver.find_element(By.ID, "createHoldingBtn")
    #     self.driver.execute_script("arguments[0].click();", click_create_holding)
    #     time.sleep(5)
    #     next_to_fourth = self.driver.find_element(By.ID, "doc_nextbtn")
    #     self.driver.execute_script("arguments[0].click();", next_to_fourth)
    #     time.sleep(5)

    def assign_parcel(self):
        assign_parcel_to_party = self.driver.find_element(By.XPATH,
                                                          "(//td[@class='align-center']//input[@type='checkbox'])[2]")

        self.driver.execute_script("arguments[0].click();", assign_parcel_to_party)
        time.sleep(5)

    def next_to_seven(self):
        next_to_seven = self.driver.find_element(By.XPATH, "//button[@class='btn btn-nrlais' and contains(text(), "
                                                           "'Next')]")
        self.driver.execute_script("arguments[0].click();", next_to_seven)

    def add_claim(self, cr, crreference, crdescription):
        add_CR = self.driver.find_element(By.XPATH, '//*[@id="row_1"]/td[5]/a')
        self.driver.execute_script("arguments[0].click();", add_CR)
        upload_CR = self.driver.find_element(By.ID, 'upload_doc_req')
        upload_CR.send_keys(cr)
        cr_reference = self.driver.find_element(By.CSS_SELECTOR, 'input#doc_reference_req')
        cr_reference.send_keys(crreference)
        cr_description = self.driver.find_element(By.CSS_SELECTOR, 'textarea#doc_description_req')
        cr_description.send_keys(crdescription)
        add_cr_all = self.driver.find_element(By.XPATH,
                                              '//*[@id="add_req_document"]/div/div/div[3]/div/button')
        self.driver.execute_script("arguments[0].click();", add_cr_all)
        time.sleep(5)

    def add_LC(self, LHC, LHCreference, LHCdescription):
        add_lc = self.driver.find_element(By.XPATH, '//*[@id="row_2"]/td[5]/a')
        self.driver.execute_script("arguments[0].click();", add_lc)
        upload_LH = self.driver.find_element(By.ID, "upload_doc_req")
        upload_LH.send_keys(LHC)
        LHC_reference = self.driver.find_element(By.CSS_SELECTOR, "input#doc_reference_req")
        LHC_reference.send_keys(LHCreference)
        LHC_description = self.driver.find_element(By.CSS_SELECTOR, 'textarea#doc_description_req')
        LHC_description.send_keys(LHCdescription)
        add_LHC_all = self.driver.find_element(By.XPATH,
                                               '//*[@id="add_req_document"]/div/div/div[3]/div/button')
        self.driver.execute_script("arguments[0].click();", add_LHC_all)
        time.sleep(5)

    def next_to_final(self):
        next_to_final = self.driver.find_element(By.ID, "doc_nextbtn")
        self.driver.execute_script("arguments[0].click();", next_to_final)
        time.sleep(5)

    def save_transaction(self):
        register_transaction = self.driver.find_element(By.ID, 'button_save_transaction')

        self.driver.execute_script("arguments[0].scrollIntoView();", register_transaction)
        self.driver.execute_script("arguments[0].click();",
                                   self.waitforpresence.wait_until_element_to_be_clickable(By.ID,
                                                                                           'button_save_transaction'))
        time.sleep(10)

        # click on ok button
        click_ok = self.driver.find_element(By.XPATH, "//button[@data-bb-handler='ok']")
        self.driver.execute_script("arguments[0].click();", click_ok)
        time.sleep(3)

    def register_gift_existing_transaction(self, giftapplicationdescription, gfirstname, gidfile,
                                           gidtext, gpocfile, gpocref, gpoctext,
                                           rfname, ridfile, ridtext, rpocfile, rpocref, rpoctext,
                                           cr, crreference, crdescription, LHC, LHCreference, LHCdescription):
        self.select_gift_transaction()
        self.refresh_page()
        self.gift_application_description(giftapplicationdescription)
        self.load_gift_parcel(gfirstname)
        self.next_to_second()
        self.giver_id_info(gidfile, gidtext)
        self.giver_marital_status(gpocfile, gpocref, gpoctext)
        self.select_parcel_to_transfer()
        self.add_existing_holding(rfname)
        self.add_reciever_id_info(ridfile, ridtext)
        self.add_reciever_pom_info(rpocfile, rpocref, rpoctext)
        self.add_reciever_id_and_pom()
        self.next_to_fifth()
        self.next_to_sixth()
        self.assign_parcel()
        self.next_to_seven()
        self.add_claim(cr, crreference, crdescription)
        self.add_LC(LHC, LHCreference, LHCdescription)
        self.next_to_final()
        self.save_transaction()
