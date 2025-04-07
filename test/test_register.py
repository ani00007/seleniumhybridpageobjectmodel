from time import sleep
from pytest import mark

header = "gender, firstname, lastname, email, password"
data = [
    ("male", "john", "wick", "johnwick999@gmail.com", "yeah@123" )
]

@mark.parametrize(header, data)
def test_register(pages, gender, firstname, lastname, email, password):
    pages.register.click_on_register_link()
    pages.register.register(gender, firstname, lastname, email, password)
    sleep(2)
    pages.register.click_register_btn()

    assert pages.register.is_user_registered() == True
    pages.register.click_continue_btn()
    pages.register.click_logout_btn()
    sleep(2)
    assert pages.login.is_homepage_displayed() == True



