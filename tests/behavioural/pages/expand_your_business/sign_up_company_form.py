from random import choice

from selenium.webdriver.common.by import By

from tests.behavioural.pages.base import BasePage


class SignUpCompanyForm(BasePage):
    def __init__(self, context):
        self.path = 'international/expand-your-business-in-the-uk/profile/?signup=true'
        super().__init__(context, self.path)

    def submit(self):
        self.do_click_link((By.XPATH, "//button[text()='Submit']"))

    def enter_company_name(self, company_name):
        self.do_send_keys((By.ID, 'id_company_name'), company_name)

    def enter_company_headquarters(self, company_headquarters):
        self.do_send_keys((By.ID, 'js-company-location-select'), company_headquarters)

    def choose_first_headquarters(self):
        location = self.find_element((By.ID, 'js-company-location-select__option--0'))
        location.click()
        return location.text

    def enter_full_name(self, full_name):
        self.do_send_keys((By.ID, 'id_full_name'), full_name)

    def enter_role(self, role):
        self.do_send_keys((By.ID, 'id_role'), role)

    def enter_company_website(self, company_website):
        self.do_send_keys((By.ID, 'id_company_website'), company_website)

    def enter_telephone_number(self, telephone_number):
        self.do_send_keys((By.ID, 'id_telephone_number'), telephone_number)

    def chose_random_landing_timeline(self):
        self.do_click((By.ID, 'id_landing_timeframe'))
        # first option is blank hence string length check
        landing_choices = self.find_elements(
            (By.XPATH, "//select[@id='id_landing_timeframe']//option[string-length(text())>0]")
        )
        landing_time = choice(landing_choices)
        landing_time.click()
        return landing_time.text
