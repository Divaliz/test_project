from .pages.product_page import ProductPage
import pytest

urls = [f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{no}" for no in range(10)]


@pytest.mark.parametrize('link', urls, pytest.param(
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail)
                         )
def test_guest_can_add_product_to_basket(browser, link):
    # link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart_button()
    page.solve_quiz_and_get_code()
    page.name_should_match_the_product()
    page.price_should_match_the_product()
