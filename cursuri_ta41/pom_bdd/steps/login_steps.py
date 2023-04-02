from behave import *


@given('I am on the Login page')
def step_impl(context):
    context.login_page.navigate_to_login_page()


@when('I insert "{email}" in the email input')
def step_impl(context, email):
    context.login_page.set_email(email)


@when('I insert "{password}" in the password input')
def step_impl(context, password):
    context.login_page.set_password(password)


@when('I click on the login button')
def step_impl(context):
    context.login_page.click_login_button()


@then('The main error message is displayed')
def step_impl(context):
    assert context.login_page.is_main_error_message_displayed()


@then('The error text contains "{message}"')
def step_impl(context, message):
    context.login_page.assertIn(message, context.login_page.get_main_error_message_text(), "Error message invalid")