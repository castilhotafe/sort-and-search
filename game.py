"""Python Guessing Game"""
# version 1
import random

from typing import Literal, Callable

clues = Literal['correct', 'higher', 'lower']
interaction = Literal['ai', 'human']

def prompt_guess(min_value: int, max_value: int) -> int:
    while True:
        try:
            guess = int(input(f"guess {min_value}-{max_value}?> "))
        except ValueError:
            print("Please guess a valid number")
            continue
        return guess

class Game:

    def __init__(self, max_value: int = 100, prompt: Callable = prompt_guess):
        self.max_value = self.upper_bound = max_value
        self.min_value = self.lower_bound = 1
        self.secret = random.randint(self.min_value, self.max_value)
        self.prompt = prompt
        self.tries = 0

    def _provide_clues(self, guess: int) -> tuple[int, int, clues]:

        if guess == self.secret:
            return guess, guess, "correct"
        elif guess < self.secret:
            return guess + 1, self.upper_bound, "higher"
        else:
            return self.lower_bound, guess - 1, "lower"

    def make_guess(self) -> clues:
        self.tries += 1
        guess = self.prompt(self.lower_bound, self.upper_bound)
        self.lower_bound, self.upper_bound, clue = self._provide_clues(guess)
        return clue

    def display_clue(self, clue):
        return f"Guess {clue}"

    def play(self):
        print(f"Guess a number between {self.min_value} - {self.max_value}")
        while True:
            clue = self.make_guess()
            if clue == 'correct':
                print("You win!")
                break
            print(self.display_clue(clue))
        print(f"You won in {self.tries} tries")


if __name__ == '__main__':
    game = Game(max_value = 100)
    game.play()
