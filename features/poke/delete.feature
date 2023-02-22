@poke @delete
Feature: Delete pokemon

Scenario Outline: Delete a pokemon
    Given final user is loged in app
    When send a request to delete pokemon with id "<id>" 
    Then the response status code is "200"
    
    Examples:
    | id  |
    | 005 |