@eyb_random_data @wip
Feature: Expand Your Business
    As a logged in user
    I want to be able to engage with the Expand Your Business service offering

    @Chrome
    Scenario: User can sign up to the EYB service
        Given I am on the sign-up page
        When I enter registration credentials
        When I enter a confirmation code
        When I complete company details
        Then I am am taken to the EYB guide page with registration confirmation

    @Chrome
    Scenario: User can sign in to the EYB service
        Given I am on the sign-in page
        When I enter login credentials
        Then I am am taken to the EYB guide page

    @Chrome
    Scenario: User can add related business information
        Given I am on the EYB landing page
        When I am signed in
        When I complete the triage
        Then the guide page is displayed
