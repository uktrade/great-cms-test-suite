from random import choice

from selenium.webdriver.common.by import By

from tests.behavioural.pages.base import BasePage


class SpendForm(BasePage):
    def __init__(self, context):
        self.path = 'international/expand-your-business-in-the-uk/spend/'
        super().__init__(context, self.path)

    def submit(self):
        self.do_click_link((By.XPATH, "//button[text()='Continue']"))

    def error_message_visible(self):
        return self.is_visible((By.LINK_TEXT, 'You must select at least one spend option'))

    def currency_selector_visible(self):
        return self.is_visible((By.ID, 'id_spend_currency'))

    def select_random_currency(self):
        self.do_click((By.ID, 'id_spend_currency'))
        currency_options = self.find_elements((By.XPATH, "//select[@id='id_spend_currency']//option"))
        choice(currency_options).click()
        self.do_click_link((By.XPATH, "//form//button[text()='Select']"))
        # submitting this form reloads the page, wait before continuing
        self.wait_for_url_change(self.url)

    def spend_options_greater_than_zero(self):
        return len(self.find_elements((By.XPATH, "//input[@name='spend']"))) > 0

    def choose_random_spend_option(self):
        # click on the label because parent div is full width and so clicking in the middle doesn't set value
        options = self.find_elements((By.XPATH, "//input[@name='spend']/following-sibling::label"))
        choice(options).click()
