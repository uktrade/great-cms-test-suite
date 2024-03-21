Feature: UK Export Academy
  As a user
  I want to be able to engage with the UK Export Academy service offering

  @Chrome
  Scenario: Verify landing page for non logged in users
    Given I am on the UKEA landing page
    Then I should see a sign up cta

  @Chrome
  Scenario: Check Landing page is loaded from home page
    Given I am on Great home page
    When I click “Join the UK export academy” card
    Then I should see UKEA landing page
