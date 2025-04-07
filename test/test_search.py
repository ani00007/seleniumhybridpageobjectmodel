from pytest import mark
from time import sleep

header = "email, password, product"
data = [("hulk_smash@gmail.com", "hulk1234@", "computer")]

@mark.parametrize(header, data)
def test_search(pages, email, password, product):
    pages.login.click_login()
    pages.login.login_link(email,password)
    sleep(2)
    pages.login.click_login_btn()
    sleep(2)
    assert pages.login.is_user_logged_in(email) == True

    pages.search.enter_search_keyword(product)
    sleep(2)
    pages.search.click_on_search()
    sleep(2)

    assert pages.search.is_computer_product_sidplayed() == True
    sleep(2)

    pages.login.click_logout_btn()
    sleep(2)
    assert pages.login.is_homepage_displayed() == True
    sleep(2)




