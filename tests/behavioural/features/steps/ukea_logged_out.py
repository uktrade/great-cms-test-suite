from behave import given, then, when

from tests.behavioural.pages.export_academy.landing_page import ExportAcademy
from tests.behavioural.pages.homepage import HomePage


@given('I am on the UKEA landing page')
def step_visit_ukea_landing_page(context):
    landing_page = ExportAcademy(context)
    landing_page.get_url()

    assert context.browser.current_url == landing_page.url


@then('I should see a sign up cta')
def step_ukea_logged_out_landing_page_displayed(context):
    landing_page = ExportAcademy(context)

    assert landing_page.signup_cta_visible() is True


@given('I am on Great home page')
def step_visit_ukea_landing_page_from_great_home_page(context):
    context.great_home_page = HomePage(context)
    context.great_home_page.get_url()
    assert context.browser.current_url == context.great_home_page.url


@when('I click “Join the UK export academy” card')
def step_click_card_to_join_ukea(context):
    context.great_home_page.click_join_the_uk_export_academy_card()


@then('I should see UKEA landing page')
def step_ukea_landing_page_is_loaded_on_browser(context):
    ukea_landing_page = ExportAcademy(context)
    ukea_landing_page.get_url()
    assert context.browser.current_url == ukea_landing_page.url
    assert ukea_landing_page.signup_cta_visible() is True
