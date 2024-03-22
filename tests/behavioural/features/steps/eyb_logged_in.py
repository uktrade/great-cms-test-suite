from behave import given, then, when

from tests.behavioural.pages.expand_your_business.change_answers import ChangeAnswersPage
from tests.behavioural.pages.expand_your_business.guide_page import GuidePage
from tests.behavioural.pages.expand_your_business.landing_page import ExpandYourBusiness


@given('I am on the EYB landing page')
def step_visit_eyb_landing_page(context):
    landing_page = ExpandYourBusiness(context)
    landing_page.get_url()
    landing_page.accept_international_cookies()

    assert context.browser.current_url == landing_page.url


@when('I am signed in')
def step_verify_signed_in(context):
    context.execute_steps(
        """
            Given I am on the sign-in page
            When I enter login credentials
        """
    )

    landing_page = ExpandYourBusiness(context)
    assert landing_page.signed_in() is True


@then('The guide page is displayed')
def step_guide_page_displayed(context):
    guide_page = GuidePage(context)
    # using in here as current_url contains a fragment id (#spend_container)
    assert guide_page.url in context.browser.current_url

    assert guide_page.checklist_for_uk_expansion_displayed() is True

    guide_page.click_personalised_guide_tab()
    assert guide_page.personalised_guide_displayed() is True
    assert guide_page.articles_displayed() is True


@when('I navigate to the EYB guide page')
def step_navigate_to_guide_page(context):
    guide_page = GuidePage(context)
    guide_page.get_url()
    assert guide_page.url in context.browser.current_url


@when('I click change your answers')
def step_click_change_answers(context):
    guide_page = GuidePage(context)
    guide_page.click_change_answers()


@then('the data presented matches previously entered data')
def step_change_answers_summary_page(context):
    change_answers_page = ChangeAnswersPage(context)
    content = change_answers_page.get_content_text()

    triage_keys = ['triage_sector', 'triage_intent', 'triage_location', 'triage_hiring', 'triage_spend']

    for key in triage_keys:
        assert context.user_data[key] in content
