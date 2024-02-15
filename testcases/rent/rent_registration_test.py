import pytest
import unittest

from base.base_driver import BaseDriver
from pages.rent.rent_mod_officer import RentModOfficer
from pages.rent.rent_reg_officer import RentRegOfficer
from pages.servitude.servitude_officer import ServitudeOfficer
from utilities.Expert_no_cmss import ExpertNoCMSS
from utilities.close_transaction import CloseTheTransaction
from utilities.new_application import NewApplication
from ddt import ddt, file_data

from utilities.supervisor_role import Supervisor


@pytest.mark.usefixtures("setup")
@ddt
class Test_Rent_Registration(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def Class_Setup(self):
        self.login = BaseDriver(self.driver)
        self.logout = BaseDriver(self.driver)
        self.new_application = NewApplication(self.driver)
        self.officer = RentRegOfficer(self.driver)
        self.modifyOfficer = RentModOfficer(self.driver)
        self.expert = ExpertNoCMSS(self.driver)
        self.close = CloseTheTransaction(self.driver)
        self.supervisor = Supervisor(self.driver)

    # @file_data("../testdata/testdata.json")
    @file_data('../../testdata/rent/rentregistrationtestdata.yaml')
    def test_register_rent_transaction(self, rapplicationdescription, firstname, fathername,
                                       gfname, idfile, idtext, pomfile,
                                       pomreference, pomdescription,
                                       tfname, tfathername, tgfname, taddress,
                                       uploadid, idreference, rentvalue, agreementdoc,
                                       rentreference, rentdescription, uploadLHC,
                                       addLHCreference, addLHCdescription,
                                       expertremarktext, supervisorremarktext, officerremarktext):
        # login as officer

        self.login.log_into_nrlais("Officer", "Officer")

        # click on new application and

        self.new_application.select_new_application()

        # select special case from the list

        self.officer.register_rent_transaction(rapplicationdescription, firstname, fathername,
                                               gfname, idfile, idtext, pomfile,
                                               pomreference, pomdescription,
                                               tfname, tfathername, tgfname, taddress,
                                               uploadid, idreference, rentvalue, agreementdoc,
                                               rentreference, rentdescription, uploadLHC,
                                               addLHCreference, addLHCdescription)

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