import time

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from base.base_driver import BaseDriver
from utilities.add_id_info import IdInfo
from utilities.application_description import AppDesc
from utilities.load_parcel import LoadParcel
from utilities.marital_status import MaritalStatus


class ExchangeOfficer(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.appdesc = AppDesc(self.driver)
        self.loadparcel = LoadParcel(self.driver)
        self.idinfo = IdInfo(self.driver)
        self.maritalstatus = MaritalStatus(self.driver)
        self.waitfor = BaseDriver(self.driver)

    def select_exchange_transaction(self):
        time.sleep(5)
        exchange_transaction = self.driver.find_element(By.XPATH, '//*[@id="transaction_menu"]/div[4]/article/a')
        self.driver.execute_script("arguments[0].click();", exchange_transaction)
        time.sleep(5)
        self.driver.refresh()
        time.sleep(5)

    def exchange_application_description(self, exchangeapplicationdescription):
        self.appdesc.application_description(exchangeapplicationdescription)

    def load_first_parcel(self, fhfirstname, fhfathername, fhgfname):
        first_parcel = self.driver.find_element(By.XPATH, "//button[normalize-space()='Load First Holding Parcel']")
        self.driver.execute_script("arguments[0].click();", first_parcel)
        time.sleep(5)
        first_name = self.driver.find_element(By.ID, "sea_name")
        father_name = self.driver.find_element(By.ID, "sea_father")
        gf_name = self.driver.find_element(By.ID, "sea_gfather")
        search_button = self.driver.find_element(By.XPATH, '//*[@id="sea_form"]/div[2]/button')
        first_name.send_keys(fhfirstname)
        # self.driver.execute_script("arguments[0].value = arguments[1];", first_name, firstname)
        father_name.send_keys(fhfathername)
        gf_name.send_keys(fhgfname)
        self.driver.execute_script("arguments[0].click();", search_button)
        time.sleep(10)
        # self.loadparcel.search_Holding(fhfirstname, fhfathername, fhgfname)
        self.loadparcel.add_parcel()
        self.loadparcel.next_button()

    def first_holder_id_info(self, fhidfile, fhidtext):
        self.idinfo.id_info(fhidfile, fhidtext)

    def first_holder_marital_status(self, fhpocfile, fhpocref, fhpoctext):
        self.maritalstatus.marital_status(fhpocfile, fhpocref, fhpoctext)

    def select_parcel_fh(self):
        select_parcel = self.driver.find_element(By.XPATH, "//input[@type='checkbox' and @field='select']")
        self.driver.execute_script("arguments[0].click();", select_parcel)
        time.sleep(5)
        next_to_fourth = self.driver.find_element(By.XPATH,
                                                  '//*[@id="step-parcel1"]/div/div[2]/div/button')
        self.driver.execute_script("arguments[0].click();", next_to_fourth)

    def refresh_second_holding(self):
        refresh = self.driver.find_element(By.ID, "exchange_applicant2")
        self.driver.execute_script("arguments[0].innerHTML = arguments[0].innerHTML", refresh)

    def load_second_parcel(self, shfirstname, shfathername, shgfname):
        second_parcel = self.driver.find_element(By.XPATH,
                                                 '//*[@id="step-holding2"]/div/div[3]/div/button[1]')
        self.driver.execute_script("arguments[0].click();", second_parcel)
        time.sleep(5)
        first_name = self.driver.find_element(By.ID, "sea_name")
        father_name = self.driver.find_element(By.ID, "sea_father")
        gf_name = self.driver.find_element(By.ID, "sea_gfather")
        search_button = self.driver.find_element(By.XPATH, '//*[@id="sea_form"]/div[2]/button')
        first_name.send_keys(shfirstname)
        # self.driver.execute_script("arguments[0].value = arguments[1];", first_name, firstname)
        father_name.send_keys(shfathername)
        gf_name.send_keys(shgfname)
        self.driver.execute_script("arguments[0].click();", search_button)
        time.sleep(10)
        # self.loadparcel.search_Holding(shfirstname, shfathername, shgfname)
        self.loadparcel.add_parcel()
        # self.loadparcel.next_button()

    def second_holder_id(self, shidfile, shidtext):
        self.driver.implicitly_wait(100)
        add_id_info = self.driver.find_element(By.ID, "add_id")
        time.sleep(5)
        self.driver.execute_script("arguments[0].click();", add_id_info)
        add_id_file = self.driver.find_element(By.ID, "id_file")
        time.sleep(5)
        add_id_file.send_keys(shidfile)
        select_id_type = self.driver.find_element(By.ID, "id_type")
        time.sleep(5)
        select_id_dd = Select(select_id_type)
        select_id_dd.select_by_index(1)
        add_id_text = self.driver.find_element(By.ID, "id_text")
        time.sleep(5)
        add_id_text.send_keys(shidtext)
        time.sleep(3)
        add_id_content = self.driver.find_element(By.CSS_SELECTOR, '#add_id_content > div > ' 'div >' 'div.modal'
                                                                   '-footer > div > a')
        add_id_content.send_keys(Keys.ENTER)
        # self.driver.execute_script("arguments[0].click();",
        #                            self.waitfor.wait_until_element_to_be_clickable(By.XPATH,
        #                                                                            '//*[@id="add_id_content"]/div/div'
        #                                                                            '/div[3]/div/a'))
        # action_chains = ActionChains(self.driver)

        # Perform a click action on the element action_chains.move_to_element(
        # self.waitfor.wait_until_presence_of_element_located(By.CSS_SELECTOR, '#add_id_content > div > ' 'div >'
        # 'div.modal-footer > div > a')).perform() self.driver.execute_script("arguments[0].click();",
        # self.waitfor.wait_until_element_to_be_clickable(By.CSS_SELECTOR, '#add_id_content > div > div > '
        # 'div.modal-footer > div > a'))
        time.sleep(5)

    def second_holder_marital_status(self, shpocfile, shpocref, shpoctext):
        add_marital_info = self.driver.find_element(By.CSS_SELECTOR, 'td#pom_btn a#add_id')
        self.driver.execute_script("arguments[0].click();", add_marital_info)
        time.sleep(5)
        add_poc_file = self.driver.find_element(By.ID, "pom_file")
        add_poc_file.send_keys(shpocfile)
        time.sleep(5)
        add_poc_reference = self.driver.find_element(By.CSS_SELECTOR, "input#pom_ref")
        add_poc_reference.send_keys(shpocref)
        time.sleep(5)
        add_poc_text = self.driver.find_element(By.CSS_SELECTOR, "input#pom_text")
        add_poc_text.send_keys(shpoctext)
        time.sleep(3)
        # self.driver.execute_script("arguments[0].click();",
        #                            self.waitfor.wait_until_element_to_be_clickable(By.XPATH,
        #                                                                            '//*[@id="add_pom_content"]/div'
        #                                                                            '/div/div[3]/div/a'))
        action_chains = ActionChains(self.driver)

        # Perform a click action on the element
        action_chains.click(self.waitfor.wait_until_element_to_be_clickable(By.CSS_SELECTOR,
                                                                            '#add_pom_content > div > div > '
                                                                            'div.modal-footer > div > a')).perform()
        time.sleep(3)
        next_to_third = self.driver.find_element(By.ID, "doc_nextbtn")
        time.sleep(5)
        self.driver.execute_script("arguments[0].click();", next_to_third)
        time.sleep(5)

    def select_parcel_sh(self):
        select_parcel = self.driver.find_element(By.XPATH, "//input[@type='checkbox' and @field='select']")
        self.driver.execute_script("arguments[0].click();", select_parcel)
        time.sleep(5)
        next_to_fifth = self.driver.find_element(By.XPATH,
                                                 '//*[@id="step-parcel1"]/div/div[2]/div/button')
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

    def add_FLC(self, fhLHC, fhLHCreference, fhLHCdescription):
        add_fhlc = self.driver.find_element(By.XPATH, '//*[@id="row_2"]/td[5]/a')
        self.driver.execute_script("arguments[0].click();", add_fhlc)
        upload_LH = self.driver.find_element(By.ID, "upload_doc_req")
        upload_LH.send_keys(fhLHC)
        LHC_reference = self.driver.find_element(By.CSS_SELECTOR, "input#doc_reference_req")
        LHC_reference.send_keys(fhLHCreference)
        LHC_description = self.driver.find_element(By.CSS_SELECTOR, 'textarea#doc_description_req')
        LHC_description.send_keys(fhLHCdescription)
        add_LHC_all = self.driver.find_element(By.XPATH,
                                               '//*[@id="add_req_document"]/div/div/div[3]/div/button')
        self.driver.execute_script("arguments[0].click();", add_LHC_all)
        time.sleep(5)

    def add_SLC(self, shLHC, shLHCreference, shLHCdescription):
        add_shlc = self.driver.find_element(By.XPATH, '//*[@id="row_3"]/td[5]/a')
        self.driver.execute_script("arguments[0].click();", add_shlc)
        upload_LH = self.driver.find_element(By.ID, "upload_doc_req")
        upload_LH.send_keys(shLHC)
        LHC_reference = self.driver.find_element(By.CSS_SELECTOR, "input#doc_reference_req")
        LHC_reference.send_keys(shLHCreference)
        LHC_description = self.driver.find_element(By.CSS_SELECTOR, 'textarea#doc_description_req')
        LHC_description.send_keys(shLHCdescription)
        add_LHC_all = self.driver.find_element(By.XPATH,
                                               '//*[@id="add_req_document"]/div/div/div[3]/div/button')
        self.driver.execute_script("arguments[0].click();", add_LHC_all)
        time.sleep(5)

    def next_button(self):
        next_to_final = self.driver.find_element(By.ID, "doc_nextbtn")
        self.driver.execute_script("arguments[0].click();", next_to_final)
        time.sleep(5)

    def save_transaction(self):
        register_transaction = self.driver.find_element(By.CSS_SELECTOR, 'button#save_transation')

        self.driver.execute_script("arguments[0].scrollIntoView();", register_transaction)
        self.driver.execute_script("arguments[0].click();",
                                   self.waitfor.wait_until_element_to_be_clickable(By.CSS_SELECTOR,
                                                                                   'button#save_transation'))
        time.sleep(10)

        # click on ok button
        click_ok = self.driver.find_element(By.XPATH, "//button[@data-bb-handler='ok']")
        self.driver.execute_script("arguments[0].click();", click_ok)
        time.sleep(3)

    def register_exchange_transaction(self, exchangeapplicationdescription,
                                      fhfirstname, fhfathername, fhgfname, fhidfile, fhidtext, fhpocfile, fhpocref,
                                      fhpoctext, shfirstname, shfathername, shgfname, shidfile, shidtext, shpocfile,
                                      shpocref, shpoctext, cr, crreference, crdescription, fhLHC, fhLHCreference,
                                      fhLHCdescription
                                      , shLHC, shLHCreference, shLHCdescription):
        self.select_exchange_transaction()
        self.exchange_application_description(exchangeapplicationdescription)
        self.load_first_parcel(fhfirstname, fhfathername, fhgfname)
        self.first_holder_id_info(fhidfile, fhidtext)
        self.first_holder_marital_status(fhpocfile, fhpocref, fhpoctext)
        self.select_parcel_fh()
        self.refresh_second_holding()
        self.load_second_parcel(shfirstname, shfathername, shgfname)
        self.second_holder_id(shidfile, shidtext)
        self.second_holder_marital_status(shpocfile, shpocref, shpoctext)
        self.select_parcel_sh()
        self.add_claim(cr, crreference, crdescription)
        self.add_FLC(fhLHC, fhLHCreference, fhLHCdescription)
        self.add_SLC(shLHC, shLHCreference, shLHCdescription)
        self.next_button()
        self.save_transaction()
