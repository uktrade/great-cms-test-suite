from selenium.webdriver.common.by import By

from tests.behavioural.pages.base import BasePage


class HomePage(BasePage):
    """
    The HomePage class for POM (Page Object Model) Behave structure.
    """

    def __init__(self, context):
        self.path = ''
        super().__init__(context, self.path)

    def click_export_support_for_uk_businesses_link(self):
        self.do_click_link((By.LINK_TEXT, 'Export support for UK businesses'))
