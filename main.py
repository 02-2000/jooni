import asyncio
import discord
from discord.ext import commands
from check import get_prefix


TOKEN = ''

bot = commands.Bot(command_prefix="J!")

botcolor = 0xffffff

bot.remove_command('help')
########################################################################################################################

extensions = ['commands.autoreact','commands.jail','commands.tempchannel']


@bot.event
async def on_ready():
    print('Online.')
    print('--------------------------------------')
    await status_task()


########################################################################################################################
async def status_task():
    await bot.change_presence(activity=discord.Game('Your Game here'), status=discord.Status.idle)


########################################################################################################################
if __name__ == '__main__':
    for extension in extensions:
        try:
            bot.load_extension(extension)
        except Exception as error:
            print('{} konnte nicht geladen werden. [{}]'.format(extension, error))

bot.run(TOKEN)
