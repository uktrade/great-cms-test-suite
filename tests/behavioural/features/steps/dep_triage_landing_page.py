from behave import given, then, when

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
    link = homepage.get_link('gain access to a trusted network')
    link.click()


@then('The DEP triage landing page is loaded')
def step_load_dep_triage_landing_page(context):
    guidance_and_support_page = GuidanceAndSupportPage(context)

    assert guidance_and_support_page.context.browser.current_url == guidance_and_support_page.url
