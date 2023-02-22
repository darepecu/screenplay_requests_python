@global
Feature: Login in the aplication 
  
  Scenario: Login with correct credentials
    Given final user want to login in the aplicacion 
    When the user send credentials
    Then the response status code is "200"
    And the response contains authentication token