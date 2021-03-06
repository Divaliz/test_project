from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_cart_button(self):
        btn = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        btn.click()

    def name_should_match_the_product(self):
        msg = self.browser.find_element(*ProductPageLocators.ADDED_TO_CART_MSG)
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        assert msg.text == product_name.text, "name is not matching"

    def price_should_match_the_product(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        total_in_basket = self.browser.find_element(*ProductPageLocators.TOTAL_IN_BASKET_MSG)
        assert total_in_basket.text == product_price.text, "price is not matching"

    def guest_cant_see_success_message(self):
        assert BasePage.is_not_element_present(self, *ProductPageLocators.ADDED_TO_CART_MSG)

    def message_disappeared_after_adding_product_to_basket(self):
        assert BasePage.is_disappeared(self, *ProductPageLocators.ADDED_TO_CART_MSG)





