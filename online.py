import discord
from discord.ext import commands
from colorama import Fore
from colorama import init
import json
init()
bot = commands.Bot(command_prefix="!", self_bot=True)


with open('token.json', 'r') as myfile:
    data=myfile.read()
obj = json.loads(data)
TOKEN_AUTH = str(obj["token"])



@bot.event
async def on_ready():
    print(f" > Connected to User: {Fore.RED}{bot.user.name}{Fore.RESET}")
    print(f" > User ID: {Fore.RED}{bot.user.id}{Fore.RESET}")
    print(f" > RPC {Fore.RED}started{Fore.RESET}!")
    await bot.change_presence(activity=discord.Streaming(name='Funny Shit', platform="YouTube", url='https://www.youtube.com/watch?v=iik25wqIuFo')) ### this only works with yt or twitch links!
    ### Other status Ideas: (You can also loop them if you want)
    ### await client.change_presence(activity=discord.Game('Sea of Thieves')) <<< Makes it seem like you are playing Sea of thieves
    ### await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='Netflix')) <<< Makes it seem like you are watching Netflix
    ### await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='Music')) <<< Makes it seem like you are listening to Music



@bot.event
async def on_message(message):
    if bot.user.mentioned_in(message):
        if message.channel.type is discord.ChannelType.private:
            print(f" > You got Pinged/Mentioned in: {Fore.RED}{message.channel}{Fore.RESET}")
        else:
            print(f" > You got Pinged/Mentioned in Guild: {Fore.RED}{message.guild}{Fore.RESET}, in channel: {Fore.RED}#{message.channel}{Fore.RESET}")
    else:
        if message.channel.type is discord.ChannelType.private:
            if message.author == bot.user:
                return
            else:
                print(f" > Message received from {Fore.RED}{message.author}{Fore.RESET} ({message.author.id})!")
                ###print(message.channel) <<< Other way of printing the same thing as above
                ###print(message.content) <<< Doesn't work for some reason idk why
            


bot.run(TOKEN_AUTH, bot=False)