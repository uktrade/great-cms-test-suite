# from selenium import webdriver


# def before_scenario(context, scenario):
#     for tag in scenario.tags:
#         if tag == 'Chrome':
#             options = webdriver.ChromeOptions()
#             options.add_argument('--headless')
#             context.browser = webdriver.Chrome(options=options)
#         elif tag == 'Firefox':
#             options = webdriver.FirefoxOptions()
#             options.add_argument('--headless')
#             context.browser = webdriver.Firefox(options=options)
#         elif tag == 'Ie':
#             options = webdriver.IeOptions()
#             options.add_argument('--headless')
#             context.browser = webdriver.Ie(options=options)
#         elif tag == 'Edge':
#             options = webdriver.EdgeOptions()
#             options.add_argument('--headless')
#             context.browser = webdriver.Edge(options=options)
#         elif tag == 'Safari':
#             options = webdriver.SafariOptions()
#             options.add_argument('--headless')
#             context.browser = webdriver.Safari(options=options)


# def after_scenario(context, scenario):
#     context.browser.quit()

import os

import yaml
from browserstack.local import Local

# from https://github.com/browserstack/behave-browserstack/blob/master/features/environment.py and slightly modified
from selenium import webdriver

CONFIG_FILE = os.environ['CONFIG_FILE'] if 'CONFIG_FILE' in os.environ else 'browserstack.yml'
TASK_ID = int(os.environ['TASK_ID']) if 'TASK_ID' in os.environ else 0

with open(CONFIG_FILE) as data_file:
    CONFIG = yaml.safe_load(data_file)

bs_local = None

BROWSERSTACK_USERNAME = os.environ['BROWSERSTACK_USERNAME'] if 'BROWSERSTACK_USERNAME' in os.environ else CONFIG['user']
BROWSERSTACK_ACCESS_KEY = (
    os.environ['BROWSERSTACK_ACCESS_KEY'] if 'BROWSERSTACK_ACCESS_KEY' in os.environ else CONFIG['key']
)


def start_local():
    """Code to start browserstack local before start of test."""
    global bs_local
    bs_local = Local()
    bs_local_args = {"key": BROWSERSTACK_ACCESS_KEY, "forcelocal": "true"}
    bs_local.start(**bs_local_args)


def stop_local():
    """Code to stop browserstack local after end of test."""
    global bs_local
    if bs_local is not None:
        bs_local.stop()


def before_scenario(context, scenario):
    # desired_capabilities = CONFIG['environments'][TASK_ID]
    # for key in CONFIG["capabilities"]:
    #     if key not in desired_capabilities:
    #         desired_capabilities[key] = CONFIG["capabilities"][key]
    #     elif key == "bstack:options":
    #         desired_capabilities[key].update(CONFIG["capabilities"][key])
    # desired_capabilities['bstack:options']['source'] = 'behave:sample-master:v1.2'

    # if "bstack:options" in desired_capabilities and "local" in desired_capabilities["bstack:options"] and desired_capabilities["bstack:options"]["local"]:
    # start_local()

    context.browser = webdriver.Remote(
        # desired_capabilities=desired_capabilities,
        command_executor="https://%s:%s@hub.browserstack.com/wd/hub"
        % (BROWSERSTACK_USERNAME, BROWSERSTACK_ACCESS_KEY)
    )
    # import pdb; pdb.set_trace()


def after_scenario(context, scenario):
    # import pdb; pdb.set_trace()
    if context.failed is True:
        context.browser.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "At least 1 assertion failed"}}'
        )
    if context.failed is not True:
        context.browser.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "All assertions passed"}}'
        )
    context.browser.quit()
    # stop_local()
