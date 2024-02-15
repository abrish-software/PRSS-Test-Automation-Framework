import time

import pytest
import unittest

from base.base_driver import BaseDriver
from pages.inheritancewithoutwill.inheritancewithoutwill_Officer import InheritWithoutWillOfficer
from pages.inheritancewithwill.Inheritancewithwill_Officer import InheritWithWillOfficer
from utilities.expert_logout import ExpertLogout
from utilities.Expert_no_cmss import ExpertNoCMSS
from utilities.close_the_transaction_title_deed import CloseTransaction
from utilities.new_application import NewApplication
from ddt import ddt, file_data

from utilities.supervisor_role import Supervisor


@pytest.mark.usefixtures("setup")
@ddt
class Test_InheritWithoutWill(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def Class_Setup(self):
        self.login = BaseDriver(self.driver)
        self.logout = BaseDriver(self.driver)
        self.expertlogout = ExpertLogout(self.driver)
        self.new_application = NewApplication(self.driver)
        self.officer = InheritWithoutWillOfficer(self.driver)
        self.expert = ExpertNoCMSS(self.driver)
        self.closetransaction = CloseTransaction(self.driver)
        self.supervisor = Supervisor(self.driver)

    # @file_data("../testdata/testdata.json")
    @file_data('../testdata/inheritancewithoutwill/inheritancewithoutwilltestdata.yaml')
    def test_register_inheritwithoutwill_transaction(self, inheritwithwillapplicationdescription, dfirstname, dfathername,
                                            dgfname, fname, fathername, gfname, address, uploadid, idreference, pomdoc,
                                            add_pom_ref, POD, podreference, poddescription, cr, crreference, crdescription
                                            , cddoc, cdreference, cddescription, LHC, LHCreference,
                                            LHCdescription, expertremarktext, supervisorremarktext, titledeed):
        # login as officer

        self.login.log_into_nrlais("Officer", "Officer")

        # click on new application and

        self.new_application.select_new_application()

        # select special case from the list

        self.officer.register_inheitwithoutwill_transaction(inheritwithwillapplicationdescription, dfirstname, dfathername,
                                            dgfname , fname, fathername, gfname, address, uploadid, idreference, pomdoc,
                                            add_pom_ref, POD, podreference, poddescription, cr, crreference, crdescription
                                            , cddoc, cdreference, cddescription, LHC, LHCreference, LHCdescription)

        self.logout.logout()

        # login as expert user
        self.login.log_into_nrlais("Expert", "Expert")

        # click on the transaction to send it to supervisor
        self.expert.send_to_supervisor_for_approval(expertremarktext)

        # logout from expert account
        self.driver.refresh()
        time.sleep(5)
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
