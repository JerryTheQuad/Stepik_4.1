from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')

class LoginPageLocators():
    SIGN_IN = (By.CSS_SELECTOR, '#login_form')
    SIGN_UP = (By.CSS_SELECTOR, '#register_form')
    SIGN_UP_EMAIL = (By.NAME, 'registration-email')
    SIGN_UP_PASS = (By.NAME, 'registration-password1')
    SIGN_UP_PASS_CONFIRM = (By.NAME, 'registration-password2')
    SIGN_UP_BUTTON = (By.NAME, 'registration_submit')

class ItemPageLocators():
    ITEM_NAME = (By.TAG_NAME, 'h1')
    ADD_CART = (By.CSS_SELECTOR, 'button.btn-add-to-basket')
    ITEM_ADDED_SUCCESS_NAME = (By.CSS_SELECTOR, 'div.alertinner')
    ITEM_PRICE = (By.CSS_SELECTOR, 'p.price_color')
    CART_ADDED_PRICE = (By.CSS_SELECTOR, 'div.alert-info')

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_LINK = (By.PARTIAL_LINK_TEXT, 'basket')
    BASKET_ITEMS = (By.CSS_SELECTOR, 'div.basket-items')
    BASKET_EMPTY = (By.XPATH, '//div[@id="content_inner"]/p')
