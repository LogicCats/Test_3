import random
import time

class FootballMatch:
    def __init__(self, team_a, team_b):
        self.team_a = team_a
        self.team_b = team_b
        self.team_a_score = 0
        self.team_b_score = 0

    def play_half(self):
        print(f"Идет тайм для {self.team_a} и {self.team_b}...")
        time.sleep(1)  # Имитация времени игры
        self.team_a_score += random.randint(0, 1)
        self.team_b_score += random.randint(0, 1)
        self.display_score()

    def display_score(self):
        print(f"Текущий счет: {self.team_a} {self.team_a_score} - {self.team_b_score} {self.team_b}")

    def play_match(self):
        print(f"Матч между {self.team_a} и {self.team_b} начался!")
        self.play_half()
        self.play_half()
        self.display_final_result()

    def display_final_result(self):
        print("Матч завершен!")
        result = self.get_result()
        print(result)

    def get_result(self):
        if self.team_a_score > self.team_b_score:
            return f"{self.team_a} выигрывает!"
        elif self.team_b_score > self.team_a_score:
            return f"{self.team_b} выигрывает!"
        else:
            return "Ничья!"

if __name__ == "__main__":
    # Пример использования
    match = FootballMatch("Команда A", "Команда B")
    match.play_match()
