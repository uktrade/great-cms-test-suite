from behave import use_fixture
from selenium import webdriver

from config.settings import BROWSERSTACK_ACCESS_KEY, BROWSERSTACK_USERNAME, USE_BROWSERSTACK
from tests.behavioural.fixtures import eyb_random_data, great_random_data

# browserstack code slightly modified from
# from https://github.com/browserstack/behave-browserstack/blob/master/features/environment.py


def before_feature(context, feature):
    for tag in feature.tags:
        if tag == 'eyb_random_data':
            use_fixture(eyb_random_data, context)
        if tag == 'great_random_data':
            use_fixture(great_random_data, context)


def before_scenario(context, scenario):  # noqa: C901
    if USE_BROWSERSTACK:
        context.browser = webdriver.Remote(
            command_executor=f'https://{BROWSERSTACK_USERNAME}:{BROWSERSTACK_ACCESS_KEY}@hub.browserstack.com/wd/hub'
        )
    else:
        for tag in scenario.tags:
            if tag == 'Chrome':
                options = webdriver.ChromeOptions()
                options.add_argument('--headless')
                context.browser = webdriver.Chrome(options=options)
            elif tag == 'Firefox':
                options = webdriver.FirefoxOptions()
                options.add_argument('--headless')
                context.browser = webdriver.Firefox(options=options)
            elif tag == 'Ie':
                options = webdriver.IeOptions()
                options.add_argument('--headless')
                context.browser = webdriver.Ie(options=options)
            elif tag == 'Edge':
                options = webdriver.EdgeOptions()
                options.add_argument('--headless')
                context.browser = webdriver.Edge(options=options)
            elif tag == 'Safari':
                options = webdriver.SafariOptions()
                options.add_argument('--headless')
                context.browser = webdriver.Safari(options=options)


def after_scenario(context, feature):
    if USE_BROWSERSTACK:
        if context.failed is True:
            context.browser.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "At least 1 assertion failed"}}'  # noqa: E501
            )
        if context.failed is not True:
            context.browser.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "All assertions passed"}}'  # noqa: E501
            )
    context.browser.quit()
