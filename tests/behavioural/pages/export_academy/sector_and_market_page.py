from selenium.webdriver.common.by import By

from tests.behavioural.pages.base import BasePage


class ExportAcademySectorAndMarketPage(BasePage):
    def __init__(self, context):
        self.path = 'export-academy/events/?type=sector&type=market'
        super().__init__(context, self.path)

    def is_sector_check_box_selected(self):
        sector_checkbox = self.get_tag_driver((By.CSS_SELECTOR, "input[value='sector']"))
        return sector_checkbox.is_selected()

    def is_market_check_box_selected(self):
        market_checkbox = self.get_tag_driver((By.CSS_SELECTOR, "input[value='market']"))
        return market_checkbox.is_selected()
