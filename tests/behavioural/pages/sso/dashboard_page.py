from tests.behavioural.pages.base import BasePage


class DashboardPage(BasePage):
    def __init__(self, context):
        self.path = 'dashboard/'
        super().__init__(context, self.path)
