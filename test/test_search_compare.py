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

    pages.search_compare.move_to_electronics()
    pages.search_compare.click_on_camera_photo()
    sleep(2)
    assert pages.search_compare.is_camrea_photo_displayed() == True

    sleep(2)
    pages.search_compare.click_on_1mp_60gb_Handycam_recoder()
    sleep(2)
    assert pages.search_compare.is_1mp_60gb_Handycam_recoder_displayed() == True

    sleep(2)
    pages.search_compare.click_on_add_to_compare_list()
    sleep(2)
    assert pages.search_compare.is_compare_product_page_displayed() == True

    for _ in range(2):
        pages.search_compare.click_back_button()
        sleep(2)
    assert pages.search_compare.is_camrea_photo_displayed() == True

    pages.search_compare.click_on_camrecorder()
    sleep(1)
    assert pages.search_compare.is_camrecorder_displayed() == True

    pages.search_compare.click_on_add_to_compare_list()
    sleep(1)
    assert pages.search_compare.is_compare_page_and_camrecorder_displayed() == True

    pages.search_compare.remove_camrecorder()
    sleep(1)
    assert pages.search_compare.is_camrecorder_displayed() == False

    pages.search_compare.remove_1mp_60gb_Handycam_recoder()
    sleep(1)
    assert pages.search_compare.is_1mp_60gb_Handycam_recoder_displayed() == False

    assert pages.search_compare.is_comapre_page_empty_message_displayed() == True
    sleep(2)

    pages.login.click_logout_btn()
    sleep(2)
    assert pages.login.is_homepage_displayed() == True
    sleep(2)
