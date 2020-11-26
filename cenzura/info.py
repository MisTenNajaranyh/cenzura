import discord
from discord.ext import commands
import requests
import os
import psutil
import humanize
import platform

class Info(commands.Cog):
    def __init__(self, client):
        self.bot = client
        
    @commands.command(description="Pokazuje ekipe bota", usage="team")
    async def team(self, ctx):
        poligon = {
            "owners": [
                0,
                0
            ],
            "poligon": [
                0,
                0
            ]
        }

        e = discord.Embed(title="Ekipa:", description="\n".join(list(map(lambda user: self.bot.get_user(user).name + "#" + self.bot.get_user(user).discriminator, poligon["owners"]))) + "\n\n**Reszta poligonu**:\n" + "\n".join(list(map(lambda user: self.bot.get_user(user).name + "#" + self.bot.get_user(user).discriminator, poligon["poligon"]))), color= discord.Color.red())
        e.set_thumbnail(url=self.bot.user.avatar_url)
        await ctx.send(embed=e)
        
    @commands.command(description="Pokazuje statystyki bota", usage="botstats")
    async def botstats(self, ctx):
        e = discord.Embed(title="Statystyki bota:", description=f"Serwery: `{len(self.bot.guilds)}`\nUżytkownicy: `{len(self.bot.users)}`\n\nKomendy: `{len(self.bot.commands)}`\n\nWersja Python: `{platform.python_version()}`\nWersja discord.py: `{discord.__version__}`\n\nWykorzystana pamięć RAM: `{humanize.naturalsize(psutil.Process().memory_full_info().rss)}`\nWykorzystane CPU: `{psutil.cpu_percent()}%`", color=discord.Color.red())
        
        await ctx.send(embed=e)
      
def setup(client):
    client.add_cog(Info(client))
    print("Załadowano info")
