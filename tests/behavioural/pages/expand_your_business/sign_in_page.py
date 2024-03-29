from selenium.webdriver.common.by import By

from tests.behavioural.pages.base import BasePage


class SignInPage(BasePage):
    def __init__(self, context):
        self.path = 'international/expand-your-business-in-the-uk/login/'
        super().__init__(context, self.path)

    def press_signin_button(self):
        self.do_click_link((By.XPATH, "//button[text()='Sign in']"))

    def enter_email_address(self, email_address):
        self.do_send_keys((By.ID, 'id_email'), email_address)

    def enter_password(self, password):
        self.do_send_keys((By.ID, 'id_password'), password)
