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
