import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class AddCustomer:
    link_customers_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    link_customers_menuitem_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btn_addnew_xpath = "//a[normalize-space()='Add new']"
    textbox_email_id = "Email"
    textbox_password_id = "Password"
    textbox_fname_id = "FirstName"
    textbox_lname_id = "LastName"
    rd_mgender_id = "Gender_Male"
    rd_fgender_id = "Gender_Female"
    textbox_dob_id = "DateOfBirth"
    textbox_companyname_id = "Company"
    textbox_istaxexempt_id = "IsTaxExempt"
    textbox_newsletter_xpath = "//div[@class='input-group-append']//div[@class='k-widget k-multiselect k-multiselect-clearable']"
    ls_yourstorename_xpath = "//span[normalize-space()='Your store name']"
    ls_teststore_xpath = "//span[normalize-space()='Test store 2']"
    textbox_customerrole_xpath = "//div[@class='input-group-append input-group-required']//div[@role='listbox']"
    ls_admin_xpath = "//span[normalize-space()='Administrators']"
    ls_fm_xpath = "//span[normalize-space()='Forum Moderators']"
    ls_guest_xpath = "//*[@id='SelectedCustomerRoleIds_listbox']/li[3]"
    ls_registered_xpath = "//span[normalize-space()='Registered']"
    ls_vendor_xpath = "//span[normalize-space()='Vendors']"
    drp_mgrofvendor_xpath = "//select[@id='VendorId']"
    textbox_active_id = "Active"
    textbox_admincomment_id = "AdminComment"
    btn_save_xpath = "//button[@name='save']"

    def __init__(self, driver):
        self.driver = driver

    def clickcustomersmenu(self):
        self.driver.find_element(By.XPATH, self.link_customers_menu_xpath).click()

    def clickcustomersmenuitem(self):
        self.driver.find_element(By.XPATH, self.link_customers_menuitem_xpath).click()

    def clickaddnew(self):
        self.driver.find_element(By.XPATH, self.btn_addnew_xpath).click()

    def enteremail(self, email):
        self.driver.find_element(By.ID, self.textbox_email_id).send_keys(email)

    def enterpassword(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def enterfname(self, firstname):
        self.driver.find_element(By.ID, self.textbox_fname_id).send_keys(firstname)

    def enterlname(self, lastname):
        self.driver.find_element(By.ID, self.textbox_lname_id).send_keys(lastname)

    def selectgender(self, gender):
        if gender == "Male":
            self.driver.find_element(By.ID, self.rd_mgender_id).click()
        elif gender == "Female":
            self.driver.find_element(By.ID, self.rd_fgender_id).click()
        else:
            self.driver.find_element(By.ID, self.rd_mgender_id).click()

    def enterdob(self, dob):
        self.driver.find_element(By.ID, self.textbox_dob_id).send_keys(dob)

    def entercompanyname(self, companyname):
        self.driver.find_element(By.ID, self.textbox_companyname_id).send_keys(companyname)

    def entertaxexempt(self):
        self.driver.find_element(By.ID, self.textbox_istaxexempt_id).click()

    def enternewsletter(self):
        self.driver.find_element(By.XPATH, self.textbox_newsletter_xpath).click()

    def setnewsitem1(self):
        self.driver.find_element(By.XPATH, self.ls_yourstorename_xpath).click()

    def setnewsitem2(self):
        self.driver.find_element(By.XPATH, self.ls_teststore_xpath).click()

    def selectcustomersrole(self, role):
        self.driver.find_element(By.XPATH, self.textbox_customerrole_xpath).click()
        time.sleep(2)
        if role == "Registered":
            self.listitem = self.driver.find_element(By.XPATH, self.ls_registered_xpath)
        elif role == "Administrators":
            self.listitem = self.driver.find_element(By.XPATH, self.ls_admin_xpath)
        elif role == "Forum Moderators":
            self.listitem = self.driver.find_element(By.XPATH, self.ls_fm_xpath)
        elif role == "Vendors":
            self.listitem = self.driver.find_element(By.XPATH, self.ls_vendor_xpath)
        elif role == "Guests":
            self.driver.find_element(By.XPATH, "//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.listitem = self.driver.find_element(By.XPATH, self.ls_guest_xpath)
        else:
            self.listitem = self.driver.find_element(By.XPATH, self.ls_guest_xpath)
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def entermgrofvendor(self, value):
        drp = Select(self.driver.find_element(By.XPATH, self.drp_mgrofvendor_xpath))
        drp.select_by_visible_text(value)

    def enteractive(self):
        self.driver.find_element(By.ID, self.textbox_active_id).click()

    def enteradmincomment(self, msg):
        self.driver.find_element(By.ID, self.textbox_admincomment_id).send_keys(msg)

    def clicksave(self):
        self.driver.find_element(By.XPATH, self.btn_save_xpath).click()















