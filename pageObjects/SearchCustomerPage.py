from selenium.webdriver.common.by import By


class SearchCustomer:
    textbox_email_id = "SearchEmail"
    textbox_fname_id = "SearchFirstName"
    textbox_lname_id = "SearchLastName"
    btn_search_id = "search-customers"

    # searchtableresult_xpath = "//table[@role='grid']"
    # table_xpath = "//table[@id='customers-grid']"
    tablerow_xpath = "//table[@id='customers-grid']//tr"
    tablecolumn_xpath = "//table[@id='customers-grid']//tr/td"

    def __init__(self, driver):
        self.driver = driver

    def setemail(self, email):
        self.driver.find_element(By.ID, self.textbox_email_id).clear()
        self.driver.find_element(By.ID, self.textbox_email_id).send_keys(email)

    def setfname(self, fname):
        self.driver.find_element(By.ID, self.textbox_fname_id).clear()
        self.driver.find_element(By.ID, self.textbox_fname_id).send_keys(fname)

    def setlname(self, lname):
        self.driver.find_element(By.ID, self.textbox_lname_id).clear()
        self.driver.find_element(By.ID, self.textbox_lname_id).send_keys(lname)

    def clicksearch(self):
        self.driver.find_element(By.ID, self.btn_search_id).click()

    def getrowno(self):
        return len(self.driver.find_elements(By.XPATH, self.tablerow_xpath))

    def getcolumnno(self):
        return len(self.driver.find_elements(By.XPATH, self.tablecolumn_xpath))

    def searchbyemail(self, email):
        flag = False
        for r in range(1, self.getrowno()+1):
            # table = self.driver.find_element(By.XPATH, self.table_xpath)
            emailid = self.driver.find_element(By.XPATH, "//table[@id='customers-grid']//tr["+str(r)+"]/td[2]").text
            if emailid == email:
                flag = True
                break
        return flag

    def searchbyname(self, fullname):
        flag = False
        for r in range(1, self.getrowno()+1):
            name = self.driver.find_element(By.XPATH, "//table[@id='customers-grid']//tr["+str(r)+"]/td[3]").text
            if name == fullname:
                flag = True
                break
        return flag