Feature: User Registration
  Scenario Outline: the user should be able to register
    Given the user is on the Register page
    And the user enter <username> as username
    And the user enter <password> as password
    When the user click on SignUp button
    Then registration should be displayed successfully

    Examples:
      | username | password |
      | Manish   | vbn1     |
      | Bittu    | mjk      |
      | Vikram   | yut      |
      | Moni     | 123      |
