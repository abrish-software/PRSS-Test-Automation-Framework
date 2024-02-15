import pytest
import unittest

from base.base_driver import BaseDriver
from pages.SpecialCase.special_Officer_female import SpecialOfficerFemale
from pages.SpecialCase.special_officer_male import SpecialOfficerMale
from pages.SpecialCase.special_officer_joint import SpecialJointHolders
from utilities.close_the_transaction_title_deed import CloseTransaction
from utilities.expert_role import Expert
from utilities.new_application import NewApplication
from ddt import ddt, file_data

from utilities.supervisor_role import Supervisor


@pytest.mark.usefixtures("setup")
@ddt
class Test_special_case(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def Class_Setup(self):
        self.login = BaseDriver(self.driver)
        self.logout = BaseDriver(self.driver)
        self.new_application = NewApplication(self.driver)
        self.specialcasemale = SpecialOfficerMale(self.driver)
        self.specialcasefemale = SpecialOfficerFemale(self.driver)
        self.expert = Expert(self.driver)
        self.supervisor = Supervisor(self.driver)
        self.close = CloseTransaction(self.driver)
        self.jointholders = SpecialJointHolders(self.driver)

    # @file_data("../testdata/testdata.json")
    @file_data('../testdata/specialcase/specialtestdatasinglemaleholder.yaml')
    def test_register_one_holder_male(self, applicationdescription, firstname, fathername, gfname, holderaddress,
                                      holderID,
                                      IDreference, holderclaim, holderclaimR, holderclaimD, Holdingproof,
                                      HoldingproofR, HoldingproofD, remarktext, supervisorremarktext, titledeed):
        # login as officer

        self.login.log_into_nrlais("Officer", "Officer")

        # click on new application and

        self.new_application.select_new_application()

        # select special case from the list

        self.specialcasemale.register_special_case_transaction(applicationdescription, firstname, fathername, gfname,
                                                               holderaddress, holderID, IDreference, holderclaim,
                                                               holderclaimR, holderclaimD, Holdingproof, HoldingproofR,
                                                               HoldingproofD)

        self.logout.logout()

        # login as expert user
        self.login.log_into_nrlais("Expert", "Expert")

        # click on the transaction to send it to supervisor
        self.expert.send_to_supervisor_for_approval(remarktext)

        # logout from expert account
        self.logout.logout()

        # login as a supervisor
        self.login.log_into_nrlais("Supervisor", "Supervisor")

        # approve the transaction

        self.supervisor.approved_transaction(supervisorremarktext)

        # logout from supervisor account
        self.logout.logout()

        # login as Officer to close transaction
        self.login.log_into_nrlais("Officer", "Officer")

        # click on the transaction to be closed
        self.close.finalize_the_transaction(titledeed)

        # @file_data("../testdata/testdata.json")

    @file_data('../testdata/specialcase/specialtestdatasinglefemaleholder.yaml')
    def test_register_one_holder_female(self, applicationdescription, firstname, fathername, gfname, holderaddress,
                                        holderID,
                                        IDreference, holderclaim, holderclaimR, holderclaimD, Holdingproof,
                                        HoldingproofR, HoldingproofD, remarktext, supervisorremarktext, titledeed):
        # login as officer

        self.login.log_into_nrlais("Officer", "Officer")

        # click on new application and

        self.new_application.select_new_application()

        # select special case from the list

        self.specialcasefemale.register_special_case_transaction(applicationdescription, firstname, fathername, gfname,
                                                                 holderaddress, holderID, IDreference, holderclaim,
                                                                 holderclaimR, holderclaimD, Holdingproof,
                                                                 HoldingproofR,
                                                                 HoldingproofD)

        self.logout.logout()

        # login as expert user
        self.login.log_into_nrlais("Expert", "Expert")

        # click on the transaction to send it to supervisor
        self.expert.send_to_supervisor_for_approval(remarktext)

        # logout from expert account
        self.logout.logout()

        # login as a supervisor
        self.login.log_into_nrlais("Supervisor", "Supervisor")

        # approve the transaction

        self.supervisor.approved_transaction(supervisorremarktext)

        # logout from supervisor account
        self.logout.logout()

        # login as Officer to close transaction
        self.login.log_into_nrlais("Officer", "Officer")

        # click on the transaction to be closed
        self.close.finalize_the_transaction(titledeed)

    @file_data('../testdata/specialcase/specialtestdatajointholders.yaml')
    def test_register_joint_holders(self, applicationdescription, fhfirstname, fhfathername, fhgfname, fholderaddress,
                                    fhshare_info, fholderID, fhIDreference, shfirstname, shfathername, shgfname,
                                    sholderaddress, shshare_info, sholderID, shIDreference, holderclaim, holderclaimR,
                                    holderclaimD,
                                    Holdingproof, HoldingproofR, HoldingproofD, remarktext, supervisorremarktext,
                                    titledeed):
        # login as officer

        self.login.log_into_nrlais("Officer", "Officer")

        # click on new application and
        # Assuming self.driver is an instance of WebDriver
        self.driver.refresh()

        self.new_application.select_new_application()

        # select special case from the list
        self.jointholders.register_special_case_joint_holders(applicationdescription, fhfirstname, fhfathername,
                                                              fhgfname, fholderaddress,
                                                              fhshare_info, fholderID, fhIDreference, shfirstname,
                                                              shfathername, shgfname, sholderaddress, shshare_info,
                                                              sholderID, shIDreference, holderclaim, holderclaimR,
                                                              holderclaimD,
                                                              Holdingproof, HoldingproofR, HoldingproofD)
        self.logout.logout()
        #
        # login as expert user
        self.login.log_into_nrlais("Expert", "Expert")

        # click on the transaction to send it to supervisor
        self.expert.send_to_supervisor_for_approval(remarktext)

        # logout from expert account
        self.logout.logout()

        # login as a supervisor
        self.login.log_into_nrlais("Supervisor", "Supervisor")

        # approve the transaction

        self.supervisor.approved_transaction(supervisorremarktext)

        # logout from supervisor account
        self.logout.logout()

        # login as Officer to close transaction
        self.login.log_into_nrlais("Officer", "Officer")

        # click on the transaction to be closed
        self.close.finalize_the_transaction(titledeed)
