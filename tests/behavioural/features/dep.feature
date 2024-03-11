
Feature: Digital Entry Point
  As a user
  I want to be able to access and use DEP (Digital Entry Point)

  @Chrome
  Scenario: User can see 'Export support for UK businesses' link in footer and visit DEP triage landing page
     Given I am on the homepage
     When I click on the "Export support for UK businesses" link in footer
     Then The DEP triage landing page is loaded
