@eyb_random_data
Feature: Expand Your Business
    As a logged in user
    I want to be able to engage with the Expand Your Business service offering

    @Chrome
    Scenario: User can sign up to the EYB service
        Given I am on the sign-up page
        When I enter registration credentials
        And I enter a confirmation code
        And I complete company details
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
        And I complete the triage
        Then the guide page is displayed

    @Chrome
    Scenario: User can edit related business information
        Given I am signed in
        When I complete the triage
        And I navigate to the EYB guide page
        And I click change your answers
        Then I am taken to the Change your answers summary page
        And the data presented matches previously entered data
        And clicking change beside an attribute enables the answer to be changed and persisted

    @Chrome
    Scenario: Guide page contains checklist and personalised guide
        Given I am signed in
        When I complete the triage
        And I navigate to the EYB guide page
        Then the guide page is displayed
