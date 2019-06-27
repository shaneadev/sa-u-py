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
def hello_function(message,client,args):
    try:
        return 'Hello {}, Argument One: {}'.format(message.author, args[0])
    except Exception as e:
        return e

# hello command dictionary
hello_command = {
    # if the string starts with this the function will be called
    'trigger': '!hello',
    
    # specifies the function to call
    'function': hello_function,
    
    # number of arguments that the functions needs
    'args_num': 1,
    
    # name of the argument that the funtions takes
    'args_name': ['string'],
    
    # describes what the function does
    'description': 'Will respond hello to the caller and show arg 1'
}
		
client.run(os.getenv('TOKEN'))
