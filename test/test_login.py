import time

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

    assert pages.login.is_user_logged_in(email) == True
    sleep(2)

    pages.login.click_logout_btn()
    sleep(2)
    assert pages.login.is_homepage_displayed() == True
    sleep(2)






