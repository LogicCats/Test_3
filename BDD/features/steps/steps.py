import random
from behave import given, when, then

class FootballMatch:
    def __init__(self, team_a, team_b):
        self.team_a = team_a
        self.team_b = team_b
        self.team_a_score = 0
        self.team_b_score = 0

    def play_half(self):
        self.team_a_score += random.randint(0, 1)
        self.team_b_score += random.randint(0, 1)

    def play_match(self):
        self.play_half()
        self.play_half()

    def get_score(self):
        return f"{self.team_a} {self.team_a_score} - {self.team_b_score} {self.team_b}"

    def get_result(self):
        if self.team_a_score > self.team_b_score:
            return f"{self.team_a} выигрывает!"
        elif self.team_b_score > self.team_a_score:
            return f"{self.team_b} выигрывает!"
        else:
            return "Ничья!"


@given('a football match between "{team_a}" and "{team_b}"')
def step_given_football_match(context, team_a, team_b):
    context.match = FootballMatch(team_a, team_b)


@when('the match is played')
def step_when_match_played(context):
    context.match.play_match()


@then('the score should be displayed')
def step_then_score_displayed(context):
    score = context.match.get_score()
    print(f"Текущий счет: {score}")


@then('the match result should be announced')
def step_then_match_result(context):
    result = context.match.get_result()
    print(result)


#behave
