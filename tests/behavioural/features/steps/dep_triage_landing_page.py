from behave import given, then, when

from tests.behavioural.pages.guide_and_support import GuidanceAndSupportPage
from tests.behavioural.pages.homepage import HomePage


@given('I am on the homepage')
def step_visit_homepage(context):
    homepage = HomePage(context)
    homepage.get_url()
    homepage.accept_domestic_cookies()

    assert context.browser.current_url == homepage.url


@when('I click on the "Export support for UK businesses" link in footer')
def step_click_link(context):
    homepage = HomePage(context)
    homepage.click_export_support_for_uk_businesses_link()


@then('The DEP triage landing page is loaded')
def step_load_dep_triage_landing_page(context):
    guidance_and_support_page = GuidanceAndSupportPage(context)
    assert context.browser.current_url == guidance_and_support_page.url
