import pytest
import unittest

from base.base_driver import BaseDriver
from pages.mortgage.mortgage_mod_officer import MortgageModOfficer
from pages.mortgage.mortgage_reg_officer import MortgageRegOfficer
from pages.rent.rent_mod_officer import RentModOfficer
from utilities.Expert_no_cmss import ExpertNoCMSS
from utilities.close_transaction import CloseTheTransaction
from utilities.new_application import NewApplication
from ddt import ddt, file_data

from utilities.supervisor_role import Supervisor


@pytest.mark.usefixtures("setup")
@ddt
class Test_Mortgage_Modification(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def Class_Setup(self):
        self.login = BaseDriver(self.driver)
        self.logout = BaseDriver(self.driver)
        self.new_application = NewApplication(self.driver)
        self.officer = MortgageModOfficer(self.driver)
        self.modifyOfficer = RentModOfficer(self.driver)
        self.expert = ExpertNoCMSS(self.driver)
        self.close = CloseTheTransaction(self.driver)
        self.supervisor = Supervisor(self.driver)

    # @file_data("../testdata/testdata.json")
    @file_data('../../testdata/mortgage/mortgagemodificationtestdata.yaml')
    def test_modify_mortgage_transaction(self, mmapplicationdescription, firstname, fathername,
                                          gfname, idfile, idtext, pomfile, pomreference, pomdescription,
                                          mortgageamount, uploadBL,
                                          BLreference, BLdescription,
                                           expertremarktext, supervisorremarktext, officerremarktext):
        # login as officer

        self.login.log_into_nrlais("Officer", "Officer")

        # click on new application and

        self.new_application.select_new_application()

        # select special case from the list

        self.officer.register_mortgage_mod_transaction(mmapplicationdescription, firstname, fathername,
                                          gfname, idfile, idtext, pomfile, pomreference, pomdescription,
                                          mortgageamount, uploadBL,
                                          BLreference, BLdescription)

        self.logout.logout()

        # login as expert user
        self.login.log_into_nrlais("Expert", "Expert")

        # click on the transaction to send it to supervisor
        self.expert.send_to_supervisor_for_approval(expertremarktext)

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
        self.close.finalize_the_transaction(officerremarktext)
