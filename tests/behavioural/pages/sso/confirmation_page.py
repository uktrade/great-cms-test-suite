from selenium.webdriver.common.by import By

from tests.behavioural.pages.base import BasePage


class ConfirmationPage(BasePage):
    def __init__(self, context):
        self.path = 'signup/'
        super().__init__(context, self.path)

    def press_continue(self):
        self.do_click_link((By.ID, 'signup-modal-submit-success'))
