from behave import then

from tests.behavioural.pages.expand_your_business.guide_page import GuidePage


@then('The guide page is displayed with limited information')
def step_guide_page_displayed(context):
    guide_page = GuidePage(context)
    # using in here as current_url contains a fragment id (#spend_container)
    assert guide_page.url in context.browser.current_url

    assert guide_page.checklist_for_uk_expansion_displayed() is True

    guide_page.click_personalised_guide_tab()
    assert guide_page.personalised_guide_displayed() is True
    assert guide_page.sign_up_banner_displayed() is True
