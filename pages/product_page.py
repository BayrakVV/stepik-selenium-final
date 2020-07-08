from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        add_to_basket_button = self.browser.find_element(
            *ProductPageLocators.ADD_TO_BASKET_BUTTON
        )
        add_to_basket_button.click()

    def product_is_added_to_basket(self):
        product_name = self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME
        )
        product_added_message = self.browser.find_element(
            *ProductPageLocators.PRODUCT_ADDED_MESSAGE
        )
        assert product_name.text in product_added_message.text, \
            'Product has not been added to basket'

    def basket_price_is_product_price(self):
        product_price = self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE
        )
        basket_total_price_message = self.browser.find_element(
            *ProductPageLocators.BASKET_TOTAL_PRICE_MESSAGE
        )
        assert product_price.text in basket_total_price_message.text, \
            'Basket price and product price ins not equal'
