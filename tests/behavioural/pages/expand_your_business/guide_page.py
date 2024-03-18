from selenium.webdriver.common.by import By

from tests.behavioural.pages.base import BasePage


class GuidePage(BasePage):
    def __init__(self, context):
        self.path = 'international/expand-your-business-in-the-uk/guide/'
        super().__init__(context, self.path)

    def checklist_for_uk_expansion_displayed(self):
        return self.is_visible((By.ID, 'tab_step-by-step-guide'))

    def click_personalised_guide_tab(self):
        self.do_click((By.ID, 'tab_personalised-guide'))

    def personalised_guide_displayed(self):
        return self.is_visible((By.ID, 'tab_personalised-guide'))

    def sign_up_banner_displayed(self):
        return self.is_visible((By.ID, 'sign-up-banner'))

    def sign_up_success_banner_displayed(self):
        return self.is_visible(
            (By.CSS_SELECTOR, "div[class='govuk-notification-banner govuk-notification-banner--success']")
        )

    def entered_information_displayed(self):
        content = self.find_element((By.ID, 'content')).text
        return (
            self.context.user_data['company_name'] in content
            and self.context.user_data['company_headquarters'] in content
        )
