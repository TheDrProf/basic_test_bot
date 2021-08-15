from discord.ext import commands
import json
import time
import aiohttp
import asyncio
import os

#Load your Data for info below
with open('data/data.json', 'r') as f:
    data = json.load(f)

#set your variables from your data[]
token = data['token'] #Dont Share -- Bot Login key
bot_description = "Test Bot" #basic bot description
prefix = data['prefix'] #set your prefix variable

bot = commands.Bot(command_prefix=prefix, description=bot_description) #define bot and setup prefix and description
startupchannel = int(data['startupchannel']) #channel where you want start up message to go

class TestBot(): #build bot class
    def session(self):
        return self.bot.session

    @bot.event #tells this is bot event
    async def on_ready(): # when bot is ready event
        sendbotchannel = bot.get_channel(startupchannel) # get that startup channel

###
        print('\n################')
        print("Bot is online!")
        print('################')
        print('Logged in as:')
        print(bot.user.name)
        print(bot.user.id)
        print('Prefix: ', prefix)
        print('#################\n')
### -- This sends bot online/info to terminal

        y = os.listdir("cogs") #list all files in cogs folder
        for i in y: #for loop for that list of cogs
            if i in ["__pycache__","cog_template.py"]: #skip the pointless files
                continue #SKIP
            else: # if it aint those lets load them
                i = i[:-3] # remove .py from cogs list <cogs.py> -> <cogs>
                print(f"\nLoading cog --{i}") #terminal notification
                try: # try to load cog
                    bot.load_extension(f'cogs.{i}') # load cog
                except Exception as error: # if fails error here
                    print(f"<<# !-!- ERROR COG '{i}' -!-! #>>{error}") #error to terminal
        await sendbotchannel.send(":cookie:`<<<---BOT IS READY--->>>`:cookie:") #bot is done to startup channel
        print("\n<<< --- Bot is Ready --- >>>") # bot is ready to terminal

bot.run(token) # run all that shit ^^^ with given token
