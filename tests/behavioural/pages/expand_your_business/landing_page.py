from selenium.webdriver.common.by import By

from tests.behavioural.pages.base import BasePage


class ExpandYourBusiness(BasePage):
    """
    The Guidance and Support class for POM (Page Object Model) Behave structure.
    """

    def __init__(self, context):
        self.path = 'international/expand-your-business-in-the-uk/'
        super().__init__(context, self.path)

    # overriding as International cookie banner uses different wording
    def accept_cookies(self):
        self.do_click((By.ID, 'atlas-cookie-accept-all'))

    def start_triage(self):
        self.do_click_link((By.LINK_TEXT, 'Start now'))
