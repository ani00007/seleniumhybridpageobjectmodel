from pom.homepage import HomePage
from lib.lib import Wrapper
from selenium.common.exceptions import NoSuchElementException
from time import sleep


class Wishlist(HomePage):
    def select_catagory(self):
        l = ["4", "8", "12"]
        count = 0
        for i in l:
            dropdown = ("xpath", "//select[@id='products-pagesize']")
            wrapper = Wrapper(self.driver)
            wrapper.select_element(dropdown, value=i)
            sleep(2)
            products = self.driver.find_elements("xpath", "//div[@class='item-box']")
            if int(i) == len(products):
                count += 1
                continue
        if count == len(l):
            return True
        else:
            return False

    def is_blue_green_shoes_product_is_displayed(self):
        blue_green_sneaker = ("xpath", "//form[@id='product-details-form']")
        wrapper = Wrapper(self.driver)
        for _ in range(5):
            try:
                wrapper.is_displayed(blue_green_sneaker)
                return True
            except NoSuchElementException:
                sleep(1)
                continue
        return False

    def is_product_added_to_your_wishlist_message_displayed(self):
        message = ("xpath", "//p[text()='The product has been added to your ']")
        wrapper = Wrapper(self.driver)
        for _ in range(5):
            try:
                wrapper.is_displayed(message)
                return True
            except NoSuchElementException:
                sleep(1)
                continue
        return False

    def is_wishlist_page_displayes_with_blue_green_sneaker(self):
        wishlist = ("xpath", "//h1[contains(text(), 'Wishlist')]")
        sneaker = ("xpath", "//a[text()='Blue and green Sneaker']")
        wrapper = Wrapper(self.driver)
        for _ in range(5):
            try:
                if (self.driver.find_element(*wishlist).is_displayed()) and (self.driver.find_element(*sneaker).is_displayed()):
                    return True
            except NoSuchElementException:
                sleep(1)
                continue
        return False

    # def is_wishlist_quantity_is_zero(self):
    #     quantity = ("xpath", "//input[@class='qty-input']")
    #     update = ("xpath", "//input[@value='Update wishlist']")
    #     message = ("xpath", "//div[@class='wishlist-content']")
    #     wrapper = Wrapper(self.driver)
    #     wrapper.enter_text(quantity, value="0")
    #     wrapper.click_element(update)
    #
    #     for _ in range(5):
    #         try:
    #             self.driver.find_element(message)

    def quantity(self):
        quantity = ("xpath", "//input[@class='qty-input']")
        wrapper = Wrapper(self.driver)
        wrapper.enter_text(quantity, value="0")
        
    def is_wishlist_empty_message_displayed(self):
        message = ("xpath", "//div[@class='wishlist-content']")
        wrapper = Wrapper(self.driver)
        for _ in range(5):
            try:
                wrapper.is_displayed(message)
                return True
            except NoSuchElementException:
                sleep(1)
                continue
        return False

