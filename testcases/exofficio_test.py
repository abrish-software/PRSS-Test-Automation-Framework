import pytest
import unittest

from base.base_driver import BaseDriver
from pages.ExOfficio.ExOfficio_Expert import ExOfficioExpert
from pages.ExOfficio.ExOfficio_Officer import ExOfficioOfficer
from pages.ExOfficio.ExOfficio_close import ExOfficioClose
from utilities.supervisor_role import Supervisor
from utilities.new_application import NewApplication
from ddt import ddt, file_data


@pytest.mark.usefixtures("setup")
@ddt
class Test_ExOfficio(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def Class_Setup(self):
        self.login = BaseDriver(self.driver)
        self.logout = BaseDriver(self.driver)
        self.new_application = NewApplication(self.driver)
        self.exofficioofficer = ExOfficioOfficer(self.driver)
        self.exofficioexpert = ExOfficioExpert(self.driver)
        self.exofficioclose = ExOfficioClose(self.driver)
        self.supervisor = Supervisor(self.driver)

    # @file_data("../testdata/testdata.json")
    @file_data('../testdata/exofficio/exofficiotestdata.yaml')
    def test_register_exofficio_transaction(self, exapplicationdescription, firstname, fathername,
                                            gfname, oname, oaddress, exofficiodoc, reference, description, ortho,
                                            expertremarktext, supervisorremarktext, officerremarktext):
        # login as officer

        self.login.log_into_nrlais("Officer", "Officer")

        # click on new application and

        self.new_application.select_new_application()

        # select special case from the list

        self.exofficioofficer.register_exofficio_transaction(exapplicationdescription, firstname, fathername,
                                                             gfname, oname, oaddress, exofficiodoc, reference,
                                                             description)

        self.logout.logout()

        # login as expert user
        self.login.log_into_nrlais("Expert", "Expert")

        # click on the transaction to send it to supervisor
        self.exofficioexpert.send_to_supervisor_for_approval(ortho, expertremarktext)

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
        self.exofficioclose.Close_exofficio(officerremarktext)
