import os
import discord


DISCORD_TOKEN = " "

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
client = discord.Client(intents=intents)

def start_bot(get_response):
    @client.event
    async def on_ready():
        print(f"Logged in as {client.user.name}")
    
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        reply = get_response(str(message.author), message.content)
        await message.channel.send(reply)

    client.run(DISCORD_TOKEN)
