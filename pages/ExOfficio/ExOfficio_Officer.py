import time

from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver
from utilities.application_description import AppDesc
from utilities.load_parcel import LoadParcel


class ExOfficioOfficer(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.waitforpresence = BaseDriver(self.driver)
        self.appdesc = AppDesc(self.driver)
        self.loadparcel = LoadParcel(self.driver)

    def select_exofficio_transaction(self):
        time.sleep(5)
        exofficio_transaction = self.driver.find_element(By.XPATH, '//*[@id="transaction_menu"]/div[5]/article/a')
        self.driver.execute_script("arguments[0].click();", exofficio_transaction)
        time.sleep(5)

    # # select Kebele
    # def select_kebele(self):
    #     # select kebele
    #     select_kebele = self.driver.find_element(By.ID, "special_case_kebele")
    #     kebele_dd = Select(select_kebele)
    #     kebele_dd.select_by_index(3)
    #     time.sleep(2)

    # fill in the application description and click next button
    def exofficio_application_description(self, exapplicationdescription):
        self.appdesc.application_description(exapplicationdescription)
        # exapp_d = self.driver.find_element(By.ID, "app_description")
        # exapp_d.send_keys(exapplicationdescription)
        # time.sleep(5)
        # next_b = self.driver.find_element(By.ID, "nextToSecond")
        # self.driver.execute_script("arguments[0].click();", next_b)
        # time.sleep(5)

    def load_parcel(self, firstname, fathername, gfname):
        self.loadparcel.load_parcel_infromation(firstname, fathername, gfname)

    # def load_parcel(self):
    #     load_parcel_info = self.driver.find_element(By.XPATH, "//button[@data-toggle='modal' "
    #                                                           "and @data-target='#pick_person' "
    #                                                           "and @data-backdrop='static']")
    #     self.driver.execute_script("arguments[0].click();", load_parcel_info)
    #     time.sleep(5)
    #
    # def search_Holding(self, firstname, fathername, gfname):
    #     first_name = self.driver.find_element(By.ID, "sea_name")
    #     father_name = self.driver.find_element(By.ID, "sea_father")
    #     gf_name = self.driver.find_element(By.ID, "sea_gfather")
    #     search_button = self.driver.find_element(By.XPATH, '//*[@id="sea_form"]/div[2]/button')
    #     first_name.send_keys(firstname)
    #     father_name.send_keys(fathername)
    #     gf_name.send_keys(gfname)
    #     self.driver.execute_script("arguments[0].click();", search_button)
    #     time.sleep(10)
    #
    # def add_parcel(self):
    #     # add_parcel_info = self.driver.find_element(By.XPATH,
    #     #                                            '//*[@id="total_result"]/table/tbody/tr[1]/td/table/thead/tr/td['
    #     #                                            '5]/div/a[2]')
    #     self.driver.execute_script("arguments[0].click();",
    #                                self.waitforpresence.wait_until_presence_of_element_located(By.XPATH,
    #                                                                                            '//*['
    #                                                                                            '@id="total_result'
    #                                                                                            '"]/table/tbody/tr['
    #                                                                                            '1]/td/table/thead/tr'
    #                                                                                            '/td['
    #                                                                                            '5]/div/a[2]'))
    #     time.sleep(10)
    #
    # def next_button(self):
    #     button_next = self.driver.find_element(By.ID, "nextToSecond")
    #     self.driver.execute_script("arguments[0].click();", button_next)
    #     time.sleep(5)

    # add id information
    def add_applicant_info(self, oname, oaddress):
        self.driver.implicitly_wait(5)
        add_party = self.driver.find_element(By.XPATH, "//button[@id='ex_officio_applicant_add']")
        self.driver.execute_script("arguments[0].click();", add_party)
        time.sleep(5)
        org_name = self.driver.find_element(By.XPATH, '//*[@id="non_natural_party_name"]')
        org_name.send_keys(oname)
        time.sleep(5)
        org_address = self.driver.find_element(By.XPATH, '//*[@id="non_natural_party_address"]')
        org_address.send_keys(oaddress)
        time.sleep(5)
        save_party = self.driver.find_element(By.XPATH, '//*[@id="party"]/div/div[3]/div[3]/button')
        self.driver.execute_script("arguments[0].click();", save_party)
        time.sleep(5)
        to_the_next = self.driver.find_element(By.ID, "doc_nextbtn")
        time.sleep(5)
        self.driver.execute_script("arguments[0].click();", to_the_next)
        time.sleep(5)

    # add_marital_info
    def add_exofficio_decision(self, exofficiodoc, reference, description):
        add_exofficio = self.driver.find_element(By.XPATH, '//*[@id="row_1"]/td[5]/a')
        upload_doc = self.driver.find_element(By.ID, "upload_doc_req")
        add_reference = self.driver.find_element(By.ID, "doc_reference_req")
        add_description = self.driver.find_element(By.ID, "doc_description_req")
        add_doc = self.driver.find_element(By.XPATH, '//*[@id="add_req_document"]/div/div/div[3]/div/button')
        next_to_third = self.driver.find_element(By.XPATH, '//*[@id="doc_nextbtn"]')

        self.driver.execute_script("arguments[0].click();", add_exofficio)
        time.sleep(5)
        upload_doc.send_keys(exofficiodoc)
        time.sleep(5)
        add_reference.send_keys(reference)
        time.sleep(5)
        add_description.send_keys(description)
        time.sleep(5)
        self.driver.execute_script("arguments[0].click();", add_doc)
        time.sleep(5)
        self.driver.execute_script("arguments[0].click();", next_to_third)
        time.sleep(5)

    # save_transactipon
    def save_transaction(self):
        # self.driver.execute_script("window.scrollTo(0, 0);")
        # time.sleep(5)
        # scroll_to_register = self.driver.find_element(By.CLASS_NAME, 'x_content')
        # self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", scroll_to_register)

        self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(By.XPATH,
                                                                                              '//*['
                                                                                              '@id="save_transaction"]'))
        self.driver.execute_script("arguments[0].click();",
                                   self.waitforpresence.wait_until_element_to_be_clickable(By.XPATH,
                                                                                           '//*['
                                                                                           '@id="save_transaction"]'))
        time.sleep(10)

        # click on ok button
        click_ok = self.driver.find_element(By.XPATH, "//button[@data-bb-handler='ok']")
        self.driver.execute_script("arguments[0].click();", click_ok)
        time.sleep(3)

    # register boundary correction transaction
    def register_exofficio_transaction(self, exapplicationdescription, firstname, fathername,
                                       gfname, oname, oaddress, exofficiodoc, reference, description):
        self.select_exofficio_transaction()
        self.exofficio_application_description(exapplicationdescription)
        self.load_parcel(firstname, fathername,gfname)
        # self.search_Holding(firstname, fathername, gfname)
        # self.add_parcel()
        # self.next_button()
        self.add_applicant_info(oname, oaddress)
        self.add_exofficio_decision(exofficiodoc, reference, description)
        self.save_transaction()
