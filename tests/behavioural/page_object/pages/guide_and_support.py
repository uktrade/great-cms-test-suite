from selenium.webdriver.common.by import By

from tests.behavioural.page_object.pages.base import BasePage


class GuidanceAndSupportPage(BasePage):
    """
    The Guidance and Support class for POM (Page Object Model) Behave structure.
    """

    def __init__(self, context):
        self.path = "support/guidance-and-support/"
        super().__init__(context, self.path)