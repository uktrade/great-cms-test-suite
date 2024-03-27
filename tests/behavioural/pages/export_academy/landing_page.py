from selenium.webdriver.common.by import By

from tests.behavioural.pages.base import BasePage


class ExportAcademy(BasePage):
    """
    The Guidance and Support class for POM (Page Object Model) Behave structure.
    """

    def __init__(self, context):
        self.path = 'export-academy/'
        super().__init__(context, self.path)

    def signup_cta_visible(self):
        return self.is_visible((By.LINK_TEXT, 'Sign up to get started'))

    def visit_events_page(self):
        return self.do_click_link((By.LINK_TEXT, 'View all events'))

    def visit_sector_market_page(self):
        self.accept_domestic_cookies()
        return self.do_click_link((By.CSS_SELECTOR, "a[href*='type=sector'][href*='type=market']"))
