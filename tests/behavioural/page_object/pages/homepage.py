from selenium.webdriver.common.by import By

from tests.behavioural.page_object.pages.base import BasePage


class HomePage(BasePage):
    """
    The HomePage class for POM (Page Object Model) Behave structure.
    """

    def __init__(self, context):
        self.path = ''
        super().__init__(context, self.path)

    def click_guidance_and_support_link(self):
        self.do_click_link((By.LINK_TEXT, 'Guidance and support'))
