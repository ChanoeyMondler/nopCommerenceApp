import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    baseURL = ReadConfig().getapplicationurl()
    username = ReadConfig.getusername()
    password = ReadConfig.getpassword()

    logger = LogGen().loggen()


    @pytest.mark.regression
    def test_homepagetitle(self, setup):
        self.logger.info("********Test_001_Login********")
        self.logger.info("********Verifying Home Page Title********")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("********Home page title test is passed********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homepagetitle.png")
            self.driver.close()
            self.logger.error("********Home page title test is failed********")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("********Verifying Login test********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("********Login test is passed********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            self.logger.error("********Login test failed********")
            assert False


