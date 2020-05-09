import discord
from discord.ext import commands

class roles():
    def __init__(self, bot):
        self.bot = bot

    @bot.command(pass_context=True)
    async def role(self, ctx, role: discord.Role):
        user = ctx.author
        if role.color == "#000000":
            await user.add_roles(role)
            await ctx.send(f"{user} has been giving a role called: {role.name}")
        else:
            await ctx.send("That is not a permitted role")



    @bot.command(pass_context=True)
    async def giverole(self, ctx, user: discord.Member, role: discord.Role):
        if (ctx.author.role.name == "Administrator"):
            await user.add_roles(role)
            await ctx.send(f"{ctx.author.name}, {user.name} has been giving a role called: {role.name}")
        else:
            await ctx.send("You are not admin and cannot give roles to people")


    @bot.command()
    async def listroles(self, ctx):
        roles = [r.name for r in ctx.guild.roles[1:]]
        if (len(roles) == 0):
            return await ctx.send("You do not have any roles setup on this server, other than the default role!")
        else:
            return await ctx.send(roles)


def setup(bot):
    bot.add_cog(roles(bot))
