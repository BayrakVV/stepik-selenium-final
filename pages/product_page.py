from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_to_basket_button = self.browser.find_element(
            *ProductPageLocators.ADD_TO_BASKET_BUTTON
        )
        add_to_basket_button.click()

    def basket_price_is_product_price(self):
        product_price = self.get_text_from_element(
            *ProductPageLocators.PRODUCT_PRICE
        )
        basket_price_basket_total_price_message = self.get_text_from_element(
            *ProductPageLocators.BASKET_PRICE_IN_BASKET_TOTAL_PRICE_MESSAGE
        )
        assert product_price == basket_price_basket_total_price_message, \
            'Basket price and product price ins not equal'

    def product_is_added_to_basket(self):
        product_name = self.get_text_from_element(
            *ProductPageLocators.PRODUCT_NAME
        )
        product_name_in_product_added_message = self.get_text_from_element(
            *ProductPageLocators.PRODUCT_NAME_IN_PRODUCT_ADDED_MESSAGE
        )
        assert product_name == product_name_in_product_added_message, \
            'Product has not been added to basket'

    def should_not_be_success_message(self):

        assert self.is_not_element_present(
            *ProductPageLocators.PRODUCT_ADDED_MESSAGE
        ), 'Success message is presented, but should not be'

    def success_message_disappeared(self):
        assert self.is_disappeared(
            *ProductPageLocators.PRODUCT_ADDED_MESSAGE
        ), 'Success message didn\'t disappear'
