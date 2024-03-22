from selenium.webdriver.common.by import By

from tests.behavioural.pages.base import BasePage
from tests.behavioural.utils.utils import retrieve_regex_from_mailhog_email


class ConfirmationCodePage(BasePage):
    def __init__(self, context):
        self.path = 'signup/'
        super().__init__(context, self.path)

    def get_confirmation_code(self):
        payload = {'kind': 'to', 'query': self.context.user_data['email_address']}
        regex = r'Your confirmation code is\s*(\d{5})'
        return retrieve_regex_from_mailhog_email(payload, regex)[1]

    def enter_confirmation_code(self):
        self.do_send_keys((By.ID, 'code'), self.get_confirmation_code())

    def press_continue(self):
        self.do_click_link((By.XPATH, "//button[text()='Submit']"))
