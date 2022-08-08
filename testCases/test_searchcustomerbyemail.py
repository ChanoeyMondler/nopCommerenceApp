import pytest
import time

from pageObjects.SearchCustomerPage import SearchCustomer
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_SearchCustomerByEmail_004:
    baseURL = ReadConfig().getapplicationurl()
    username = ReadConfig().getusername()
    password = ReadConfig().getpassword()
    logger = LogGen().loggen()

    @pytest.mark.regression
    def test_searchCustomerByEmail(self, setup):
        self.logger.info("*****Test_SearchCustomerByEmail_004*****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()
        self.logger.info("*****Login Successful*****")
        self.logger.info("*****Starting search customer by email test*****")
        self.addcust = AddCustomer(self.driver)
        self.addcust.clickcustomersmenu()
        self.addcust.clickcustomersmenuitem()
        self.logger.info("*****searching customer by email*****")
        searchcust = SearchCustomer(self.driver)
        searchcust.setemail("fJSpy@gmail.com")
        searchcust.clicksearch()
        time.sleep(3)
        status = searchcust.searchbyemail("fJSpy@gmail.com")
        self.driver.close()
        assert True == status
        self.logger.info("*****Test_SearchCustomerByEmail_004 finished*****")