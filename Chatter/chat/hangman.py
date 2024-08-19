# chat/hangman.py

import random

class HangmanGame:
    WORDS = ['python', 'django', 'chatbot', 'hangman', 'websocket']

    def __init__(self):
        self.word = random.choice(self.WORDS)
        self.guesses = []
        self.max_attempts = 6
        self.attempts = 0
        self.current_state = ['_'] * len(self.word)

    def guess(self, letter):
        if letter in self.guesses:
            return f"You've already guessed '{letter}'."

        self.guesses.append(letter)

        if len(letter) > 1:
            if letter == self.word:
                return f"Congratulations! You've won! The word was '{self.word}'."
            else:
                self.attempts += 1
                if self.attempts >= self.max_attempts:
                    return f"Game Over! You've run out of attempts. The word was '{self.word}'."
                else:
                    return f"Incorrect! You have {self.max_attempts - self.attempts} attempts left. Current word: {' '.join(self.current_state)}"
        else:
            if letter in self.word:
                for index, char in enumerate(self.word):
                    if char == letter:
                        self.current_state[index] = letter
                if '_' not in self.current_state:
                    return f"Congratulations! You've won! The word was '{self.word}'."
                else:
                    return f"Correct! Current word: {' '.join(self.current_state)}"
            else:
                self.attempts += 1
                if self.attempts >= self.max_attempts:
                    return f"Game Over! You've run out of attempts. The word was '{self.word}'."
                else:
                    return f"Incorrect! You have {self.max_attempts - self.attempts} attempts left. Current word: {' '.join(self.current_state)}"

    def get_current_state(self):
        return f"Current word: {' '.join(self.current_state)}. Attempts left: {self.max_attempts - self.attempts}."
