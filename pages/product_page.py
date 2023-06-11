from .base_page import BasePage
from .locators import ItemPageLocators

class ProductPage(BasePage):
    def add_cart(self):
        button = self.browser.find_element(*ItemPageLocators.ADD_CART)
        button.click()

    def check_item_added_name(self):
        assert self.browser.find_element(*ItemPageLocators.ITEM_NAME).text in self.browser.find_element(*ItemPageLocators.ITEM_ADDED_SUCCESS_NAME).text, "The name of the item is not the same as in the success notification"

    def check_price_item_cart_correct(self):
        assert self.browser.find_element(*ItemPageLocators.ITEM_PRICE).text in self.browser.find_element(*ItemPageLocators.CART_ADDED_PRICE).text, "The price of the item is not the same as in the notification"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ItemPageLocators.ITEM_ADDED_SUCCESS_NAME), "Success message is presented, but should not be"

    def should_dissapear(self):
        assert self.is_disappeared(*ItemPageLocators.ITEM_ADDED_SUCCESS_NAME), 'The element is still present and did not dissapear'

