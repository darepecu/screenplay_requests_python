@poke @index
Feature: Index pokemon

Scenario: Show all pokemon
    Given final user is loged in app
    When send a request to show all pokemons 
    Then the response status code is "200"
    And the response contains results all pokemons