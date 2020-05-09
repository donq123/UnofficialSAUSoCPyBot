import discord
from discord.ext import commands
TOKEN = 'NzA4NTA1MDkzNTU2OTI4NTUy.XrYU-A.DDh3sk9eRaKJXBirrvcGmN7uous'
bot = commands.Bot(command_prefix= '.')

startup_extensions = ["roles"]

@bot.event
async def on_ready():
    print('Ready')

@bot.command(pass_context=True)
async def role(ctx, role: discord.Role):
    user = ctx.author
    print(role.color)
    if role.color == discord.Color.default():
        await user.add_roles(role)
        await ctx.send(f"{user} has been giving a role called: {role.name}")
    else:
        await ctx.send("That is not a permitted role")

@bot.command(pass_context=True)
async def giverole(ctx, user: discord.Member, role: discord.Role):
    if (ctx.author.role.name == "Administrator"):
        await user.add_roles(role)
        await ctx.send(f"{ctx.author.name}, {user.name} has been giving a role called: {role.name}")
    else:
        await ctx.send("You are not admin and cannot give roles to people")

@bot.command()
async def listroles(ctx):
    roles = [r.name for r in ctx.guild.roles[1:]]
    if (len(roles) == 0):
        return await ctx.send("You do not have any roles setup on this server, other than the default role!")
    else:
        return await ctx.send(roles)

bot.run(TOKEN)