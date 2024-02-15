import pytest
import unittest

from base.base_driver import BaseDriver
from pages.Expropration.Expropration_Expert import ExproprationExpert
from pages.Expropration.Expropration_Officer import ExproprationOfficer
from utilities.close_the_transaction_title_deed import CloseTransaction
from utilities.new_application import NewApplication
from ddt import ddt, file_data

from utilities.supervisor_role import Supervisor


@pytest.mark.usefixtures("setup")
@ddt
class Test_Expropration(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def Class_Setup(self):
        self.login = BaseDriver(self.driver)
        self.logout = BaseDriver(self.driver)
        self.new_application = NewApplication(self.driver)
        self.exprooofficer = ExproprationOfficer(self.driver)
        self.exprooexpert = ExproprationExpert(self.driver)
        self.closetransaction = CloseTransaction(self.driver)
        self.supervisor = Supervisor(self.driver)

    # @file_data("../testdata/testdata.json")
    @file_data('../testdata/expropration/exproprationtestdata.yaml')
    def test_register_expropration_transaction(self, exproapplicationdescription, firstname, fathername,
                                               gfname, oname, oaddress, woredadoc, reference, description,
                                               compdoc, compreference, compdescription,
                                               landdoc, landreference, landdescription,
                                               expertremarktext, supervisorremarktext, titledeed):
        # login as officer

        self.login.log_into_nrlais("Officer", "Officer")

        # click on new application and

        self.new_application.select_new_application()

        # select special case from the list

        self.exprooofficer.register_expropration_transaction(exproapplicationdescription, firstname, fathername,
                                                             gfname, oname, oaddress, woredadoc, reference, description,
                                                             compdoc, compreference, compdescription,
                                                             landdoc, landreference, landdescription)

        self.logout.logout()

        # login as expert user
        self.login.log_into_nrlais("Expert", "Expert")

        # click on the transaction to send it to supervisor
        self.exprooexpert.send_to_supervisor_for_approval(expertremarktext)

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
        self.closetransaction.finalize_the_transaction(titledeed)
