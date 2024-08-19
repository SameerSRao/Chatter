# Chatter - A Django-Based Real-Time Chat Application with AI Chatbot Integration

## Description

**Chatter** is a real-time chat application built using Django, Django Channels, and WebSockets. The application supports multiple chat rooms, user authentication, and features a simple AI chatbot that interacts with users, providing assistance and entertainment. The AI chatbot includes a basic keyword-matching system and supports playing games like Hangman. Additionally, the application includes a recap feature that summarizes missed messages, ensuring users stay updated with ongoing conversations.

## Features
1. Real-Time Chat

    - WebSockets: Leveraging Django Channels for real-time communication, enabling users to chat instantly in various chat rooms.
    - Multiple Chat Rooms: Users can create, join, and leave chat rooms. Each room is independent, and users can participate in multiple rooms.
    - Message History: Chat history is stored and loaded when a user joins a room, ensuring that conversations persist across sessions.
    - User Authentication: Integrated user registration and login system using Django’s built-in authentication framework.

2. AI Chatbot

    - Keyword Matching: The chatbot responds to specific commands or keywords, providing pre-defined responses to user queries.
    - Hangman Game: Users can play a game of Hangman by entering the !hangman command. The bot manages the game state, taking guesses and providing feedback.
    - Custom Responses: The chatbot can be easily extended with new responses and commands.

3. Recap Feature

    - Automatic Recap Summary: When users rejoin a chat room, they receive a recap of all the messages they missed since their last visit, helping them catch up on important discussions.

4. User Interface

    - Bootstrap-Enhanced UI: A clean, responsive interface built with Bootstrap, offering an intuitive user experience.
    - Message Bubbles: User messages are displayed in styled chat bubbles, with different colors for users and the chatbot.
    - Scroll Management: Automatic scrolling ensures that users always see the latest messages without manual intervention.

5. Admin Features

    - Manage Users and Rooms: Administrators can manage chat rooms and users through Django's admin panel.
    - Message Moderation: Admins can delete messages or clean up chat histories if necessary.
    - User Roles: Different user roles (e.g., Admin, Moderator, Regular User) can be assigned to manage permissions.

### Dependencies

* Describe any prerequisites, libraries, OS version, etc., needed before installing program.
* ex. Windows 10

### Installing

* How/where to download your program
* Any modifications needed to be made to files/folders

### Executing program

* How to run the program
* Step-by-step bullets
```
code blocks for commands
```

## Help

Any advise for common problems or issues.
```
command to run if program contains helper info
```

## Authors

Contributors names and contact info

ex. Dominique Pizzie  
ex. [@DomPizzie](https://twitter.com/dompizzie)

## Version History

* 0.2
    * Various bug fixes and optimizations
    * See [commit change]() or See [release history]()
* 0.1
    * Initial Release

## License

This project is licensed under the [NAME HERE] License - see the LICENSE.md file for details

## Acknowledgments

Inspiration, code snippets, etc.
* [awesome-readme](https://github.com/matiassingers/awesome-readme)
* [PurpleBooth](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
* [dbader](https://github.com/dbader/readme-template)
* [zenorocha](https://gist.github.com/zenorocha/4526327)
* [fvcproductions](https://gist.github.com/fvcproductions/1bfc2d4aecb01a834b46)
