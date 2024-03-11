from behave import given, then, when

from tests.behavioural.pages.expand_your_business.guide_page import GuidePage
from tests.behavioural.pages.expand_your_business.landing_page import ExpandYourBusiness


@given('I am on the EYB landing page')
def step_visit_eyb_landing_page(context):
    landing_page = ExpandYourBusiness(context)
    landing_page.get_url()
    landing_page.accept_cookies()

    assert context.browser.current_url == landing_page.url


@when("I complete the triage")
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


@then("The guide page is displayed with limited information")
def step_guide_page_displayed(context):
    guide_page = GuidePage(context)
    # using in here as current_url contains a fragment id (#spend_container)
    assert guide_page.url in context.browser.current_url

    assert guide_page.checklist_for_uk_expansion_displayed() is True

    guide_page.click_personalised_guide_tab()
    assert guide_page.personalised_guide_displayed() is True
    assert guide_page.sign_up_banner_displayed() is True
