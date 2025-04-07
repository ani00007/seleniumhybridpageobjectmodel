from pom.homepage import HomePage
from lib.lib import Wrapper
from selenium.common.exceptions import NoSuchElementException
from time import sleep


class LoginPage(HomePage):
    txt_email = ("xpath", "//input[@id='Email']")
    txt_password = ("xpath", "//input[@id='Password']")

    def login_link(self, email, password):
        wrapper = Wrapper(self.driver)
        wrapper.enter_text(self.txt_email, value=email)
        wrapper.enter_text(self.txt_password, value=password)

    def is_user_logged_in(self, email):
        for _ in range(5):
            try:
                self.driver.find_element("xpath", f"//a[text()='{email}']")
                return True
            except NoSuchElementException:
                sleep(1)
                continue
        return False

    def is_homepage_displayed(self):
        title = "Demo Web Shop"
        if self.driver.title == title:
            return True
        return False


