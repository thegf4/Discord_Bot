import discord
from discord.ext import commands

client  = commands.Bot(command_prefix = '\')

@client.event
async def on_ready():
    print("Trudi's FINALLY ready")

client.run("ODQwOTMxNTUyNDQzNDk4NTM2.YJfYiQ.dqyoly0dmS59Eypr-Nh7TYppM_I")