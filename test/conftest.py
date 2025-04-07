from selenium import webdriver
from pytest import fixture
from pom.login import LoginPage
from pom.register import Registration
from pom.newsletter import NewsLetter
from pom.search import Search
from pom.search_and_compare import Search_and_Compare
from pom.shopping_cart import ShoppingCart
from pom.shopping_cart_conditions import ShoppingCartConditions
from pom.wishlist import Wishlist
from pom.review import Review


@fixture
def _driver():
    opt = webdriver.ChromeOptions()
    opt.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=opt)
    driver.maximize_window()
    driver.get("https://demowebshop.tricentis.com/")
    yield driver

    print("***** Teardown *****")
    driver.close()


@fixture
def pages(_driver):
    class Pages:
        login = LoginPage(_driver)
        register = Registration(_driver)
        newsletter = NewsLetter(_driver)
        search = Search(_driver)
        search_compare = Search_and_Compare(_driver)
        shopping_cart = ShoppingCart(_driver)
        shopping_cart_conditions = ShoppingCartConditions(_driver)
        wishlist = Wishlist(_driver)
        review = Review(_driver)
    return Pages()

