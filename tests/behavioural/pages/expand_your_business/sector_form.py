from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from tests.behavioural.pages.base import BasePage


class SectorForm(BasePage):
    def __init__(self, context):
        self.path = 'international/expand-your-business-in-the-uk/sector/'
        super().__init__(context, self.path)

    def submit(self):
        self.do_click_link((By.XPATH, "//button[text()='Continue']"))

    def error_message_visible(self):
        return self.is_visible((By.LINK_TEXT, 'You must enter your business sector'))

    def enter_sector(self, sector):
        self.do_send_keys((By.ID, 'js-sector-select'), sector)

    def sector_list_displayed_and_count_greater_than_zero(self):
        locator = (By.XPATH, "//ul[@id='js-sector-select__listbox']//li")
        child_count = len(self.find_elements(locator))
        return self.is_visible(locator) and child_count > 0

    def choose_first_sector_displayed(self):
        element = self.find_element((By.ID, 'js-sector-select__option--0'))
        text = element.text
        element.click()
        return text

    def clear_sector_entry(self):
        self.do_send_keys((By.ID, 'js-sector-select'), Keys.BACKSPACE * 255)
