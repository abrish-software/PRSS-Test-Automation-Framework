import time

from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from utilities.add_id_info import IdInfo
from utilities.add_new_holder_info import IdNewHolder
from utilities.application_description import AppDesc
from utilities.load_parcel import LoadParcel
from utilities.marital_status import MaritalStatus


class InheritWithWillOfficer(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.appdesc = AppDesc(self.driver)
        self.loadparcel = LoadParcel(self.driver)
        self.idinfo = IdInfo(self.driver)
        self.maritalstatus = MaritalStatus(self.driver)
        self.waitforpresence = BaseDriver(self.driver)
        self.addparty = IdNewHolder(self.driver)

    def select_inheritwithwill_transaction(self):
        inheritance_transaction = self.driver.find_element(By.XPATH, "//button[@id='inheritance_btn']")
        self.driver.execute_script("arguments[0].click();", inheritance_transaction)
        time.sleep(5)
        inheritwithwill_transaction = self.driver.find_element(By.XPATH,
                                                               "//div[@id='inheritance_popover']//a[text("
                                                               ")='Inheritance with Will']")
        self.driver.execute_script("arguments[0].click();", inheritwithwill_transaction)
        time.sleep(5)

    def inheritwithwill_application_description(self, inheritwithwillapplicationdescription):
        self.appdesc.application_description(inheritwithwillapplicationdescription)

    def load_inheritwithwill_parcel(self, dfirstname, dfathername, dgfname):
        self.loadparcel.load_parcel_infromation(dfirstname, dfathername, dgfname)

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

    def select_deceased_party(self):
        deceased_party = self.driver.find_element(By.XPATH, '//*[@id="ap_inheritance_deceased"]')
        self.driver.execute_script("arguments[0].click();", deceased_party)
        time.sleep(5)
        third_page = self.driver.find_element(By.ID, "nextToThird")
        self.driver.execute_script("arguments[0].click();", third_page)
        time.sleep(5)

    def add_reciever_party(self, fname, fathername, gfname, address, uploadid, idreference, pomdoc, add_pom_ref):
        add_reciever = self.driver.find_element(By.ID, "inheritance_harmony_beneficiary_add")
        self.driver.execute_script("arguments[0].click();", add_reciever)
        # Add holder Information
        time.sleep(5)
        add_first_name = self.driver.find_element(By.ID, "party_firstname")
        add_first_name.send_keys(fname)
        time.sleep(3)
        add_father_name = self.driver.find_element(By.ID, "party_fathername")
        add_father_name.send_keys(fathername)
        time.sleep(3)
        add_gfather_name = self.driver.find_element(By.ID, "party_gfathername")
        add_gfather_name.send_keys(gfname)
        time.sleep(3)
        self.addparty.add_DOB()
        self.addparty.marital_status()
        self.addparty.holder_address(address)
        self.addparty.disability_info()
        self.addparty.family_status()
        self.addparty.Id_Information(uploadid, idreference)
        self.addparty.add_pom(pomdoc, add_pom_ref)

    def Next_button(self):
        next_to_fourth = self.driver.find_element(By.ID, 'doc_nextbtn')
        time.sleep(5)
        self.driver.execute_script("arguments[0].click();", next_to_fourth)
        time.sleep(10)

    def construct_holding(self):
        click_on_construct = self.driver.find_element(By.ID, "inheritance_harmony_new_holding_add")
        self.driver.execute_script("arguments[0].click();", click_on_construct)
        time.sleep(5)

    def select_party(self):
        select_party_info = self.driver.find_element(By.XPATH,
                                                     "(//td[position()=6 and @class='align-right']/button)[1]")
        self.driver.execute_script("arguments[0].click();", select_party_info)
        time.sleep(5)

    def create_holding(self):
        click_create_holding = self.driver.find_element(By.ID, "createHoldingBtn")
        self.driver.execute_script("arguments[0].click();", click_create_holding)
        time.sleep(5)
        next_to_fifth = self.driver.find_element(By.ID, "doc_nextbtn")
        self.driver.execute_script("arguments[0].click();", next_to_fifth)
        time.sleep(5)

    def assign_parcel(self):
        assign_parcel_to_party = self.driver.find_element(By.XPATH,
                                                          "(//td[@class='align-center']//input[@type='checkbox'])")

        self.driver.execute_script("arguments[0].click();", assign_parcel_to_party)
        time.sleep(5)
        next_to_sixth = self.driver.find_element(By.XPATH, "//button[@class='btn btn-nrlais' and contains(text(), "
                                                           "'Next')]")
        self.driver.execute_script("arguments[0].click();", next_to_sixth)

    def add_proof_of_death(self, POD, podreference, poddescription):
        add_POD = self.driver.find_element(By.XPATH, '//*[@id="row_1"]/td[5]/a')
        self.driver.execute_script("arguments[0].click();", add_POD)
        time.sleep(5)
        upload_POD = self.driver.find_element(By.ID, "upload_doc_req")
        upload_POD.send_keys(POD)
        time.sleep(5)
        pod_reference = self.driver.find_element(By.ID, "doc_reference_req")
        pod_reference.send_keys(podreference)
        time.sleep(5)
        pod_description = self.driver.find_element(By.ID, "doc_description_req")
        pod_description.send_keys(poddescription)
        time.sleep(5)
        save_POD = self.driver.find_element(By.XPATH, '//*[@id="add_req_document"]/div/div/div[3]/div/button')
        self.driver.execute_script("arguments[0].click();", save_POD)
        time.sleep(5)

    def add_claim(self, cr, crreference, crdescription):
        add_CR = self.driver.find_element(By.XPATH, '//*[@id="row_2"]/td[5]/a')
        self.driver.execute_script("arguments[0].click();", add_CR)
        time.sleep(5)
        upload_CR = self.driver.find_element(By.ID, 'upload_doc_req')
        upload_CR.send_keys(cr)
        time.sleep(5)
        cr_reference = self.driver.find_element(By.CSS_SELECTOR, 'input#doc_reference_req')
        cr_reference.send_keys(crreference)
        time.sleep(5)
        cr_description = self.driver.find_element(By.CSS_SELECTOR, 'textarea#doc_description_req')
        cr_description.send_keys(crdescription)
        time.sleep(5)
        add_cr_all = self.driver.find_element(By.XPATH,
                                              '//*[@id="add_req_document"]/div/div/div[3]/div/button')
        self.driver.execute_script("arguments[0].click();", add_cr_all)
        time.sleep(5)

    def add_will_document(self, willdoc, willreference, willdescription):
        add_will = self.driver.find_element(By.XPATH, '//*[@id="row_3"]/td[5]/a')
        self.driver.execute_script("arguments[0].click();", add_will)
        time.sleep(5)
        upload_will = self.driver.find_element(By.ID, "upload_doc_req")
        upload_will.send_keys(willdoc)
        time.sleep(5)
        will_reference = self.driver.find_element(By.ID, "doc_reference_req")
        will_reference.send_keys(willreference)
        time.sleep(5)
        will_description = self.driver.find_element(By.ID, "doc_description_req")
        will_description.send_keys(willdescription)
        time.sleep(5)
        save_will = self.driver.find_element(By.XPATH, '//*[@id="add_req_document"]/div/div/div[3]/div/button')
        self.driver.execute_script("arguments[0].click();", save_will)
        time.sleep(5)

    def add_certeficate(self, LHC, LHCreference, LHCdescription):
        add_lhc = self.driver.find_element(By.XPATH, '//*[@id="row_4"]/td[5]/a')
        self.driver.execute_script("arguments[0].click();", add_lhc)
        upload_LH = self.driver.find_element(By.ID, "upload_doc_req")
        upload_LH.send_keys(LHC)
        time.sleep(5)
        LHC_reference = self.driver.find_element(By.CSS_SELECTOR, "input#doc_reference_req")
        LHC_reference.send_keys(LHCreference)
        time.sleep(5)
        LHC_description = self.driver.find_element(By.CSS_SELECTOR, 'textarea#doc_description_req')
        LHC_description.send_keys(LHCdescription)
        time.sleep(5)
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

    def register_inheitwithwill_transaction(self, inheritwithwillapplicationdescription, dfirstname, dfathername,
                                            dgfname
                                            , fname, fathername, gfname, address, uploadid, idreference, pomdoc,
                                            add_pom_ref
                                            , POD, podreference, poddescription, cr, crreference, crdescription
                                            , willdoc, willreference, willdescription, LHC, LHCreference,
                                            LHCdescription):

        self.select_inheritwithwill_transaction()
        self.inheritwithwill_application_description(inheritwithwillapplicationdescription)
        self.load_inheritwithwill_parcel(dfirstname, dfathername,dgfname)
        self.select_deceased_party()
        self.add_reciever_party(fname, fathername, gfname, address, uploadid, idreference, pomdoc, add_pom_ref)
        self.Next_button()
        self.construct_holding()
        self.select_party()
        self.create_holding()
        self.assign_parcel()
        self.add_proof_of_death(POD, podreference, poddescription)
        self.add_claim(cr, crreference, crdescription)
        self.add_will_document(willdoc, willreference, willdescription)
        self.add_certeficate(LHC, LHCreference, LHCdescription)
        self.next_button()
        self.save_transaction()
