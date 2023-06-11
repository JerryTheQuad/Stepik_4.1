from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def no_item_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), 'There is an item in the basket, but should not be'
    def basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY), 'The basket is not empty, but should be'