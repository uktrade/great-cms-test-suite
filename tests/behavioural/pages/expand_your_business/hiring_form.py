from random import choice

from selenium.webdriver.common.by import By

from tests.behavioural.pages.base import BasePage


class HiringForm(BasePage):
    def __init__(self, context):
        self.path = 'international/expand-your-business-in-the-uk/hiring/'
        super().__init__(context, self.path)

    def submit(self):
        self.do_click_link((By.XPATH, "//button[text()='Continue']"))

    def error_message_visible(self):
        return self.is_visible((By.LINK_TEXT, 'You must select at least one hiring option'))

    def hiring_options_greater_than_zero(self):
        return len(self.find_elements((By.XPATH, "//div[@id='hiring']//div[@class='govuk-radios__item']"))) > 0

    def choose_random_hiring_option(self):
        options = self.find_elements((By.XPATH, "//div[@id='hiring']//div[@class='govuk-radios__item']//label"))
        choice(options).click()
