from behave import given, then

from tests.behavioural.pages.export_academy.landing_page import ExportAcademy


@given('I am on the UKEA landing page')
def step_visit_ukea_landing_page(context):
    landing_page = ExportAcademy(context)
    landing_page.get_url()

    assert context.browser.current_url == landing_page.url


@then('I should see a sign up cta')
def step_ukea_logged_out_landing_page_displayed(context):
    landing_page = ExportAcademy(context)

    assert landing_page.signup_cta_visible() is True
