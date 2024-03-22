@great_random_data
Feature: Single Sign On
  As a user
  I want to be able to engage with Great service offering

  @Chrome
  Scenario: User can sign up to the Great services
    Given I am on the great.gov.uk homepage
    And I navigate to the sign up page
    When I enter email and password
    And I enter my new confirmation code
    And I click continue on the confirmation page
    Then I am taken to the dashboard page for the new user

  @Chrome
  Scenario: User can sign in to the Great services
    Given I am on the great homepage
    When I complete the sign in steps
    Then I am taken to the user dashboard page

  @Chrome
  Scenario: User can sign out to the Great services
    Given I am on the main homepage
    And I complete the authentication steps
    When I am taken to the dashboard page
    And I click the sign out button
    Then I am taken back to great.gov.uk
