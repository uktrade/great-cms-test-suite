from selenium.webdriver.common.by import By

from tests.behavioural.pages.base import BasePage


class ChangeAnswersPage(BasePage):
    def __init__(self, context):
        self.path = 'international/expand-your-business-in-the-uk/change-your-answers/'
        super().__init__(context, self.path)

    def get_content_text(self):
        return self.find_element((By.ID, 'content')).text
