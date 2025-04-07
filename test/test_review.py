from pytest import mark
from time import sleep

header = "email, password"
data = [("hulk_smash@gmail.com", "hulk1234@")]


@mark.parametrize(header, data)
def test_login(pages, email, password):
    pages.login.click_login()
    sleep(2)
    pages.login.login_link(email, password)
    sleep(1)
    pages.login.click_login_btn()
    sleep(2)
    pages.review.click_on_jewelry()
    sleep(2)
    assert pages.review.is_jewelry_page_displayed() == True
    sleep(1)

    pages.review.click_on_filter_by_price()
    sleep(2)
    assert pages.review.is_product_between_filter_price_displayed() == True

    pages.review.click_on_black_nd_white_diamond_heart()
    sleep(2)
    assert pages.review.black_white_dimond_heart_product_is_displayed() == True

