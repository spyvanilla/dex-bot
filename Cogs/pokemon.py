import json
from pprint import pprint

import requests
import discord
from discord.ext import commands

POKE_API_URL = 'https://pokeapi.co/api/v2/'

class Pokemon(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.command()
    async def help(self,ctx):
        embed_var = discord.Embed(title="Commands", description="Search for everything pokemon related here!", color=0x7289da)
        embed_var.set_thumbnail(url=self.client.user.avatar_url)
        
        embed_var.add_field(name="**pokemon**",value="Search for a pokemon in pokedex and get basic info about it",inline=False)
        await ctx.send(embed=embed_var)

    @commands.command()
    async def pokemon(self,ctx,pokemon):
        try:
            data = requests.get(f'{POKE_API_URL}pokemon/{pokemon}').json()
        except json.decoder.JSONDecodeError: # if the request returns 404, it raises an error when decoding to json
            await ctx.send("Pokemon not found!")
            return

        types = " | ".join([type_name['type']['name'].capitalize() for type_name in data['types']])
        abilites = " | ".join(ability['ability']['name'].replace('-',' ').capitalize() for ability in data['abilities'])

        embed_var = discord.Embed(title=data['name'].capitalize(), description=str(types), color=0x7289da)
        embed_var.set_thumbnail(url=data['sprites']['front_default'])

        embed_var.add_field(name="Height",value=f"{data['height']} m",inline=False)
        embed_var.add_field(name="Weight",value=f"{data['weight']} kg",inline=False)
        embed_var.add_field(name="Abilities",value=abilites,inline=False)
        embed_var.add_field(name="XP given",value=f"{data['base_experience']} xp",inline=False)
        await ctx.send(embed=embed_var)

def setup(client):
    client.add_cog(Pokemon(client))