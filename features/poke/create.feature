@poke @create
Feature: Create a new pokemon

Scenario: Create a pokemon
    Given final user is loged in app
    When send a request to create a new pokemon
    Then the response status code is "201"
    And the response contains the information from new pokemon

