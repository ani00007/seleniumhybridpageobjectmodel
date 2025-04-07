from pom.homepage import HomePage
from lib.lib import Wrapper
from selenium.common.exceptions import NoSuchElementException
from time import sleep

class Search(HomePage):
    search_box = ("xpath", "//input[@id='small-searchterms']")

    def enter_search_keyword(self,value):
        wrapper = Wrapper(self.driver)
        wrapper.enter_text(self.search_box, value=value)

    def is_computer_product_sidplayed(self):
        products = self.driver.find_elements("xpath", "//h2[@class='product-title']")
        res = []
        for product in products:
            if "computer" in product.text or "Computer" in product.text:
                res.append(product.text)
        for item in res:
            try:
                self.driver.find_element("xpath", f"//h2[@class='product-title']//a[contains(text(), '{item}')]")
                return True
            except NoSuchElementException:
                continue
        return False
