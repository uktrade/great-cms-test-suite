@great_random_data
Feature: Single Sign On
  As a user
  I want to be able to engage with Great service offering

  @Chrome
  Scenario: User can sign up to the Great services
    Given I am on the sign up page
    When I enter email and password
    When I enter my new confirmation code
    When I click continue on the confirmation page
    Then I am taken to the dashboard page for the new user

  @Chrome
  Scenario: User can sign in to the Great services
    Given I am on the login page
    When I enter sso login credentials
    Then I am taken to the user dashboard page
