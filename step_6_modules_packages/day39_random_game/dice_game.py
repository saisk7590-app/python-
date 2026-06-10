# dice_game.py

import random

class DiceGame:
    def __init__(self):
        self.rounds = 5
        self.reset_scores()

    def reset_scores(self):
        self.player_score = 0
        self.computer_score = 0

    def roll_dice(self):
        return random.randint(1, 6)

    def play_round(self, round_number):
        player_roll = self.roll_dice()
        computer_roll = self.roll_dice()

        print(f"\n🎯 Round {round_number}")
        print(f"Player rolled: {player_roll}")
        print(f"Computer rolled: {computer_roll}")

        if player_roll > computer_roll:
            self.player_score += 1
            print("👉 Player wins this round!")
        elif computer_roll > player_roll:
            self.computer_score += 1
            print("👉 Computer wins this round!")
        else:
            print("👉 Round is a tie!")

    def show_final_result(self):
        print("\n🏁 Final Scores")
        print(f"Player: {self.player_score}")
        print(f"Computer: {self.computer_score}")

        if self.player_score > self.computer_score:
            print("🏆 Player wins the game!")
        elif self.computer_score > self.player_score:
            print("🏆 Computer wins the game!")
        else:
            print("🤝 The game is a tie!")

    def play(self):
        self.reset_scores()

        for i in range(1, self.rounds + 1):
            self.play_round(i)

        self.show_final_result()