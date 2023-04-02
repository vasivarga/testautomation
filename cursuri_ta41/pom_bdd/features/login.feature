Feature: Test the functionality of the Login Page

 Scenario: Check that an error message is displayed when the user tries to log in with an unregistered email
   Given I am on the Login page
   When I insert "wrong_email@host.com" in the email input
   When I insert "somepass" in the password input
   When I click on the login button
   Then The main error message is displayed
   Then The error text contains "No customer account found"
