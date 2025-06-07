Feature: Add to Cart
  Scenario: the user should able to add product into cart
    Given user open the login page
    And the user enter "Bittu" as username
    And the user enter "mjk" as password
    When the user click on login button
    And the user click on product name
    Then that product be successfully added

  Scenario: the user should able to be place an order
    When the user click on cart button
    Then the selected product should be visible
    And  the user click on placeOrder button
    And the user able to put all the details
    And the user sucessfully logout


