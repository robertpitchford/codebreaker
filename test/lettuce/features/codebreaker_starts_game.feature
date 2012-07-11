Feature: Running codebreaker

  As a codebreaker
  I want to start a game
  So that I can break the code

  Scenario: start a game
    Given codebreaker is not running
    When I start a new game
    Then I should see "Welcome to Codebreaker!"
    And  I should see "Enter guess:"