Feature: Football Match Simulation

  Scenario: Start a football match
    Given a football match between "Team A" and "Team B"
    When the match is played
    Then the score should be displayed
    And the match result should be announced

  Scenario: End a football match
    Given a football match between "Team A" and "Team B"
    When the match is played
    Then the score should be displayed
    And the match result should be announced
