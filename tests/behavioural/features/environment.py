from selenium import webdriver


def before_scenario(context, scenario):
    for tag in scenario.tags:
        if tag == "Chrome":
            options = webdriver.ChromeOptions()
            options.add_argument('--headless')
            context.browser = webdriver.Chrome(options=options)
        elif tag == "Firefox":
            options = webdriver.FirefoxOptions()
            options.add_argument('--headless')
            context.browser = webdriver.Firefox(options=options)
        elif tag == "Ie":
            options = webdriver.IeOptions()
            options.add_argument('--headless')
            context.browser = webdriver.Ie(options=options)
        elif tag == "Edge":
            options = webdriver.EdgeOptions()
            options.add_argument('--headless')
            context.browser = webdriver.Edge(options=options)
        elif tag == "Safari":
            options = webdriver.SafariOptions()
            options.add_argument('--headless')
            context.browser = webdriver.Safari(options=options)


def after_scenario(context, scenario):
    context.browser.quit()
