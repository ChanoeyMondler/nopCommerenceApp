import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import excelUtils

class Test_002_DDT_Login:
    baseURL = ReadConfig().getapplicationurl()
    path = ".\\testData\\LoginData.xlsx"
    logger = LogGen().loggen()


    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.logger.info("********Test_002_DDT_Login Starts********")
        self.logger.info("********Verifying Login_ddt test********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.rowno = excelUtils.getrowcount(self.path, "Sheet1")
        lst_status = []

        for row in range(2, self.rowno+1):
            # read test data from excel
            self.username = excelUtils.readdata(self.path, "Sheet1", row, 1)
            self.password = excelUtils.readdata(self.path, "Sheet1", row, 2)
            self.exp_result = excelUtils.readdata(self.path, "Sheet1", row, 3)
            # enter the data from excel to application
            self.lp.setusername(self.username)
            self.lp.setpassword(self.password)
            self.lp.clicklogin()

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp_result == "Pass":
                    excelUtils.writedata(self.path, "Sheet1", row, 4, "Pass")
                    self.logger.info("***Pass***")
                    self.lp.clicklogout()
                    lst_status.append("Pass")
                elif self.exp_result == "Fail":
                    excelUtils.writedata(self.path, "Sheet1", row, 4, "Fail")
                    self.logger.info("***failed***")
                    self.lp.clicklogout()
                    lst_status.append("Fail")
            elif act_title != exp_title:
                if self.exp_result == "Pass":
                    excelUtils.writedata(self.path, "Sheet1", row, 4, "Fail")
                    self.logger.info("*** failed***")
                    lst_status.append("Fail")
                elif self.exp_result == "Fail":
                    excelUtils.writedata(self.path, "Sheet1", row, 4, "Pass")
                    self.logger.info("***passed***")
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            self.logger.info("Login DDT test passed")
            self.driver.close()
            assert True
        else:
            self.logger.info("Login DDT test failed")
            self.driver.close()
            assert False

        self.logger.info("*****End of Login DDT Test*****")
        self.logger.info("*****Completed TC_LoginDDT_002*****")


















