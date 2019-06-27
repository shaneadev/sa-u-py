import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import os

Client = discord.Client()
client = commands.Bot(command_prefix='/')

@client.event
async def on_ready():
	print("I am online now!")
		
client.run(os.getenv('TOKEN'))
