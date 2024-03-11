Feature: Expand Your Business
  As a user
  I want to be able to use EYB (Expand Your Business)

  @Chrome
  Scenario: Limited 'logged out' experience available
    Given I am on the EYB landing page
    When I complete the triage
    Then The guide page is displayed with limited information

  @Chrome
  Scenario: User can sign up to the EYB service
    Given I am on the sign-up page
    When I complete the sign-up form
