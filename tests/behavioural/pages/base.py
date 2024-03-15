from behave.runner import Context as behave_context
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By

from config.settings import ROOT
from tests.behavioural.utils.test_helpers import TestHelper


class BasePage(TestHelper):
    """
    The base page class for all pages under the POM (Page Object Model) Behave structure. All page classes should
    inherit from BasePage. All common functionality should be added here (e.g. accept cookies).

    POM (Page Object Model) reference: https://www.martinfowler.com/bliki/PageObject.html
    """

    def __init__(self, context: behave_context, path: str):
        self.root = ROOT
        self.path = path
        self.url = f'{self.root}{self.path}'
        super().__init__(context)

    def accept_cookies(self):
        """
        Accepts the cookie pop up banner (if present)
        :return: None
        """

        try:
            self.do_click_link((By.LINK_TEXT, 'Accept all cookies'))
        except NoSuchElementException:  # Cookie popup already accepted
            pass
        except TimeoutException:
            pass

    def get_url(self):
        """
        Retrieves the page URL in the browser
        :return: None
        """
        self.navigate(self.url)