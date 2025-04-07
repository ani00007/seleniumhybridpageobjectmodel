from time import sleep
from pytest import mark

header = "email"
data = ["johnwick999@gmail.com"]

@mark.parametrize(header, data)
def test_newsletter(pages, email):
    pages.newsletter.newsletter(email)
    sleep(2)
    pages.newsletter.click_on_subscribe()
    sleep(2)

    assert pages.newsletter.is_user_registered() == True
    sleep(1)
