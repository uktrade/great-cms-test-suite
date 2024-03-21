from behave import given, then, when

from tests.behavioural.pages.homepage import HomePage
from tests.behavioural.pages.sso.dashboard_page import DashboardPage
from tests.behavioural.pages.sso.sign_in_page import SignInPage


@given('I am on the great homepage')
def step_start_on_great(context):
    homepage = HomePage(context)
    homepage.get_url()
    homepage.accept_domestic_cookies()
    assert context.browser.current_url == homepage.url


@when('I click the sign in link')
def step_navigate_to_sign_in(context):
    homepage = HomePage(context)
    homepage.click_sign_in_link()


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
