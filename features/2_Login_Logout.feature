Feature: User Login and Logout
  Scenario Outline: the user can able to login and logout
    Given user open the login page
    And the user enter "<usename>" as usename
    And the user enter "<pasword>" as pasword
    When the user click on login button
    Then login should be happen
    And the user sucessfully logout
    Examples:
      |usename |pasword |
      |trf      |vbn1     |
      |cvrt     |mjk      |

  Scenario: Invalid login
  Given user open the login page
  And the user enter "wronguser" as usename
  And the user enter "wrongpass" as pasword
  When the user click on login button
  Then error alert should be shown