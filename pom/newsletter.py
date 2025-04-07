from pom.homepage import HomePage
from lib.lib import Wrapper
from selenium.common.exceptions import NoSuchElementException
from time import sleep


class NewsLetter(HomePage):
    txt_newsletter = ("id", "newsletter-email")
    verification_message = ("xpath", "//div[@id='newsletter-result-block']")

    def newsletter(self, email):
        wrapper = Wrapper(self.driver)
        wrapper.enter_text(self.txt_newsletter, value=email)

    def is_user_registered(self):
        try:
            self.driver.find_element(*self.verification_message).is_displayed()
            return True
        except NoSuchElementException:
            return False
