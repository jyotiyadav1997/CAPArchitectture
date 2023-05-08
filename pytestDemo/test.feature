Feature: Register User
  User logs in and registers with PII data

  Scenario: Registering the user
    Given : I am user
    And I have PII data
    When I go to FSPU site
    And I enter email Id
    Then I should be able to proceed
    And user should get register page
