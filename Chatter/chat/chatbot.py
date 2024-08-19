# chat/chatbot.py
from .hangman import HangmanGame

class SimpleChatBot:
    def __init__(self):
        # You can define more sophisticated rules here
        self.responses = {
            "hello": "Hi there! How can I assist you today?",
            "how are you": "I'm just a bot, but I'm here to help you!",
            "what is your name": "I am your friendly chat assistant.",
            "help": "You can ask me anything about the chat application.",
        }
        self.games = {}
    
    def get_response(self, message, room_name=None):
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

        message = message.lower()
        for key in self.responses:
            if key in message:
                return self.responses[key]
        return "I'm not sure how to respond to that. Try asking something else!"
