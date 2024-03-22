from selenium.webdriver.common.by import By

from tests.behavioural.pages.base import BasePage
from tests.behavioural.utils.test_helpers import DESKTOP


class GuidePage(BasePage):
    def __init__(self, context):
        self.path = 'international/expand-your-business-in-the-uk/guide/'
        super().__init__(context, self.path)

    def checklist_for_uk_expansion_displayed(self):
        if self.get_device_type() == DESKTOP:
            return self.is_visible((By.ID, 'tab_step-by-step-guide'))
        else:
            return self.is_visible((By.LINK_TEXT, 'Checklist for UK expansion'))

    def click_personalised_guide_tab(self):
        if self.get_device_type() == DESKTOP:
            self.do_click((By.ID, 'tab_personalised-guide'))
        else:
            pass

    def personalised_guide_displayed(self):
        if self.get_device_type() == DESKTOP:
            return self.is_visible((By.ID, 'tab_personalised-guide'))
        else:
            return self.is_visible((By.LINK_TEXT, 'Personalised guide'))

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

    def articles_displayed(self):
        return (
            len(self.find_elements((By.XPATH, "//div[@id='personalised-guide']//div[@class='article-list-item']"))) > 0
        )

    def click_change_answers(self):
        self.do_click_link((By.LINK_TEXT, 'Change your answers'))
