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
	
## start hello command
def hello_function(message, client, args):
    try:
        return 'Hello {}, Argument One: {}'.format(message.author, args[0])
    except Exception as e:
        return e
ch.add_command({
    'trigger': '/hello',
    'function': hello_function,
    'args_num': 1,
    'args_name': ['string'],
    'description': 'Will respond hello to the caller'
})
		
client.run(os.getenv('TOKEN'))
