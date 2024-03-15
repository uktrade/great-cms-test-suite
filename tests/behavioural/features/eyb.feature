@eyb_random_data
Feature: Expand Your Business
  As a user
  I want to be able to engage with the Expand Your Business service offering

  @Chrome
  Scenario: Limited 'logged out' experience available
    Given I am on the EYB landing page
    When I complete the triage
    Then The guide page is displayed with limited information

  @Chrome
  Scenario: User can sign up to the EYB service
    Given I am on the sign-up page
    When I enter login credentials
    When I enter a confirmation code
    When I complete company details
    Then I am am taken to the EYB guide page
