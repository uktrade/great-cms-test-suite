from tests.behavioural.pages.base import BasePage


class GuidanceAndSupportPage(BasePage):
    """
    The Guidance and Support class for POM (Page Object Model) Behave structure.
    """

    def __init__(self, context):
        self.path = 'support/export-support/'
        super().__init__(context, self.path)
