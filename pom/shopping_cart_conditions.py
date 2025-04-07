from pom.homepage import HomePage
from lib.lib import Wrapper
from selenium.common.exceptions import NoSuchElementException
from time import sleep


class ShoppingCartConditions(HomePage):
    locator_quantity_ = ("xpath", "//tr[@class='cart-item-row']//input[@type='text']")

    def is_apparel_and_shoes_is_displayed(self):
        locator = ("xpath", "//h1[text()='Apparel & Shoes']")
        wrapper = Wrapper(self.driver)
        for _ in range(5):
            try:
                wrapper.is_displayed(locator)
                return True
            except NoSuchElementException:
                sleep(1)
                continue
        return False

    def is_shopping_cart_and_blue_green_sneaker_is_displayed(self):
        blue_green_sneaker = ("xpath", "//td[@class='product']//a[text()='Blue and green Sneaker']")
        shopping_cart = ("xpath", "//h1[text()='Shopping cart']")
        wrapper = Wrapper(self.driver)
        for _ in range(5):
            try:
                wrapper.is_displayed(blue_green_sneaker) and wrapper.is_displayed(shopping_cart)
                return True
            except NoSuchElementException:
                sleep(1)
                continue
        return False

    def is_price_quantity_total_is_displayed(self):
        price = ("xpath", "//tr[@class='cart-item-row']//span[@class='product-unit-price' and text()='11.00']")
        quantity = ("xpath", "//tr[@class='cart-item-row']//input[@value = '1']")
        total = ("xpath", "//tr[@class='cart-item-row']//span[@class='product-subtotal' and text()='11.00' ]")
        wrapper = Wrapper(self.driver)
        for _ in range(5):
            try:
                wrapper.is_displayed(price)
                wrapper.is_displayed(quantity)
                wrapper.is_displayed(total)
                return True
            except NoSuchElementException:
                sleep(1)
                continue
        return False

    def add_quantity(self, value):
        wrapper = Wrapper(self.driver)
        wrapper.enter_text(self.locator_quantity_, value=value)

    def is_updated_price_quantity_total_is_displayed(self):
        price = ("xpath", "//tr[@class='cart-item-row']//span[@class='product-unit-price' and text()='11.00']")
        quantity = ("xpath", "//tr[@class='cart-item-row']//input[@value = '4']")
        total = ("xpath", "//tr[@class='cart-item-row']//span[@class='product-subtotal' and text()='44.00' ]")
        wrapper = Wrapper(self.driver)
        for _ in range(5):
            try:
                wrapper.is_displayed(price)
                wrapper.is_displayed(quantity)
                wrapper.is_displayed(total)
                return True
            except NoSuchElementException:
                sleep(1)
                continue
        return False
