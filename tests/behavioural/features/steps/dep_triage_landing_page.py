from behave import given, then, when
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select, WebDriverWait

from tests.behavioural.page_object.pages.guide_and_support import GuidanceAndSupportPage
from tests.behavioural.page_object.pages.homepage import HomePage


@given('I am on the homepage')
def step_visit_homepage(context):
    homepage = HomePage(context)
    homepage.get_url()
    homepage.accept_cookies()

    assert homepage.context.browser.current_url == homepage.url


@when('I click on the "Guidance and Support" link in footer')
def step_click_link(context):
    homepage = HomePage(context)
    link = homepage.get_link('Guidance and support')
    link.click()
    # wait until page has been refreshed
    # todo (if we stick with selenium) lift this up to a base class e.g. via click methods below
    # https://github.com/uktrade/great-cms/blob/2e77269f1a5180c674e751bbbece0b2ca5e41606/tests/ui/utils/test_helpers.py#L41
    wait = WebDriverWait(context.browser, 10)
    wait.until(ec.url_changes(homepage.url))


@then('The DEP triage landing page is loaded')
def step_load_dep_triage_landing_page(context):
    guidance_and_support_page = GuidanceAndSupportPage(context)
    assert guidance_and_support_page.context.browser.current_url == guidance_and_support_page.url
