import pytest
import unittest

from base.base_driver import BaseDriver
from pages.Divorce.close_divorce import CloseDivorce
from pages.Divorce.divorce_officer import DivorceOfficer
from pages.inheritancewithwill.Inheritancewithwill_Officer import InheritWithWillOfficer
from pages.marriage.marriage_officer import MarriageOfficer
# from pages.inheritancewithwill.expert_logout import ExpertLogout
from utilities.Expert_no_cmss import ExpertNoCMSS
from utilities.close_the_transaction_title_deed import CloseTransaction
from utilities.expert_role import Expert
from utilities.new_application import NewApplication
from ddt import ddt, file_data

from utilities.supervisor_role import Supervisor


@pytest.mark.usefixtures("setup")
@ddt
class Test_Divorce(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def Class_Setup(self):
        self.login = BaseDriver(self.driver)
        self.logout = BaseDriver(self.driver)
        # self.expertlogout = ExpertLogout(self.driver)
        self.new_application = NewApplication(self.driver)
        self.officer = DivorceOfficer(self.driver)
        self.expert = Expert(self.driver)
        self.close = CloseDivorce(self.driver)
        self.supervisor = Supervisor(self.driver)

    # @file_data("../testdata/testdata.json")
    @file_data('../testdata/divorce/divorcetestdata.yaml')
    def test_register_divorce_transaction(self,dapplicationdescription, firstname, fathername,
                                     gfname, hidfile, hidtext,
                                    widfile, widtext, divorcefile, divorceref, divorcedesc,
                                     crfile, crreference, crdescription,
                                     uploadLHC, addLHCreference, addLHCdescription,
                                    expertremarktext, supervisorremarktext, titledeed1, titledeed2):
        # login as officer

        self.login.log_into_nrlais("Officer", "Officer")

        # click on new application and

        self.new_application.select_new_application()

        # select special case from the list

        self.officer.register_divorce_transaction(dapplicationdescription, firstname, fathername,
                                     gfname, hidfile, hidtext,
                                    widfile, widtext, divorcefile, divorceref, divorcedesc,
                                     crfile, crreference, crdescription,
                                     uploadLHC, addLHCreference, addLHCdescription)

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
        self.close.finalize_the_transaction(titledeed1, titledeed2)
