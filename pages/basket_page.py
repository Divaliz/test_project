from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def guest_cant_see_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS)
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY_MSG)
