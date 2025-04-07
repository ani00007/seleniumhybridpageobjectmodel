from pytest import mark
from time import sleep

header = "email, password"
data = [("hulk_smash@gmail.com", "hulk1234@")]

@mark.parametrize(header, data)
def test_search_compare(pages, email, password):
    pages.login.click_login()
    pages.login.login_link(email,password)
    sleep(2)
    pages.login.click_login_btn()
    sleep(2)
    assert pages.login.is_user_logged_in(email) == True

    pages.shopping_cart.click_on_books()
    assert pages.shopping_cart.is_book_page_displayed() == True

    pages.shopping_cart.computing_internet_add_to_cart_btn()
    assert pages.shopping_cart.is_product_added_confirmation_message_displayed() == True
    sleep(5)

    pages.shopping_cart.click_on_shopping_cart()
    assert pages.shopping_cart.is_shopping_cart_and_computing_internet_displayed() == True

    pages.login.click_logout_btn()
    sleep(2)
    assert pages.login.is_homepage_displayed() == True
    sleep(2)

