import pytest
import time

from pageObjects.SearchCustomerPage import SearchCustomer
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_SearchCustomerByName_005:
    baseURL = ReadConfig().getapplicationurl()
    username = ReadConfig().getusername()
    password = ReadConfig().getpassword()
    logger = LogGen().loggen()

    @pytest.mark.regression
    def test_searchCustomerByName(self, setup):
        self.logger.info("*****Test_SearchCustomerByName_005*****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()
        self.logger.info("*****Login Successful*****")
        self.logger.info("*****Starting search customer by name test*****")
        self.addcust = AddCustomer(self.driver)
        self.addcust.clickcustomersmenu()
        self.addcust.clickcustomersmenuitem()
        self.logger.info("*****searching customer by name*****")
        searchcust = SearchCustomer(self.driver)
        searchcust.setfname("John")
        searchcust.setlname("Smith")
        searchcust.clicksearch()
        time.sleep(3)
        status = searchcust.searchbyname("John Smith")
        self.driver.close()
        assert True == status
        self.logger.info("*****Test_SearchCustomerByName_005 finished*****")