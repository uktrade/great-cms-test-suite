@great_random_data
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

  @Chrome
  Scenario: View events
    Given I am in export academy events page and logged in
    When I click on an event
    Then I should see details of that event

  @Chrome
  Scenario: Events Filters
    Given I am in UK Export Academy landing page
    When I click sector & market card
    Then I should be in "UK Export Academy Events" page with both sector and master filters on
