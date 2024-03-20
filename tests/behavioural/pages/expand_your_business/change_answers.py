from selenium.webdriver.common.by import By

from tests.behavioural.pages.base import BasePage


class ChangeAnswersPage(BasePage):
    def __init__(self, context):
        self.path = 'international/expand-your-business-in-the-uk/change-your-answers/'
        super().__init__(context, self.path)

    def get_content_text(self):
        return self.find_element((By.ID, 'content')).text

    def click_change_sector(self):
        self.do_click_link((By.XPATH, "//dt[text()='Sector']/following-sibling::dd//a"))

    def click_change_intent(self):
        self.do_click_link((By.XPATH, "//dt[text()='Expansion plans']/following-sibling::dd//a"))

    def click_change_location(self):
        self.do_click_link((By.XPATH, "//dt[text()='Preferred location']/following-sibling::dd//a"))

    def click_change_hiring(self):
        self.do_click_link((By.XPATH, "//dt[contains(text(), 'hire (within first 3 years)')]/following-sibling::dd//a"))

    def click_change_planned_spend(self):
        self.do_click_link((By.XPATH, "//dt[text()='Planned spend for UK expansion']/following-sibling::dd//a"))
