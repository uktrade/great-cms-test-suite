from behave import given, then, when

from tests.behavioural.pages.expand_your_business.confirmation_code_page import ConfirmationCodePage
from tests.behavioural.pages.expand_your_business.guide_page import GuidePage
from tests.behavioural.pages.expand_your_business.sign_up_company_form import SignUpCompanyForm
from tests.behavioural.pages.expand_your_business.sign_up_page import SignUpPage


@given('I am on the sign-up page')
def step_register_user(context):
    signup_page = SignUpPage(context)
    signup_page.get_url()
    assert context.browser.current_url == signup_page.url


@when('I enter login credentials')
def step_login_credentials(context):
    signup_page = SignUpPage(context)
    signup_page.enter_email_address(context.user_data['email_address'])
    signup_page.enter_password(context.user_data['password'])
    signup_page.press_signup_button()


@when('I enter a confirmation code')
def step_confirmation_code(context):
    signup_page = SignUpPage(context)
    assert signup_page.url in context.browser.current_url
    confirmation_code_page = ConfirmationCodePage(context)
    confirmation_code_page.enter_confirmation_code()
    confirmation_code_page.press_continue()


@when('I complete company details')
def step_add_company_details(context):
    signup_company_form = SignUpCompanyForm(context)
    assert context.browser.current_url == signup_company_form.url
    signup_company_form.enter_company_name(context.user_data['company_name'])
    signup_company_form.enter_company_headquarters(context.user_data['partial_company_headquarters_location'])
    context.user_data['company_headquarters'] = signup_company_form.choose_first_headquarters()
    signup_company_form.enter_full_name(context.user_data['user_full_name'])
    signup_company_form.enter_role(context.user_data['user_role'])
    signup_company_form.enter_company_website(context.user_data['company_website'])
    signup_company_form.enter_telephone_number(context.user_data['telephone_number'])
    context.user_data['landing_time'] = signup_company_form.chose_random_landing_timeline()
    signup_company_form.submit()


@then('I am am taken to the EYB guide page')
def step_eyb_guide_page(context):
    guide_page = GuidePage(context)
    assert guide_page.url in context.browser.current_url
    assert guide_page.sign_up_success_banner_displayed() is True
    assert guide_page.entered_information_displayed() is True
