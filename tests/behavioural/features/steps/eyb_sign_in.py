from behave import given, then, when

from tests.behavioural.pages.expand_your_business.guide_page import GuidePage
from tests.behavioural.pages.expand_your_business.sign_in_page import SignInPage


@given('I am on the sign-in page')
def step_register_user(context):
    signin_page = SignInPage(context)
    signin_page.get_url()
    assert context.browser.current_url == signin_page.url


@when('I enter login credentials')
def step_login_credentials(context):
    signin_page = SignInPage(context)
    signin_page.enter_email_address(context.user_data['email_address'])
    signin_page.enter_password(context.user_data['password'])
    signin_page.press_signin_button()


@then('I am am taken to the EYB guide page')
def step_eyb_guide_page(context):
    guide_page = GuidePage(context)
    assert guide_page.url in context.browser.current_url


@given('I am signed in')
def step_login(context):
    context.execute_steps(
        """
            Given I am on the sign-in page
            When I enter login credentials
            Then I am am taken to the EYB guide page
        """
    )
