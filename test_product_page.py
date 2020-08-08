from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.login_page import BasePage
import pytest

urls = [f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{no}" for no in range(10)]


#@pytest.mark.parametrize('link', urls, pytest.param(
#    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail)
#                        )
#def test_guest_can_add_product_to_basket(browser, link):
#    link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
#    page = ProductPage(browser, link)
#    page.open()
#    page.add_to_cart_button()
#    page.solve_quiz_and_get_code()
#    page.price_should_match_the_product()


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


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.guest_cant_see_product_in_basket()


@pytest.fixture(scope="class")
def setup(browser):
    page = BasePage.go_to_login_page()
    page.register_new_user()
    page.should_be_authorized_user()


class TestUserAddToBasketFromProductPage:
    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.guest_cant_see_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        page = ProductPage(browser, link)
        page.open()
        page.add_to_cart_button()
        page.solve_quiz_and_get_code()
        page.price_should_match_the_product()
