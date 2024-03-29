from typing import Tuple

from behave.runner import Context as BehaveContext
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select, WebDriverWait

"""Parent for all pages"""
"""Contains generic methods for ALL pages"""


DESKTOP = 1
MOBILE_DEVICE = 2


class TestHelper:
    def __init__(self, context: BehaveContext):
        self.context = context
        self.driver = context.browser
        self._wait = WebDriverWait(self.driver, 20)
        self.driver.maximize_window()
        self.device_type = self.get_device_type()

    def get_device_type(self):
        # breakpoint from great/cms/core->sass->learn->_base.scss->$mobile
        mobile_breakpoint = 640
        window_size = self.driver.get_window_size()

        if window_size['width'] <= mobile_breakpoint:
            return MOBILE_DEVICE

        return DESKTOP

    def navigate(self, url):
        self.driver.get(url)
        self._wait.until(ec.url_to_be(url))

    def do_click(self, locator: Tuple[str, str]):
        self._wait.until(ec.visibility_of_element_located(locator)).click()

    def do_click_link(self, locator: Tuple[str, str]):
        """Modifcation to do_click method that waits for the page to reload (i.e. stale element)"""
        element = self._wait.until(ec.visibility_of_element_located(locator))
        element.click()
        self.wait_for_refresh(element)

    def do_send_keys(self, locator: Tuple[str, str], input_text):
        self._wait.until(ec.visibility_of_element_located(locator)).send_keys(input_text)

    def is_visible(self, locator: Tuple[str, str]):
        element = self._wait.until(ec.visibility_of_element_located(locator))
        return bool(element)

    def get_element_text(self, locator: Tuple[str, str]):
        element = self._wait.until(ec.visibility_of_element_located(locator))
        return element.text

    def find_element(self, locator: Tuple[str, str]):
        self._wait.until(ec.visibility_of_element_located(locator))
        element = self.driver.find_element(locator[0], locator[1])
        return element

    def find_elements(self, locator: Tuple[str, str]):
        elements = self.driver.find_elements(locator[0], locator[1])
        return elements

    def do_select(self, locator: Tuple[str, str], option):
        select_element = self._wait.until(ec.visibility_of_element_located(locator))
        select = Select(select_element)
        select.select_by_visible_text(option)

    def get_selected_option(self, locator: Tuple[str, str]):
        select_element = self._wait.until(ec.visibility_of_element_located(locator))
        select = Select(select_element)
        return select.all_selected_options[0].text

    def get_tag_driver(self, locator: Tuple[str, str]):
        return self._wait.until(ec.presence_of_element_located(locator))

    def wait_for_url(self, url):
        return self._wait.until(ec.url_to_be(url))

    def wait_for_refresh(self, element):
        return self._wait.until(ec.staleness_of(element))

    def wait_for_url_change(self, url):
        return self._wait.until(ec.url_changes(url))
