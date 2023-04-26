# README

## Overview
This code is for creating a Discord bot using the OpenAI's GPT-3 language model. The bot uses the Discord API to receive and send messages and the OpenAI API to generate responses to messages received.

The code allows users to easily create their own bots by changing the values of openai.api_key, DISCORD_TOKEN, and fst_message to their own OpenAI API key, Discord token, and initial message prompt respectively.

## Prerequisites
To use this code, you need to have the following:

Python 3.6 or later installed on your computer.
A Discord account and a Discord bot application created. You can follow the official Discord guide to create a bot application and retrieve its token.
Plus an OpenAI API key.

## Usage
Clone this repository to your local machine.
Open the project in your preferred code editor.
Replace empty strings of openai.api_key in gpt_part.py file and DISCORD_TOKEN in discord_bot.py file with your own OpenAI API key and Discord bot token respectively.
Optionally, you can change the prompt message to your desired message by modifying the fst_message variable in gpt_part.py file.
Save the changes.
Install the required packages by running pip install -r requirements.txt.
Run the bot by executing the main.py file with the command python main.py.
Invite the bot to your Discord server using the generated OAuth2 URL from the Discord bot application page.
Start chatting with the bot in a Discord channel.
Remember to @mention the bot or talk to it on private.

Note: This code is a basic template for creating a Discord bot using the OpenAI API. You may need to modify the code to suit your specific use case.
