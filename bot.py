import discord
from discord.ext import commands
TOKEN = ''
bot = commands.Bot(command_prefix= '.')

startup_extensions = ["roles"]

@bot.event
async def on_ready():
    print('Ready')

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

    bot.run(TOKEN)