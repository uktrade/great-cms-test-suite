from selenium.webdriver.common.by import By

from tests.behavioural.pages.base import BasePage


class ExportAcademyEventsPage(BasePage):
    def __init__(self, context):
        self.path = 'export-academy/events/'
        super().__init__(context, self.path)

    def visit_an_event_detail_page(self):
        self.accept_domestic_cookies()
        return self.do_click_link(
            (
                By.XPATH,
                "//div[@class='govuk-grid-row event-list-card']//a[@class='govuk-link govuk-heading-s great-title-link']",  # noqa
            )
        )

    def is_event_detail_visible(self):
        return self.is_visible((By.XPATH, "//h2[text()='Description']"))

    def event_title(self):
        return self.get_tag_driver((By.TAG_NAME, 'title')).title
