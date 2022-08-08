import pytest
import random
import string
from selenium.webdriver.common.by import By

from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return "".join(random.choice(chars) for x in range(size))


class Test_003_AddCustomer:
    baseURL = ReadConfig().getapplicationurl()
    username = ReadConfig.getusername()
    password = ReadConfig.getpassword()
    logger = LogGen().loggen()

    @pytest.mark.sanity
    def test_addcustomer(self, setup):
        self.logger.info("*****Test_003_AddCustomer*****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        self.lp = LoginPage(self.driver)

        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()

        self.logger.info("*****Login successful*****")
        self.logger.info("*****Starting Add Customer Test*****")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickcustomersmenu()
        self.addcust.clickcustomersmenuitem()
        self.addcust.clickaddnew()

        self.logger.info("*****Providing customer info*****")

        self.email = random_generator() + "@163.com"
        self.addcust.enteremail(self.email)
        self.addcust.enterpassword("kruse123")
        self.addcust.enterfname("Monica")
        self.addcust.enterlname("Geller")
        self.addcust.selectgender("Female")
        self.addcust.enterdob("08/23/1985")
        self.addcust.entercompanyname("Central Perk")
        self.addcust.selectcustomersrole("Guests")
        self.addcust.entermgrofvendor("Vendor 2")
        self.addcust.enteradmincomment("This is for test purpose...")
        self.addcust.clicksave()

        self.logger.info("*****Save customer info*****")
        self.logger.info("***** Add customer validation started*****")

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text

        if "The new customer has been added successfully." in self.msg:
            assert True
            self.logger.info("*****Add new customer test passed*****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_addcustomer_scr.png")
            self.logger.error("*****Add new customer test failed*****")
            assert False

        self.driver.close()
        self.logger.info("*****Add customer test completed*****")





