from pom.homepage import HomePage
from lib.lib import Wrapper
from selenium.common.exceptions import NoSuchElementException
from time import sleep

class Search_and_Compare(HomePage):

    def is_camrea_photo_displayed(self):

        for _ in range(5):
            try:
                self.driver.find_element("xpath", "//h1[text()='Camera, photo']").is_displayed()
                return True
            except NoSuchElementException:
                sleep(1)
                continue
        return False

    def is_1mp_60gb_Handycam_recoder_displayed(self):
        for _ in range(5):
            try:
                self.driver.find_element("xpath", "//h1[contains(text(),'1MP 60GB Hard Drive Handycam Camcorder')]").is_displayed()
                return True
            except NoSuchElementException:
                sleep(1)
                continue
        return False

    def is_compare_product_page_displayed(self):
        for _ in range(5):
            try:
                self.driver.find_element("xpath", "//h1[text()='Compare products']").is_displayed() and self.driver.find_element("xpath", "//a[text()='1MP 60GB Hard Drive Handycam Camcorder']").is_displayed()
                return True
            except NoSuchElementException:
                sleep(1)
                continue
        return False

    def is_camrecorder_displayed(self):
        for _ in range(5):
            try:
                self.driver.find_element("xpath", "//h1[contains(text(),'Camcorder')]").is_displayed()
                return True
            except NoSuchElementException:
                sleep(1)
                continue
        return False

    def is_compare_page_and_camrecorder_displayed(self):
        for _ in range(5):
            try:
                self.driver.find_element("xpath", "//h1[text()='Compare products']").is_displayed() and self.driver.find_element("xpath", "//a[text()='Camcorder']").is_displayed()
                return True
            except NoSuchElementException:
                sleep(1)
                continue
        return False

    def is_comapre_page_empty_message_displayed(self):
        for _ in range(5):
            try:
                self.driver.find_element("xpath", "//div[@class='page-body']").is_displayed()
                return True
            except NoSuchElementException:
                sleep(1)
                continue
        return False



