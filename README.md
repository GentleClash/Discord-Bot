


# Discord Bot with Chat, Reminders, and Music
My first project. A very basic bot.

This is a Python-based Discord bot that provides chat, reminders, and music functionalities. The bot is built using the OpenAI GPT-3 API for chat responses and allows users to set reminders and play, pause, and skip songs from ~~YouTube~~ Spotify.

## Features

- Chat: The bot responds to user messages in the Discord server using the OpenAI GPT-3 API, providing interactive chat-based conversations.
- Reminders: Users can create, delete, and modify reminders by sending a message with the time and date of the reminder in a specific format.
- Music: Users can control music playback on the Discord server by sending commands to play, pause, and skip songs from ~~YouTube~~ Spotify.

## Installation

To use the Discord bot, you need to follow these installation steps:

1. Clone the repository to your local machine:
`git clone https://github.com/GentleClash/Discord-Bot.git`

2. Install the required dependencies:
`pip install -r requirements.txt`

3. Set up the necessary API keys:
- GPT-3 API: Sign up for an API key from OpenAI and update the `config.py` file with your API key.
- Spotify API: Follow the instructions <a href ="https://youtu.be/kaBVN8uP358">here</a> to create a project, and obtain an client id and client secret. Update the `config.py` file with your keys.
4. In the `config.py` file, replace the placeholders for `BOT_TOKEN`, `CLIENT_ID`, `CLIENT_SECRET`, `REDIRECT_URI`, and `OPENAI_API_KEY` with your own values.
5. If you plan on using the Spotify functionality, make sure you have a premium account and follow the instructions in the terminal to authenticate your account.

## Usage

To run the Discord bot, execute the following command in your terminal:

`python bot.py`

The bot will connect to your Discord server and start listening for commands. You can use various commands to interact with the bot, such as sending messages for chat, setting reminders, and controlling music playback.

## Contributions

Contributions to this project are welcome! If you would like to contribute, please fork the repository, create a new branch for your changes, and submit a pull request. 

## License

This project is licensed under the GNU General Public License v3.0 (GPL-3.0). For more details, please see the [LICENSE](LICENSE) file.

## Contact

If you have any questions, suggestions, or feedback about this project, please contact [Ayush Bajpai](github.com/GentleClash) at [Telegram](https://t.me/Ayush_Bajpai) {check the pinned message there for currently active username}.



