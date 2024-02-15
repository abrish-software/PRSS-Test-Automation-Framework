import pytest
import unittest

from base.base_driver import BaseDriver
from pages.Gift.Gift_existing_officer import GiftExistingOfficer
from utilities.Expert_no_cmss import ExpertNoCMSS
from utilities.close_the_transaction_title_deed import CloseTransaction
from utilities.new_application import NewApplication
from ddt import ddt, file_data

from utilities.supervisor_role import Supervisor


@pytest.mark.usefixtures("setup")
@ddt
class Test_Gift_To_Existing_Holder(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def Class_Setup(self):
        self.login = BaseDriver(self.driver)
        self.logout = BaseDriver(self.driver)
        self.new_application = NewApplication(self.driver)
        self.officer = GiftExistingOfficer(self.driver)
        self.expert = ExpertNoCMSS(self.driver)
        self.closetransaction = CloseTransaction(self.driver)
        self.supervisor = Supervisor(self.driver)

    # @file_data("../testdata/testdata.json")
    @file_data('../../testdata/gift/gifttoexistingtestdata.yaml')
    def test_register_gift_transaction(self, giftapplicationdescription, gfirstname, gidfile,
                                       gidtext, gpocfile, gpocref, gpoctext,
                                       rfname, ridfile, ridtext, rpocfile, rpocref, rpoctext,
                                       cr, crreference, crdescription, LHC, LHCreference, LHCdescription,
                                       expertremarktext, supervisorremarktext, titledeed):
        # login as officer

        self.login.log_into_nrlais("Officer", "Officer")

        # click on new application and

        self.new_application.select_new_application()

        # select special case from the list

        self.officer.register_gift_existing_transaction(giftapplicationdescription, gfirstname, gidfile,
                                                        gidtext, gpocfile, gpocref, gpoctext,
                                                        rfname, ridfile, ridtext, rpocfile, rpocref, rpoctext,
                                                        cr, crreference, crdescription, LHC, LHCreference,
                                                        LHCdescription)

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
        self.closetransaction.finalize_the_transaction(titledeed)
