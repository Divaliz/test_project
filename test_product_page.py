from .pages.product_page import ProductPage
import pytest

urls = [f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{no}" for no in range(10)]


#@pytest.mark.parametrize('link', urls, pytest.param(
    #"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail)
 #                        )
# def test_guest_can_add_product_to_basket(browser, link):
 #    # link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
  #  page = ProductPage(browser, link)
  #  page.open()
  #  page.add_to_cart_button()
  #  page.solve_quiz_and_get_code()
  #  page.price_should_match_the_product()

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart_button()
    page.guest_cant_see_success_message()


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.guest_cant_see_success_message()


def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart_button()
    page.message_disappeared_after_adding_product_to_basket()

