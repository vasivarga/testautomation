from behave import *


@given('I am on the Login Page')
def step_impl(context):
    context.login_page.navigate_to_login_page()


@when('I insert an unregistered email in the email input')
def step_impl(context):
    context.login_page.set_unregistered_email()


@when('I insert "{email}" in the email input')
def step_impl(context, email):
    context.login_page.set_email(email)


@when('I insert a password in the password input')
def step_impl(context):
    context.login_page.set_wrong_password()


@when('I insert "{password}" in the password input')
def step_impl(context, password):
    context.login_page.set_password(password)


@when('I click on the login button')
def step_impl(context):
    context.login_page.click_login_button()


@then('The main error message is displayed')
def step_impl(context):
    assert context.login_page.is_main_error_message_displayed()


@then('The error text contains "No customer account found" message')
def step_impl(context):
    assert context.login_page.is_no_customer_account_found_message_displayed()


@then('The error text contains "{message}"')
def step_impl(context, message):
    assert message in context.login_page.get_main_error_message_text()


@then('Email error message is displayed')
def step_impl(context):
    assert context.login_page.is_email_error_message_displayed()


@then('Email error message text is "{message}"')
def step_impl(context, message):
    assert context.login_page.get_email_error_message_text() == message


@then('Login page URL is "{url}"')
def step_impl(context, url):
    assert context.login_page.is_url_correct(url)
