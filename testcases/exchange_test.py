import pytest
import unittest

from base.base_driver import BaseDriver
from pages.Exchange.Exchange_Close import CloseExchange
from pages.Exchange.Exchange_Officer import ExchangeOfficer
from utilities.Expert_no_cmss import ExpertNoCMSS
from utilities.new_application import NewApplication
from ddt import ddt, file_data

from utilities.supervisor_role import Supervisor


@pytest.mark.usefixtures("setup")
@ddt
class Test_Exchange(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def Class_Setup(self):
        self.login = BaseDriver(self.driver)
        self.logout = BaseDriver(self.driver)
        self.new_application = NewApplication(self.driver)
        self.officer = ExchangeOfficer(self.driver)
        self.expert = ExpertNoCMSS(self.driver)
        self.closetransaction = CloseExchange(self.driver)
        self.supervisor = Supervisor(self.driver)

    # @file_data("../testdata/testdata.json")
    @file_data('../testdata/exchange/exchangetestdata.yaml')
    def test_register_exchange_transaction(self, exchangeapplicationdescription,
                                           fhfirstname, fhfathername, fhgfname, fhidfile, fhidtext, fhpocfile, fhpocref,
                                           fhpoctext, shfirstname, shfathername, shgfname, shidfile, shidtext,
                                           shpocfile,
                                           shpocref, shpoctext, cr, crreference, crdescription, fhLHC, fhLHCreference,
                                           fhLHCdescription
                                           , shLHC, shLHCreference, shLHCdescription,
                                           expertremarktext, supervisorremarktext, titledeed1, titledeed2):
        # login as officer

        self.login.log_into_nrlais("Officer", "Officer")

        # click on new application and

        self.new_application.select_new_application()

        # select special case from the list

        self.officer.register_exchange_transaction(exchangeapplicationdescription,
                                                   fhfirstname, fhfathername, fhgfname, fhidfile, fhidtext, fhpocfile,
                                                   fhpocref,
                                                   fhpoctext, shfirstname, shfathername, shgfname, shidfile, shidtext,
                                                   shpocfile,
                                                   shpocref, shpoctext, cr, crreference, crdescription, fhLHC,
                                                   fhLHCreference,
                                                   fhLHCdescription
                                                   , shLHC, shLHCreference, shLHCdescription)

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
        self.closetransaction.finalize_the_transaction(titledeed1, titledeed2)
