import json
import os

import discord
from discord.ext import commands

with open('credentials.json','r') as f:
    TOKEN = json.load(f)['TOKEN']

client = commands.Bot(command_prefix='??')
client.remove_command('help')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('??help'))
    print("Logged")

for filename in os.listdir("./Cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"Cogs.{filename[:-3]}")

client.run(TOKEN)