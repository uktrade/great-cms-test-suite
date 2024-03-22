from behave import when

from tests.behavioural.pages.homepage import HomePage
from tests.behavioural.pages.sso.sign_in_page import SignInPage


@when('I click the homepage sign in link')
def step_navigate_to_sign_in(context):
    homepage = HomePage(context)
    homepage.press_sign_in_link()


@when('I enter sso login credentials')
def step_login_credentials(context):
    sign_in_page = SignInPage(context)
    sign_in_page.enter_email_address(context.user_data['email_address'])
    sign_in_page.enter_password(context.user_data['password'])
    sign_in_page.press_sign_in_button()
