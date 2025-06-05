Feature: Add to Cart
  Scenario: the user should able to add product into cart
    Given user open the login page
    And the user enter "trf" as usename
    And the user enter "vbn1" as pasword
    When the user click on login button
    And the user click on product name
    Then that product be sucessfully added
