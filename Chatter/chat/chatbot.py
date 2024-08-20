# chat/chatbot.py
from .hangman import HangmanGame
from openai import OpenAI

class GPTChatBot:
    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key)
        self.games = {}
    
    def get_response(self, message, room_name):
        if message == "hangman":
            if room_name not in self.games:
                self.games[room_name] = HangmanGame()
                return f"Starting a new Hangman game! Enter '!guess' to make a guess.\n{self.games[room_name].get_current_state()}"
            else:
                return "A Hangman game is already in progress. " + self.games[room_name].get_current_state()
        
        elif message.startswith("guess"):
            if room_name in self.games:
                game = self.games[room_name]
                guess = message.split(' ')[1] if len(message.split(' ')) > 1 else ''
                if guess.isalpha():
                    response = game.guess(guess)
                    if 'Game Over' in response or 'Congratulations' in response:
                        del self.games[room_name]  # End the game if it's over
                    return response
                else:
                    return "Please enter a valid guess."
            else:
                return "No Hangman game in progress. Start a game with `!hangman`."

        try:
            response = self.client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": f"respond to this message in less than 100 words: {message}",
                    }
                ],
                model="gpt-4o-mini",
                max_tokens=150,
            )
            return (response.choices[0].message.content)
        except Exception as e:
            return f"Sorry, I couldn't process your request: {str(e)}"