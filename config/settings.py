import os

ROOT = os.getenv('ROOT', 'https://great.uat.uktrade.digital/')
USE_BROWSERSTACK = os.getenv('USE_BROWSERSTACK', False)
BROWSERSTACK_USERNAME = os.getenv('BROWSERSTACK_USERNAME', '')
BROWSERSTACK_ACCESS_KEY = os.getenv('BROWSERSTACK_ACCESS_KEY', '')
