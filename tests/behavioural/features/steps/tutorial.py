from behave import given, when, then


@given('we have behave installed')
def step_install(context):
    pass


@when('we implement a test')
def step_implement_test(context):
    assert True is not False


@then('behave will test it for us!')
def step_test(context):
    assert context.failed is False
