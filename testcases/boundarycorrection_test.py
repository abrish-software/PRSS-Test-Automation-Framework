import pytest
import unittest

from base.base_driver import BaseDriver
from utilities.expert_role import Expert
from utilities.supervisor_role import Supervisor
from pages.boundarycorrection.boundary_officer import BoundaryOfficer
from utilities.new_application import NewApplication
from utilities.close_the_transaction_title_deed import CloseTransaction
from ddt import ddt, file_data


@pytest.mark.usefixtures("setup")
@ddt
class Test_Boundary_Correction(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def Class_Setup(self):
        self.login = BaseDriver(self.driver)
        self.logout = BaseDriver(self.driver)
        self.new_application = NewApplication(self.driver)
        self.boundarycorrection = BoundaryOfficer(self.driver)
        self.expert = Expert(self.driver)
        self.supervisor = Supervisor(self.driver)
        self.close = CloseTransaction(self.driver)

    # @file_data("../testdata/testdata.json")
    @file_data('../testdata/boundarycorrection/boundarycorrectiontestdata.yaml')
    def test_register_boundary_correction(self, bapplicationdescription, firstname, fathername,
                                          gfname,pocfile, pocref, poctext, idfile, idtext, uploadLHC, addLHCreference,
                                          addLHCdescription, remarktext, supervisorremarktext, titledeed):
        # login as officer

        self.login.log_into_nrlais("Officer", "Officer")

        # click on new application and

        self.new_application.select_new_application()

        # select special case from the list

        self.boundarycorrection.register_boundary_correction(bapplicationdescription, firstname, fathername,
                                                             gfname,pocfile, pocref, poctext, idfile, idtext,
                                                             uploadLHC, addLHCreference, addLHCdescription)

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