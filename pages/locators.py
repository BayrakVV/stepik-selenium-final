from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.ID, 'registration_link')


class LoginPageLocators:
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.XPATH, '//button[@value="Add to basket"]')
    PRODUCT_NAME = (By.XPATH, '//*[@class="col-sm-6 product_main"]/child::h1')
    PRODUCT_PRICE = (By.XPATH, '//p[@class="price_color"]')
    PRODUCT_ADDED_MESSAGE = (By.CLASS_NAME, 'alert-success:nth-child(1)')
    BASKET_TOTAL_PRICE_MESSAGE = (By.CLASS_NAME, 'alert-info')
