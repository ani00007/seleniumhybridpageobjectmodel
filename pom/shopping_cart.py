from pom.homepage import HomePage
from lib.lib import Wrapper
from selenium.common.exceptions import NoSuchElementException
from time import sleep


class ShoppingCart(HomePage):

    def is_book_page_displayed(self):
        for _ in range(5):
            try:
                self.driver.find_element("xpath", "//h1[text()='Books']").is_displayed()
                return True
            except NoSuchElementException:
                sleep(1)
                continue
        return False

    def is_product_added_confirmation_message_displayed(self):
        for _ in range(5):
            try:
                self.driver.find_element("xpath", "//p[text()='The product has been added to your ']").is_displayed()
                return True
            except NoSuchElementException:
                sleep(1)
                continue
        return False

    def is_shopping_cart_and_computing_internet_displayed(self):
        for _ in range(5):
            try:
                self.driver.find_element("xpath", "//h1[text()='Shopping cart']").is_displayed() and self.driver.find_element("xpath", "//td[@class='product']//a[text()='Computing and Internet']").is_displayed()
                return True
            except NoSuchElementException:
                sleep(1)
                continue
        return False

