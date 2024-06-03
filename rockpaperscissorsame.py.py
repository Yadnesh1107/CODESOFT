import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissors:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissors")

        self.choices = ['Rock', 'Paper', 'Scissors']
        self.user_score = 0
        self.computer_score = 0

        # Labels for displaying scores
        self.user_score_label = tk.Label(root, text="User Score: 0")
        self.user_score_label.pack(pady=5)

        self.computer_score_label = tk.Label(root, text="Computer Score: 0")
        self.computer_score_label.pack(pady=5)

        # Result display
        self.result_label = tk.Label(root, text="Make your choice!", font=('Helvetica', 14))
        self.result_label.pack(pady=20)

        # Buttons for user choices
        self.rock_button = tk.Button(root, text="Rock", command
=lambda: self.play_game('Rock'))
        self.rock_button.pack(side=tk.LEFT, padx=20, pady=10)

        self.paper_button = tk.Button(root, text="Paper", command=lambda: self.play_game('Paper'))
        self.paper_button.pack(side=tk.LEFT, padx=20, pady=10)

        self.scissors_button = tk.Button(root, text="Scissors", command=lambda: self.play_game('Scissors'))
        self.scissors_button.pack(side=tk.LEFT, padx=20, pady=10)

        # Play again button
        self.play_again_button = tk.Button(root, text="Play Again", command=self.reset_game)
        self.play_again_button.pack(pady=20)

    def play_game(self, user_choice):
        computer_choice = random.choice(self.choices)
        result = self.determine_winner(user_choice, computer_choice)

        self.result_label.config(text=f"User: {user_choice} | Computer: {computer_choice}\n{result}")

        self.user_score_label.config(text=f"User Score: {self.user_score}")
        self.computer_score_label.config(text=f"Computer Score: {self.computer_score}")

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
             (user_choice == 'Scissors' and computer_choice == 'Paper') or \
             (user_choice == 'Paper' and computer_choice == 'Rock'):
            self.user_score += 1
            return "You win!"
        else:
            self.computer_score += 1
            return "You lose!"

    def reset_game(self):
        self.user_score = 0
        self.computer_score = 0
        self.user_score_label.config(text="User Score: 0")
        self.computer_score_label.config(text="Computer Score: 0")
        self.result_label.config(text="Make your choice!")

if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissors(root)
    root.mainloop()
