@eyb_random_data @wip
Feature: Expand Your Business
  As a logged out user
  I want to be able to engage with the Expand Your Business service offering

  @Chrome
  Scenario: Limited 'logged out' experience available
    Given I am on the EYB landing page
    When I complete the triage
    Then The guide page is displayed with limited information
