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
        await ctx.send(embed=embed_var)

    @commands.command()
    async def pokemon(self,ctx,pokemon):
        data = requests.get(POKE_API_URL + 'pokemon/' + pokemon).json()
        types = " | ".join([type_name['type']['name'] for type_name in data['types']])
        
        embed_var = discord.Embed(title=data['name'], description=str(types), color=0x7289da)
        embed_var.set_thumbnail(url=data['sprites']['front_default'])
        await ctx.send(embed=embed_var)

def setup(client):
    client.add_cog(Pokemon(client))