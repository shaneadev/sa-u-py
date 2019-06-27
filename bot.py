import discord
from discord.ext.commands import Bot
import asyncio
import time
import os

Client = discord.Client()
client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
	print("I am online now!")

@client.event
async def on_message(message):
	if message.content.startswith('hello'):
		msg = 'Hello (0.author.mention), how are you today?'.format(message)
		await client.send_message(message.channel, msg)
		
client.run(os.getenv('TOKEN'))
