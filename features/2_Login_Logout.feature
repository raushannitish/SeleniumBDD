Feature: User Login and Logout
  Scenario: the user can able to login and logout
    Given user open the login page
    And the user enter "Bittu" as username
    And the user enter "mjk" as password
    When the user click on login button
    Then login should be happen
    And the user sucessfully logout


  Scenario: Invalid login
  Given user open the login page
  And the user enter "trf" as u_name
  And the user enter "vb" as p_assword
  When the user click on login button
  Then error alert should be shown