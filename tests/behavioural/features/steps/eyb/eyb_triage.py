from random import choice

from behave import when

from tests.behavioural.pages.expand_your_business.hiring_form import HiringForm
from tests.behavioural.pages.expand_your_business.intent_form import IntentForm
from tests.behavioural.pages.expand_your_business.landing_page import ExpandYourBusiness
from tests.behavioural.pages.expand_your_business.location_form import LocationForm
from tests.behavioural.pages.expand_your_business.sector_form import SectorForm
from tests.behavioural.pages.expand_your_business.spend_form import SpendForm


@when('I complete the triage')
def step_complete_triage(context):
    context.execute_steps(
        """
            When I start the triage
            And I complete step 1 of the triage
            And I complete step 2 of the triage
            And I complete step 3 of the triage
            And I complete step 4 of the triage
            And I complete step 5 of the triage
        """
    )


@when('I start the triage')
def step_start_triage(context):
    landing_page = ExpandYourBusiness(context)
    landing_page.get_url()
    landing_page.start_triage()
    sector_form_page = SectorForm(context)

    assert context.browser.current_url == sector_form_page.url


@when('I complete step 1 of the triage')
def step_triage_stage_1(context):
    sector_form_page = SectorForm(context)
    sector_form_page.clear_sector_entry()
    assert sector_form_page.url in context.browser.current_url

    # normal flow
    eg_sector_choices = ['mining', 'food', 'farming', 'vehicles']
    sector_form_page.enter_sector(choice(eg_sector_choices))
    assert sector_form_page.sector_list_displayed_and_count_greater_than_zero() is True
    chosen_sector = sector_form_page.choose_first_sector_displayed()
    # splitting because get text on iOS contains an additional string with the number of occurrences
    chosen_sector = ''.join(chosen_sector.split('\n')[0:1]).replace('\n', ', ')
    context.user_data['triage_sector'] = chosen_sector
    sector_form_page.submit()


@when('I complete step 2 of the triage')
def step_triage_stage_2(context):
    intent_form_page = IntentForm(context)
    intent_form_page.clear_expansion_selection()
    assert intent_form_page.url in context.browser.current_url
    assert intent_form_page.expansion_options_greater_than_zero() is True

    # normal flow
    chosen_intent = intent_form_page.choose_random_expansion_option()
    context.user_data['triage_intent'] = chosen_intent
    intent_form_page.submit()


@when('I complete step 3 of the triage')
def step_triage_stage_3(context):
    location_form_page = LocationForm(context)
    location_form_page.clear_location_text()
    assert location_form_page.url in context.browser.current_url

    # normal flow
    eg_location_choices = ['new', 'edi', 'bel', 'card', 'lon']
    location_form_page.enter_location(choice(eg_location_choices))
    location_form_page.location_list_displayed_and_count_greater_than_zero() is True
    chosen_location = location_form_page.choose_first_location_displayed()
    # splitting because get text on iOS contains an additional string with the number of occurrences
    context.user_data['triage_location'] = chosen_location.split('\n')[0]
    location_form_page.submit()


@when('I complete step 4 of the triage')
def step_triage_stage_4(context):
    hiring_form_page = HiringForm(context)
    assert hiring_form_page.url in context.browser.current_url

    # normal flow
    assert hiring_form_page.hiring_options_greater_than_zero() is True
    chosen_hiring = hiring_form_page.choose_random_hiring_option()
    context.user_data['triage_hiring'] = chosen_hiring
    hiring_form_page.submit()


@when('I complete step 5 of the triage')
def step_triage_stage_5(context):
    spend_form_page = SpendForm(context)
    assert spend_form_page.url in context.browser.current_url

    # normal flow
    assert spend_form_page.currency_selector_visible() is True
    # todo, uncomment select random currency when summary page has been fixed
    # spend_form_page.select_random_currency()
    assert spend_form_page.spend_options_greater_than_zero() is True
    chosen_spend = spend_form_page.choose_random_spend_option()
    context.user_data['triage_spend'] = chosen_spend
    spend_form_page.submit()
