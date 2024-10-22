from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM), \
            "Item is presented, but should not be"

    def check_basket_message_is_empty(self):
        basket_message = self.browser.find_element(*BasketPageLocators.BASKET_IS_EMPTY).text
        assert 'Your basket is empty' in basket_message, "Basket message is different"

