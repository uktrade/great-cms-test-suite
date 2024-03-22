from behave import given, then, when

from tests.behavioural.pages.homepage import HomePage
from tests.behavioural.pages.sso.dashboard_page import DashboardPage


@given('I am on the great homepage')
def step_start_on_great(context):
    homepage = HomePage(context)
    homepage.get_url()
    homepage.accept_domestic_cookies()
    assert context.browser.current_url == homepage.url


@when('I complete the sign in steps')
def step_sign_in(context):
    context.execute_steps(
        """
            When I click the homepage sign in link
            And I enter sso login credentials
        """
    )


@then('I am taken to the user dashboard page')
def step_user_dashboard_page(context):
    dashboard_page = DashboardPage(context)
    assert dashboard_page.url in context.browser.current_url
