from behave import when

from tests.behavioural.pages.expand_your_business.hiring_form import HiringForm
from tests.behavioural.pages.expand_your_business.intent_form import IntentForm
from tests.behavioural.pages.expand_your_business.landing_page import ExpandYourBusiness
from tests.behavioural.pages.expand_your_business.location_form import LocationForm
from tests.behavioural.pages.expand_your_business.sector_form import SectorForm
from tests.behavioural.pages.expand_your_business.spend_form import SpendForm


@when('I start the triage')
def step_start_triage(context):
    landing_page = ExpandYourBusiness(context)
    landing_page.start_triage()
    sector_form_page = SectorForm(context)

    assert context.browser.current_url == sector_form_page.url


@when('I complete step 1 of the triage')
def step_triage_stage_1(context):
    sector_form_page = SectorForm(context)
    # error flow
    sector_form_page.submit()
    assert context.browser.current_url == sector_form_page.url
    assert sector_form_page.error_message_visible() is True

    # normal flow
    sector_form_page.enter_sector('mining')
    assert sector_form_page.sector_list_displayed_and_count_greater_than_zero() is True
    sector_form_page.choose_first_sector_displayed()
    sector_form_page.submit()


@when('I complete step 2 of the triage')
def step_triage_stage_2(context):
    intent_form_page = IntentForm(context)
    assert context.browser.current_url == intent_form_page.url
    assert intent_form_page.expansion_options_greater_than_zero() is True

    # error flow
    intent_form_page.submit()
    assert context.browser.current_url == intent_form_page.url
    assert intent_form_page.error_message_visible() is True

    # normal flow
    intent_form_page.choose_random_expansion_option()
    intent_form_page.submit()


@when('I complete step 3 of the triage')
def step_triage_stage_3(context):
    location_form_page = LocationForm(context)
    assert context.browser.current_url == location_form_page.url

    # error flow
    location_form_page.submit()
    assert context.browser.current_url == location_form_page.url
    assert location_form_page.error_message_visible() is True

    # normal flow
    location_form_page.enter_location('new')
    location_form_page.location_list_displayed_and_count_greater_than_zero() is True
    location_form_page.choose_first_location_displayed()
    location_form_page.submit()


@when('I complete step 4 of the triage')
def step_triage_stage_4(context):
    hiring_form_page = HiringForm(context)
    assert context.browser.current_url == hiring_form_page.url

    # error flow
    hiring_form_page.submit()
    assert context.browser.current_url == hiring_form_page.url
    assert hiring_form_page.error_message_visible() is True

    # normal flow
    assert hiring_form_page.hiring_options_greater_than_zero() is True
    hiring_form_page.choose_random_hiring_option()
    hiring_form_page.submit()


@when('I complete step 5 of the triage')
def step_triage_stage_5(context):
    spend_form_page = SpendForm(context)
    assert context.browser.current_url == spend_form_page.url

    # error flow
    spend_form_page.submit()
    assert context.browser.current_url == spend_form_page.url
    assert spend_form_page.error_message_visible() is True

    # normal flow
    assert spend_form_page.currency_selector_visible() is True
    spend_form_page.select_random_currency()
    assert spend_form_page.spend_options_greater_than_zero() is True
    spend_form_page.choose_random_spend_option()
    spend_form_page.submit()
