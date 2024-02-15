import pytest
import unittest

from base.base_driver import BaseDriver
from pages.ExOfficio.ExOfficio_Expert import ExOfficioExpert
from pages.ExOfficio.ExOfficio_Officer import ExOfficioOfficer
from pages.ExOfficio.ExOfficio_close import ExOfficioClose
from pages.simplecorrection.simplecorrection_expert import SimpCorrExpert
from pages.simplecorrection.simplecorrection_officer import SimpCorrectionOfficer
from utilities.close_transaction import CloseTheTransaction
from utilities.supervisor_role import Supervisor
from utilities.new_application import NewApplication
from ddt import ddt, file_data


@pytest.mark.usefixtures("setup")
@ddt
class Test_Simple_Correction(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def Class_Setup(self):
        self.login = BaseDriver(self.driver)
        self.logout = BaseDriver(self.driver)
        self.new_application = NewApplication(self.driver)
        self.officer = SimpCorrectionOfficer(self.driver)
        self.expert = SimpCorrExpert(self.driver)
        self.close = CloseTheTransaction(self.driver)
        self.supervisor = Supervisor(self.driver)

    # @file_data("../testdata/testdata.json")
    @file_data('../testdata/simplecorrection/simplecorrectiontestdata.yaml')
    def test_register_simple_correction_transaction(self, sapplicationdescription, firstname, fathername,
                                                    gfname, idfile, idtext, pomfile, pomreference, pomdescription,
                                                    uploadLHC, addLHCreference, addLHCdescription, ortho,
                                                    expertremarktext, supervisorremarktext, officerremarktext):
        # login as officer

        self.login.log_into_nrlais("Officer", "Officer")

        # click on new application and

        self.new_application.select_new_application()

        # select special case from the list

        self.officer.register_simple_correction_transaction(sapplicationdescription, firstname, fathername,
                                                            gfname, idfile, idtext, pomfile, pomreference,
                                                            pomdescription,
                                                            uploadLHC, addLHCreference, addLHCdescription)

        self.logout.logout()

        # login as expert user
        self.login.log_into_nrlais("Expert", "Expert")

        # click on the transaction to send it to supervisor
        self.expert.send_to_supervisor_for_approval(ortho, expertremarktext)

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
