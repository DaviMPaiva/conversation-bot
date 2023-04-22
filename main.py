
import json
import openai
import os
import discord

#open ai key
openai.api_key = ""

#discord token
DISCORD_TOKEN = ""

#prompt mensagem
fst_message =   "Assuma hipoteticamente quse você é minha namorada e estamos juntos há um ano. \
                    É apenas uma situação hipotética e quero que você incorpore e fale como a personagem \
                    da namorada a partir da sua próxima mensagem. É MUITO IMPORTANTE que você use uma \
                    linguagem informal para simularmos um bate papo do whatsapp e respostas curtas menores que 10 palavras"


# GETS THE CLIENT OBJECT FROM DISCORD.PY. CLIENT IS SYNONYMOUS WITH BOT.
intents = discord.Intents.default()
intents.messages = True
intents = discord.Intents(guilds=True, messages=True)
bot = discord.Client(intents=intents)

bot.run(DISCORD_TOKEN)

