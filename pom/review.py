from pom.homepage import HomePage
from lib.lib import Wrapper
from selenium.common.exceptions import NoSuchElementException
from time import sleep


class Review(HomePage):
    def is_jewelry_page_displayed(self):
        locator = ("xpath", "//h1[text()='Jewelry']")
        wrapper = Wrapper(self.driver)
        for _ in range(5):
            try:
                wrapper.is_displayed(locator)
                return True
            except NoSuchElementException:
                sleep(1)
                continue
        return False

    def is_product_between_filter_price_displayed(self):
        locator = self.driver.find_elements("xpath", "//span[@class='price actual-price']")
        prices = [i.text for i in locator]
        print(prices)
        count = 0
        for j in prices:
            if 0.00 <= float(j) <= 500.00:
                count += 1
                continue
        if count == len(prices):
            return True
        else:
            return False

    def black_white_dimond_heart_product_is_displayed(self):
        locator = ("xpath", "//h1[contains(text(),'Black & White Diamond Heart')]")
        wrapper = Wrapper(self.driver)
        for _ in range(5):
            try:
                wrapper.is_displayed(locator)
                return True
            except NoSuchElementException:
                sleep(1)
                continue
        return False

    def is_product_review_for_black_white_heart_diamond_displayed(self):
        locator = ("xpath", "//h1[text()='Product reviews for ']")
        wrapper = Wrapper(self.driver)
        for _ in range(5):
            try:
                wrapper.is_displayed(locator)
                return True
            except NoSuchElementException:
                sleep(1)
                continue
        return False
