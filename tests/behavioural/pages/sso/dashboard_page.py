from selenium.webdriver.common.by import By

from tests.behavioural.pages.base import BasePage


class DashboardPage(BasePage):
    def __init__(self, context):
        self.path = 'dashboard/'
        super().__init__(context, self.path)

    def press_menu_button(self):
        self.do_click_link((By.CSS_SELECTOR, "div[class='great-header-menu-button']"))

    def press_sign_out_button(self):
        self.do_click_link((By.XPATH, "//button[text()='Sign out']"))
