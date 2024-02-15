import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from base.base_driver import BaseDriver
from utilities.add_id_info import IdInfo
from utilities.add_new_holder_info import IdNewHolder
from utilities.application_description import AppDesc
from utilities.load_parcel import LoadParcel
from utilities.marital_status import MaritalStatus


class GiftOfficer(BaseDriver):
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

    def gift_application_description(self, giftapplicationdescription):
        self.appdesc.application_description(giftapplicationdescription)

    def load_gift_parcel(self, gfirstname, gfathername, ggfname):
        self.loadparcel.load_parcel_infromation(gfirstname, gfathername, ggfname)

        # first_parcel = self.driver.find_element(By.XPATH, "//button[normalize-space()='Load First Holding Parcel']")
        # self.driver.execute_script("arguments[0].click();", first_parcel)
        # time.sleep(5)
        # first_name = self.driver.find_element(By.ID, "sea_name")
        # father_name = self.driver.find_element(By.ID, "sea_father")
        # gf_name = self.driver.find_element(By.ID, "sea_gfather")
        # search_button = self.driver.find_element(By.XPATH, '//*[@id="sea_form"]/div[2]/button')
        # first_name.send_keys(fhfirstname)
        # # self.driver.execute_script("arguments[0].value = arguments[1];", first_name, firstname)
        # father_name.send_keys(fhfathername)
        # gf_name.send_keys(fhgfname)
        # self.driver.execute_script("arguments[0].click();", search_button)
        # time.sleep(10)
        # # self.loadparcel.search_Holding(fhfirstname, fhfathername, fhgfname)
        # self.loadparcel.add_parcel()
        # self.loadparcel.next_button()

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

    def add_reciever_info(self, rfname, rfathername, rgfname, raddress, ruploadid, ridreference, rpomdoc, radd_pom_ref):
        self.addparty.add_party(rfname, rfathername, rgfname, raddress, ruploadid, ridreference, rpomdoc, radd_pom_ref)

    def Next_button(self):
        next_to_third = self.driver.find_element(By.ID, 'doc_nextbtn')
        time.sleep(5)
        self.driver.execute_script("arguments[0].click();", next_to_third)
        time.sleep(10)

    def construct_holding(self):
        click_on_construct = self.driver.find_element(By.ID, "gift_harmony_new_holding_add")
        self.driver.execute_script("arguments[0].click();", click_on_construct)

    def select_party(self):
        select_party_info = self.driver.find_element(By.XPATH,
                                                     "(//td[position()=6 and @class='align-right']/button)[2]")
        self.driver.execute_script("arguments[0].click();", select_party_info)
        time.sleep(10)

    def create_holding(self):
        click_create_holding = self.driver.find_element(By.ID, "createHoldingBtn")
        self.driver.execute_script("arguments[0].click();", click_create_holding)
        time.sleep(5)
        next_to_fourth = self.driver.find_element(By.ID, "doc_nextbtn")
        self.driver.execute_script("arguments[0].click();", next_to_fourth)
        time.sleep(5)

    def assign_parcel(self):
        assign_parcel_to_party = self.driver.find_element(By.XPATH,
                                                          "(//td[@class='align-center']//input[@type='checkbox'])[2]")

        self.driver.execute_script("arguments[0].click();", assign_parcel_to_party)
        time.sleep(5)
        next_to_fifth = self.driver.find_element(By.XPATH, "//button[@class='btn btn-nrlais' and contains(text(), "
                                                           "'Next')]")
        self.driver.execute_script("arguments[0].click();", next_to_fifth)

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

    def next_button(self):
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

    def register_gift_transaction(self, giftapplicationdescription, gfirstname, gfathername, ggfname,gidfile,
                                  gidtext,gpocfile, gpocref, gpoctext,
                                  rfname, rfathername, rgfname,
                                  raddress, ruploadid, ridreference, rpomdoc, radd_pom_ref,
                                  cr, crreference, crdescription,LHC, LHCreference, LHCdescription):
        self.select_gift_transaction()
        self.gift_application_description(giftapplicationdescription)
        self.load_gift_parcel(gfirstname, gfathername, ggfname)
        self.giver_id_info(gidfile,gidtext)
        self.giver_marital_status(gpocfile, gpocref, gpoctext)
        self.select_parcel_to_transfer()
        self.add_reciever_info(rfname, rfathername, rgfname, raddress, ruploadid, ridreference, rpomdoc, radd_pom_ref)
        self.Next_button()
        self.construct_holding()
        self.select_party()
        self.create_holding()
        self.assign_parcel()
        self.add_claim(cr, crreference, crdescription)
        self.add_LC(LHC, LHCreference, LHCdescription)
        self.next_button()
        self.save_transaction()
