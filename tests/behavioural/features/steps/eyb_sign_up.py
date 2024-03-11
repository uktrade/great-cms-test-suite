from uuid import uuid4

from behave import given, when

from tests.behavioural.pages.expand_your_business.sign_up_page import SignUpPage


@given('I am on the sign-up page')
def step_visit_sign_up_page(context):
    signup_page = SignUpPage(context)
    signup_page.get_url()
    assert context.browser.current_url == SignUpPage.url


@when('I complete the sign-up form')
def step_complete_signup(context):
    signup_page = SignUpPage(context)
    context['user_data'] = {'email_address': f"automated-ui-test+{uuid4()}@uitest.com", 'password': f"A1!{uuid4()}"}
    signup_page.enter_email_address(context.user_data.email_address)
    signup_page.enter_password(context.user_data.password)
    import time

    time.sleep(15)
