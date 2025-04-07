from pytest import mark
from time import sleep

header = "email, password"
data = [("hulk_smash@gmail.com", "hulk1234@")]

@mark.parametrize(header, data )
def test_wishlist(pages, email, password):
    pages.login.click_login()
    sleep(2)
    pages.login.login_link(email, password)
    sleep(1)
    pages.login.click_login_btn()
    sleep(2)

    assert pages.login.is_user_logged_in(email) == True
    sleep(2)

    pages.wishlist.click_on_apparel_and_shoes()
    assert pages.shopping_cart_conditions.is_apparel_and_shoes_is_displayed() == True
    sleep(2)
    assert pages.wishlist.select_catagory() == True
    sleep(2)

    pages.wishlist.click_on_blue_green_sneaker()
    sleep(2)
    assert pages.wishlist.is_blue_green_shoes_product_is_displayed() == True

    pages.wishlist.click_on_add_to_wishlist_blue_green_sneaker()
    sleep(5)
    assert pages.wishlist.is_product_added_to_your_wishlist_message_displayed() == True

    pages.wishlist.click_on_wishlist()
    sleep(5)
    assert pages.wishlist.is_wishlist_page_displayes_with_blue_green_sneaker() == True

    # pages.wishlist.click_quantity()
    pages.wishlist.quantity()
    pages.wishlist.click_on_update()
    sleep(2)
    assert pages.wishlist.is_wishlist_empty_message_displayed() == True
    sleep(1)





