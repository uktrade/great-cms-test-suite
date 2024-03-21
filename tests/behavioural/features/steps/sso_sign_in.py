from behave import given, then, when

from tests.behavioural.pages.sso.dashboard_page import DashboardPage
from tests.behavioural.pages.sso.sign_in_page import SignInPage


@given('I am on the login page')
def step_sign_in_user(context):
    sign_in_page = SignInPage(context)
    sign_in_page.get_url()
    assert context.browser.current_url == sign_in_page.url


@when('I enter sso login credentials')
def step_login_credentials(context):
    sign_in_page = SignInPage(context)
    sign_in_page.enter_email_address(context.user_data['email_address'])
    sign_in_page.enter_password(context.user_data['password'])
    sign_in_page.press_sign_in_button()


@then('I am taken to the user dashboard page')
def step_user_dashboard_page(context):
    dashboard_page = DashboardPage(context)
    assert dashboard_page.url in context.browser.current_url
