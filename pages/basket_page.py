from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasketPageLocators
from pages.base_page import BasePage


class BasketPage(BasePage):
    def basket_is_empty(self):
        assert self.is_not_element_present(
            *BasketPageLocators.BASKET_CONTENT
        ), "Basket in not empty"
