import time
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()


class AddCustomer:
    lnkCustomers_menu_xpath = "//i[@class='nav-icon far fa-user']"
    lnkCustomers_menuitem_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btnAddnew_xpath = "//a[@class='btn btn-primary']"
    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"
    txtcustomerRoles_xpath = "//div[@class='k-multiselect-wrap k-floatwrap']"
    lstitemAdministrators_xpath = "//li[contains(text(),'Administrators')]"
    lstitemRegistered_xpath = "//li[contains(text(),'Registered')]"
    lstitemGuests_xpath = "//li[contains(text(),'Guests')]"
    lstitemVendors_xpath = "//li[contains(text(),'Vendors')]"
    drpmgrOfVendor_xpath = "//*[@id='VendorId']"
    rdMaleGender_xpath = "//input[@id='Gender_Male']"
    rdFeMaleGender_xpath = "//input[@id='Gender_Female']"
    txtFirstName_xpath = "//input[@id='FirstName']"
    txtLastName_xpath = "//input[@id='LastName']"
    txtDob_xpath = "//input[@id='DateOfBirth']"
    txtCompanyName_xpath = "//input[@id='Company']"
    txtAdminContent_xpath = "//textarea[@id='AdminComment']"
    btnSave_xpath = "//button[@name='save']"
    txtNewsletter_xpath = "//div[@class='input-group-append']//div[@role='listbox']"
    txtTestStore_xpath = "//span[normalize-space()='Test store 2']"
    txtYouStorename_xpath=  "//span[normalize-space()='Your store name']"



    def __init__(self, driver):
        self.driver = driver

    def clickOnCustomersMenu(self):
        self.driver.find_element(By.XPATH , self.lnkCustomers_menu_xpath).click()

    def clickOnCustomersMenuItem(self):
        self.driver.find_element(By.XPATH , self.lnkCustomers_menuitem_xpath).click()

    def clickOnAddnew(self):
        self.driver.find_element(By.XPATH , self.btnAddnew_xpath).click()

    def setEmail(self , email):
        self.driver.find_element(By.XPATH ,self.txtEmail_xpath).send_keys(email)

    def setPassword(self , password):
        self.driver.find_element(By.XPATH , self.txtPassword_xpath).send_keys(password)

    def setCustomerRoles(self , role):
        self.driver.find_element(By.XPATH ,self.txtcustomerRoles_xpath).click()
        time.sleep(4)

        if role =="Registered":
            self.listitem= self.driver.find_element(By.XPATH,self.lstitemRegistered_xpath)

        elif role == "Administrators":
            self.listitem=self.driver.find_element(By.XPATH , self.lstitemAdministrators_xpath)

        elif role=="Guests":
            time.sleep(4)
            self.driver.find_element(By.XPATH,"//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.listitem = self.driver.find_element(By.XPATH,self.lstitemGuests_xpath)

        elif role == "Registered":
            self.listitem=self.driver.find_element(By.XPATH, self.lstitemRegistered_xpath)

        elif role =="Vendors":
            self.listitem=self.driver.find_element(By.XPATH , self.lstitemVendors_xpath)

        else:
            self.listitem=self.driver.find_element(By.XPATH, self.lstitemGuests_xpath)

        time.sleep(3)

        self.driver.execute_script("arguments[0].click();", self.listitem)

    def setManagerOfVendor(self , value):
        drp = Select(self.driver.find_element(By.XPATH , self.drpmgrOfVendor_xpath))
        drp.select_by_visible_text(value)

    def setGender(self , gender):
        if gender == 'male':
            self.driver.find_element(By.XPATH , self.rdMaleGender_xpath).click()

        elif gender == "female":
            self.driver.find_element(By.XPATH , self.rdFeMaleGender_xpath).click()

        else:
            self.driver.find_element(By.XPATH , self.rdMaleGender_xpath).click()

    def setFirstName(self , fname):
        self.driver.find_element(By.XPATH , self.txtFirstName_xpath).send_keys(fname)

    def setLastName(self , lname):
        self.driver.find_element(By.XPATH , self.txtLastName_xpath).send_keys(lname)

    def setDob(self , dob):
        self.driver.find_element(By.XPATH , self.txtDob_xpath).send_keys(dob)

    def setCompanyName(self, comname):
        self.driver.find_element(By.XPATH,self.txtCompanyName_xpath).send_keys(comname)

    def setAdminContent(self , content):
        self.driver.find_element(By.XPATH ,self.txtAdminContent_xpath).send_keys(content)

    def clickOnSave(self):
        self.driver.find_element(By.XPATH ,self.btnSave_xpath).click()

    def setNewsletter(self, newsletter):
        self.driver.find_element(By.XPATH, self.txtNewsletter_xpath).click()
        time.sleep(3)

        if newsletter == "Test store 2":
            element = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, self.txtTestStore_xpath))
            )
            element.click()
        else:
            element = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, self.txtYouStorename_xpath))
            )
            element.click()