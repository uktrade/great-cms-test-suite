from random import choice

from selenium.webdriver.common.by import By

from tests.behavioural.pages.base import BasePage


class IntentForm(BasePage):
    def __init__(self, context):
        self.path = 'international/expand-your-business-in-the-uk/intent/'
        super().__init__(context, self.path)

    def submit(self):
        self.do_click_link((By.XPATH, "//button[text()='Continue']"))

    def error_message_visible(self):
        return self.is_visible((By.LINK_TEXT, 'You must select one or more expansion options'))

    def expansion_options_greater_than_zero(self):
        return len(self.find_elements((By.XPATH, "//form//fieldset//input[@name='intent']"))) > 0

    def choose_random_expansion_option(self):
        options = self.find_elements((By.XPATH, "//form//fieldset//input[@name='intent']"))
        element = choice(options)
        element.click()

        if element.text == 'Other':
            self.do_send_keys((By.ID, 'id_intent_other'), 'another intent')
