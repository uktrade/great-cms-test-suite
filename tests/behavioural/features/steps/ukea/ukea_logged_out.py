from behave import given, then, when

from tests.behavioural.pages.export_academy.landing_page import ExportAcademy
from tests.behavioural.pages.export_academy.sector_and_market_page import ExportAcademySectorAndMarketPage
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
    great_home_page = HomePage(context)
    great_home_page.click_join_the_uk_export_academy_card()

    ukea_landing_page = ExportAcademy(context)
    ukea_landing_page.get_url()
    assert context.browser.current_url == ukea_landing_page.url


@then('I should see UKEA landing page')
def step_ukea_landing_page_is_loaded_on_browser(context):
    ukea_landing_page = ExportAcademy(context)
    ukea_landing_page.get_url()
    assert context.browser.current_url == ukea_landing_page.url
    assert ukea_landing_page.signup_cta_visible() is True


@given(u'I am in UK Export Academy landing page')
def step_visit_ukea_landing_page(context):  # noqa
    context.execute_steps(
        """
        Given I am on the UKEA landing page
        """
    )


@when(u'I click sector & market card')
def step_click_sector_and_market_card(context):
    ukea_landing_page = ExportAcademy(context)
    ukea_landing_page.visit_sector_market_page()

    ukea_sector_and_market_page = ExportAcademySectorAndMarketPage(context)
    ukea_sector_and_market_page.get_url()
    assert context.browser.current_url == ukea_sector_and_market_page.url


@then(u'I should be in "UK Export Academy Events" page with both sector and master filters on')
def step_sector_and_market_checkboxes_selected(context):
    ukea_sector_and_market_page = ExportAcademySectorAndMarketPage(context)
    ukea_sector_and_market_page.get_url()

    assert ukea_sector_and_market_page.is_sector_check_box_selected() is True
    assert ukea_sector_and_market_page.is_market_check_box_selected() is True
