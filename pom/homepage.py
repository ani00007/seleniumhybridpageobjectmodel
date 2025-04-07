from lib.lib import Wrapper

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def click_login(self):
        wrapper = Wrapper(self.driver)
        wrapper.click_element(("xpath", "//a[text()='Log in']"))

    def click_login_btn(self):
        wrapper = Wrapper(self.driver)
        wrapper.click_element(("xpath", "//input[@value='Log in']"))

    def click_logout_btn(self):
        wrapper = Wrapper(self.driver)
        wrapper.click_element(("xpath", "//a[text()='Log out']"))

    def click_on_register_link(self):
        wrapper = Wrapper(self.driver)
        wrapper.click_element(("xpath", "//a[text()='Register']"))

    def click_register_btn(self):
        wrapper = Wrapper(self.driver)
        wrapper.click_element(("xpath", "//input[@id='register-button']"))

    def click_continue_btn(self):
        wrapper = Wrapper(self.driver)
        wrapper.click_element(("xpath", "//input[@class='button-1 register-continue-button']"))

    def click_on_subscribe(self):
        wrapper = Wrapper(self.driver)
        wrapper.click_element(("xpath", "//input[@value='Subscribe']"))

    def click_on_search(self):
        wrapper = Wrapper(self.driver)
        wrapper.click_element(("xpath", "//input[@value='Search']"))

    def move_to_electronics(self):
        wrapper = Wrapper(self.driver)
        wrapper.mouse_hover(("xpath", "//ul[@class='top-menu']//a[contains(text(),'Electronics')]"))

    def click_on_camera_photo(self):
        wrapper = Wrapper(self.driver)
        wrapper.click_element(("xpath", "//ul[@class='top-menu']//a[contains(text(),'Camera, photo')]"))

    def click_back_button(self):
        wrapper = Wrapper(self.driver)
        wrapper.browser_back()

    def click_on_1mp_60gb_Handycam_recoder(self):
        wrapper = Wrapper(self.driver)
        wrapper.click_element(("xpath", "//a[text()='1MP 60GB Hard Drive Handycam Camcorder']"))

    def click_on_add_to_compare_list(self):
        wrapper = Wrapper(self.driver)
        wrapper.click_element(("xpath", "//input[@value='Add to compare list']"))

    def click_on_camrecorder(self):
        wrapper = Wrapper(self.driver)
        wrapper.click_element(("xpath", "//a[text()='Camcorder']"))

    def remove_camrecorder(self):
        wrapper = Wrapper(self.driver)
        wrapper.click_element(("xpath", "//img[@alt='Picture of Camcorder']/../../..//input[@value='Remove']"))

    def remove_1mp_60gb_Handycam_recoder(self):
        wrapper = Wrapper(self.driver)
        wrapper.click_element(("xpath", "//img[@alt='Picture of 1MP 60GB Hard Drive Handycam Camcorder']/../../..//input[@value='Remove']"))

    def click_on_books(self):
        wrapper = Wrapper(self.driver)
        wrapper.click_element(("xpath", "//ul[@class='top-menu']//a[contains(text(), 'Books')]"))

    def computing_internet_add_to_cart_btn(self):
        wrapper = Wrapper(self.driver)
        wrapper.click_element(("xpath", "//a[text()='Computing and Internet']/../../..//input[@value='Add to cart']"))

    def click_on_shopping_cart(self):
        wrapper = Wrapper(self.driver)
        wrapper.click_element(("xpath", "//span[text()='Shopping cart']"))

    def click_on_apparel_and_shoes(self):
        wrapper = Wrapper(self.driver)
        wrapper.click_element(("xpath", "//ul[@class='top-menu']//a[contains(text(), 'Apparel & Shoes')]"))

    def click_on_blue_green_sneaker(self):
        wrapper = Wrapper(self.driver)
        wrapper.click_element(("xpath", "//a[text()='Blue and green Sneaker']/../..//input[@value='Add to cart']"))

    def click_on_add_to_cart_blue_green_sneaker(self):
        wrapper = Wrapper(self.driver)
        wrapper.click_element(("xpath", "//input[@id='add-to-cart-button-28']"))

    def click_on_blue_green_shopping_cart(self):
        wrapper = Wrapper(self.driver)
        wrapper.click_element(("xpath", "//span[text()='Shopping cart']"))

    def product_added_message_close_btn(self):
        wrapper = Wrapper(self.driver)
        wrapper.click_element(("xpath", "//span[@title='Close']"))

    def click_on_homepage_title(self):
        wrapper = Wrapper(self.driver)
        wrapper.click_element(("xpath", "//img"))

    def click_on_update_shopping_cart(self):
        wrapper = Wrapper(self.driver)
        wrapper.click_element(("xpath", "//input[@name='updatecart']"))

    def click_on_add_to_wishlist_blue_green_sneaker(self):
        wrapper = Wrapper(self.driver)
        wrapper.click_element(("xpath", "//input[@id='add-to-wishlist-button-28']"))

    def click_on_wishlist(self):
        wrapper = Wrapper(self.driver)
        wrapper.click_element(("xpath", "//div[@class='header-links']//a[@class='ico-wishlist']"))

    # def click_quantity(self):
    #     wrapper = Wrapper(self.driver)
    #     wrapper.click_element(("xpath", "//input[@value='Update wishlist']"))

    def click_on_update(self):
        wrapper = Wrapper(self.driver)
        wrapper.click_element(("xpath", "//input[@value='Update wishlist']"))

    def click_on_jewelry(self):
        wrapper = Wrapper(self.driver)
        wrapper.click_element(("xpath", "//ul[@class='top-menu']//a[contains(text(), 'Jewelry')]"))

    def click_on_filter_by_price(self):
        wrapper = Wrapper(self.driver)
        wrapper.click_element(("xpath", "//span[text()='0.00']"))

    def click_on_black_nd_white_diamond_heart(self):
        wrapper = Wrapper(self.driver)
        wrapper.click_element(("xpath", "//a[text()='Black & White Diamond Heart']"))

    def click_on_add_your_review(self):
        wrapper = Wrapper(self.driver)
        wrapper.click_element(("xpath", "//a[text()='Add your review']"))





