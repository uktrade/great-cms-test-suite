from behave import given, then, when

from tests.behavioural.pages.sso.confirmation_code_page import ConfirmationCodePage
from tests.behavioural.pages.sso.confirmation_page import ConfirmationPage
from tests.behavioural.pages.sso.dashboard_page import DashboardPage
from tests.behavioural.pages.sso.sign_up_page import SignUpPage


@given('I am on the sign up page')
def step_sign_up_user(context):
    sign_up_page = SignUpPage(context)
    sign_up_page.get_url()
    assert context.browser.current_url == sign_up_page.url


@when('I enter email and password')
def step_sign_up_credentials(context):
    sign_in_page = SignUpPage(context)
    sign_in_page.enter_email_address(context.user_data['email_address'])
    sign_in_page.enter_password(context.user_data['password'])
    sign_in_page.press_sign_up_button()


@when('I enter my new confirmation code')
def step_confirmation_code(context):
    signup_page = SignUpPage(context)
    assert signup_page.url in context.browser.current_url
    confirmation_code_page = ConfirmationCodePage(context)
    confirmation_code_page.enter_confirmation_code()
    confirmation_code_page.press_continue()


@when('I click continue on the confirmation page')
def step_success_continue(context):
    signup_page = SignUpPage(context)
    assert signup_page.url in context.browser.current_url
    confirmation_page = ConfirmationPage(context)
    confirmation_page.press_continue()


@then('I am taken to the dashboard page for the new user')
def step_user_dashboard_page(context):
    dashboard_page = DashboardPage(context)
    assert dashboard_page.url in context.browser.current_url
