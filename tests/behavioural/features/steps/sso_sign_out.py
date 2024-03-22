from behave import given, then, when

from tests.behavioural.pages.homepage import HomePage
from tests.behavioural.pages.sso.dashboard_page import DashboardPage


@given('I am on the main homepage')
def step_start_on_great(context):
    homepage = HomePage(context)
    homepage.get_url()
    homepage.accept_domestic_cookies()
    assert context.browser.current_url == homepage.url


@given('I complete the authentication steps')
def step_sign_in(context):
    context.execute_steps(
        """
            When I click the homepage sign in link
            And I enter sso login credentials
        """
    )


@when('I am taken to the dashboard page')
def step_user_dashboard_page(context):
    dashboard_page = DashboardPage(context)
    assert dashboard_page.url in context.browser.current_url


@when('I click the sign out button')
def step_user_sign_out(context):
    dashboard_page = DashboardPage(context)
    dashboard_page.press_menu_link()
    dashboard_page.press_sign_out_link()


@then('I am taken back to great.gov.uk')
def step_user_home_page(context):
    homepage = HomePage(context)
    homepage.get_url()
    assert context.browser.current_url == homepage.url
