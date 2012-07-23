Feature: codebreaker wins the game (or not)

  Scenario: Winning the game
    Given codebreaker is started
    When I guess the correct code
	Then I should see "Correct! You cracked the code"
	And the game should end

  Scenario: Incorrect guess does not end the game
    Given codebreaker is started
    When I guess an incorrect code
	Then I should not see "Correct! You cracked the code"
	And the game should not end