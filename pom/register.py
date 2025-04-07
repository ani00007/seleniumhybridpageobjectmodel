from pom.homepage import HomePage
from lib.lib import Wrapper
from time import sleep
from selenium.common.exceptions import NoSuchElementException


class Registration(HomePage):
    rdo_male = ("xpath", "//input[@id='gender-male']")
    rdo_female = ("xpath", "//input[@id='gender-female']")
    txt_first_name = ("xpath", "//input[@id='FirstName']")
    txt_last_name = ("xpath", "//input[@id='LastName']")
    txt_email = ("xpath", "//input[@id='Email']")
    txt_password = ("xpath", "//input[@id='Password']")
    txt_confirm_password = ("xpath", "//input[@id='ConfirmPassword']")
    lbl_registration_success_message = ("xpath", "//div[contains(text(), 'Your registration completed')]")

    def register(self, gender, fname, lname, email, password):
        wrapper = Wrapper(self.driver)
        if gender == "male":
            wrapper.click_element(self.rdo_male)
        else:
            wrapper.click_element(self.rdo_female)
        wrapper.enter_text(self.txt_first_name, value=fname)
        wrapper.enter_text(self.txt_last_name, value=lname)
        wrapper.enter_text(self.txt_email, value=email)
        wrapper.enter_text(self.txt_password, value=password)
        wrapper.enter_text(self.txt_confirm_password, value=password)

    def is_user_registered(self):
        for _ in range(5):
            try:
                self.driver.find_element(*self.lbl_registration_success_message).is_displayed()
                return True
            except NoSuchElementException:
                sleep(1)
                continue
        return False

