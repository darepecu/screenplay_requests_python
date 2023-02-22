@poke @update
Feature: Update information pokemon

Scenario Outline: Update a pokemon
    Given final user is loged in app
    When send a request to update "<id>" user to field "<field>" with value "<new_value>"
    Then the response status code is "200"
    And the response contains new information from pokemon "<field>" with value "<new_value>"
    
    Examples:
    | id | field | new_value  |
    | 3  | name  | pokelupita |
