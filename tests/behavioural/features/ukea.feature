Feature: UK Export Academy
  As a user
  I want to be able to engage with the UK Export Academy service offering

  @Chrome
  Scenario: Verify landing page for non logged in users
    Given I am on the UKEA landing page
    Then I should see a sign up cta
