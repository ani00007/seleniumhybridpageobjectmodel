from pytest import mark
from time import sleep

header = "email, password, quantity"
data = [("hulk_smash@gmail.com", "hulk1234@", "4")]

@mark.parametrize(header, data)
def test_search_compare(pages, email, password, quantity):
    pages.login.click_login()
    pages.login.login_link(email,password)
    sleep(2)
    pages.login.click_login_btn()
    sleep(2)
    assert pages.login.is_user_logged_in(email) == True

    pages.shopping_cart_conditions.click_on_apparel_and_shoes()
    sleep(2)
    assert pages.shopping_cart_conditions.is_apparel_and_shoes_is_displayed() == True

    pages.shopping_cart_conditions.click_on_blue_green_sneaker()
    sleep(2)
    pages.shopping_cart_conditions.click_on_add_to_cart_blue_green_sneaker()
    assert pages.shopping_cart.is_product_added_confirmation_message_displayed() == True
    sleep(2)
    pages.shopping_cart_conditions.product_added_message_close_btn()

    pages.shopping_cart_conditions.click_on_blue_green_shopping_cart()
    sleep(3)

    assert pages.shopping_cart_conditions.is_shopping_cart_and_blue_green_sneaker_is_displayed() == True
    assert pages.shopping_cart_conditions.is_price_quantity_total_is_displayed() == True
    sleep(2)

    pages.shopping_cart_conditions.add_quantity(quantity)
    pages.shopping_cart_conditions.click_on_update_shopping_cart()
    sleep(3)
    assert pages.shopping_cart_conditions.is_updated_price_quantity_total_is_displayed() == True


    # pages.shopping_cart_conditions.click_on_homepage_title()
    # sleep(2)
    # pages.shopping_cart_conditions.click_on_shopping_cart()
    # sleep(5)


