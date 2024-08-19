# chat/chatbot.py

class SimpleChatBot:
    def __init__(self):
        # You can define more sophisticated rules here
        self.responses = {
            "hello": "Hi there! How can I assist you today?",
            "how are you": "I'm just a bot, but I'm here to help you!",
            "what is your name": "I am your friendly chat assistant.",
            "help": "You can ask me anything about the chat application.",
        }
    
    def get_response(self, message):
        message = message.lower()
        for key in self.responses:
            if key in message:
                return self.responses[key]
        return "I'm not sure how to respond to that. Try asking something else!"
