from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from config.settings import ROOT


class BasePage:
    """
    The base page class for all pages under the POM (Page Object Model) Behave structure. All page classes should
    inherit from BasePage. All common functionality should be added here (e.g. accept cookies).

    POM (Page Object Model) reference: https://www.martinfowler.com/bliki/PageObject.html
    """

    def __init__(self, context, path):
        self.root = ROOT
        self.path = path
        self.url = f'{self.root}{self.path}'
        self.context = context

    def accept_cookies(self):
        """
        Accepts the cookie pop up banner (if present)
        :return: None
        """

        try:
            link = self.context.browser.find_element(By.LINK_TEXT, 'Accept all cookies')
            link.click()
        except NoSuchElementException:  # Cookie popup already accepted
            pass

    def get_url(self):
        """
        Retrieves the page URL in the browser
        :return: None
        """

        self.context.browser.get(self.url)

    def get_link(self, link_text):
        """
        Retrieve a link from the page based off the link text
        :return: Link object
        """

        link = self.context.browser.find_element(By.LINK_TEXT, link_text)

        return link
