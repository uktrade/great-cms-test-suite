from random import choice

from selenium.webdriver.common.by import By

from tests.behavioural.pages.base import BasePage


class LocationForm(BasePage):
    def __init__(self, context):
        self.path = 'international/expand-your-business-in-the-uk/location/'
        super().__init__(context, self.path)

    def submit(self):
        self.do_click_link((By.XPATH, "//button[text()='Continue']"))

    def error_message_visible(self):
        location_error_visible = self.is_visible((By.LINK_TEXT, 'You must select a location'))
        not_decided_error_visible = self.is_visible((By.LINK_TEXT, 'You must select not decided'))
        return location_error_visible and not_decided_error_visible

    def expansion_options_greater_than_zero(self):
        return len(self.find_elements((By.CSS_SELECTOR, "div[class='govuk-checkboxes__item']"))) > 0

    def choose_random_expansion_option(self):
        options = self.find_elements((By.CSS_SELECTOR, "div[class='govuk-checkboxes__item']"))
        choice(options).click()

    def enter_location(self, location):
        self.do_send_keys((By.ID, 'js-location-select'), location)

    def location_list_displayed_and_count_greater_than_zero(self):
        locator = (By.XPATH, "//ul[@id='js-location-select__listbox']//li")
        child_count = len(self.find_elements(locator))
        return self.is_visible(locator) and child_count > 0

    def choose_first_location_displayed(self):
        self.do_click((By.ID, 'js-location-select__option--0'))
