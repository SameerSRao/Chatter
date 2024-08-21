# Chatter

## Description

**Chatter** is a real-time chat application built using Django, Django Channels, and WebSockets. The application supports multiple chat rooms, user authentication, and features a simple AI chatbot that interacts with users, providing assistance and entertainment. The AI chatbot includes a basic keyword-matching system and supports playing games like Hangman. Additionally, the application includes a recap feature that summarizes missed messages, ensuring users stay updated with ongoing conversations.


## Screenshots

<img width="500" alt="Screenshot 2024-08-21 at 3 51 42 PM" src="https://github.com/user-attachments/assets/c9b6e94c-cfd3-4c97-b80c-70b102cb88f5">

<img width="500" alt="Screenshot 2024-08-21 at 3 51 04 PM" src="https://github.com/user-attachments/assets/cb43446d-131a-4df4-8b61-363b8623de4f">

<img width="500" alt="Screenshot 2024-08-21 at 3 56 09 PM" src="https://github.com/user-attachments/assets/5d5a1860-6c68-453d-9f32-de3a84e045e4">

## Features

1. **Real-Time Chat**
   * WebSockets: Leveraging Django Channels for real-time communication, enabling users to chat instantly in various chat rooms.
   * Multiple Chat Rooms: Users can create, join, and leave chat rooms. Each room is independent, and users can participate in multiple rooms.
   * Message History: Chat history is stored and loaded when a user joins a room, ensuring that conversations persist across sessions.
   * User Authentication: Integrated user registration and login system using Django’s built-in authentication framework.

3. **AI Chatbot**
   * AI Powered Chatbot: The application includes an OpenAI-powered chatbot, "ChatterBox," that users can interact with by prefixing messages with a designated command (e.g., !). The chatbot can respond to queries, provide summaries, and engage in simple conversational tasks.
   * Hangman Game: Users can play a game of Hangman by entering the !hangman command. The bot manages the game state, taking guesses and providing feedback.

5. **Recap Feature**
   * Automatic Recap Summary: When users rejoin a chat room, they receive a recap of all the messages they missed since their last visit, helping them catch up on important discussions.

7. **User Interface**
   * Bootstrap-Enhanced UI: A clean, responsive interface built with Bootstrap, offering an intuitive user experience.
   * Message Bubbles: User messages are displayed in styled chat bubbles, with different colors for users and the chatbot.
   * Scroll Management: Automatic scrolling ensures that users always see the latest messages without manual intervention.

9. **Admin Features**
    * Manage Users and Rooms: Administrators can manage chat rooms and users through Django's admin panel.
    * Message Moderation: Admins can delete messages or clean up chat histories if necessary.
    * User Roles: Different user roles (e.g., Admin, Moderator, Regular User) can be assigned to manage permissions.

## Dependencies

* Python 3.8+
* Django 3.0+
* Django Channels
* Redis (for channel layer)

## Installing
1. Clone the repository:
   ```
   git clone https://github.com/yourusername/Chatter.git
   cd Chatter
   ```
2. Create a virtual environment:
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Set up the database:
   ```
   python manage.py migrate
   ```
5. Run Redis (if not running):
   ```
   redis-server
   ```
6. Create a superuser (for admin access):
   ```
   python manage.py createsuperuser
   ```
7. Run the development server:
   ```
   python manage.py runserver
   ```
8. Access the application:
   - Open your browser and navigate to http://127.0.0.1:8000/

### Usage
* **Create Rooms**: Users can create new chat rooms from the homepage.
* **Join Rooms**: Users can join existing chat rooms by entering the room name.
* **Chat with Others**: Start chatting with others in real-time. The message history is available upon joining the room.
* **Interact with Chatbot**: Use the prefix '!' to interact with the Ai Chatbot
* **Play Hangman**: Type !hangman to start a Hangman game with the chatbot. Guess letters using !guess <letter>.
* **Stay Updated**: If you re-enter a chat room, a recap summary will provide you with a summary of all missed messages.
