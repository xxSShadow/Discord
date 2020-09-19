  
import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix='/')

@client.event
async def on_ready():
    print('Logged In As ' + client.user.name)

# ↓↓↓Command Goes Here↓↓↓

# ↑↑↑Command Goes Here↑↑↑

client.run('token')
