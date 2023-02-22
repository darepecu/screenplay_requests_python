@poke @show
Feature: Show information pokemon

Scenario Outline: Show a pokemon
    Given final user is loged in app
    When send a request to show a pokemon with id "<id>"
    Then the response status code is "200"
    And the response contains results all information for pokemon with id "<id>"
    
    Examples:
    | id |
    | 12 |
    | 2  |
    | 3  |
