import logging
import os

from discord.ext import commands

'''Logger設置'''
logger = logging.getLogger('discord')


class AdminCmd(commands.Cog):

    def __init__(self, client):
        self.client = client

    # 關閉Bot
    @commands.command()
    @commands.is_owner()
    async def bye(self, ctx):
        await ctx.send('掰掰~')
        await self.client.close()

    # 重新啟動Bot
    @commands.is_owner()
    @commands.command()
    async def restart(self, ctx):
        await ctx.send('重新啟動完成!')
        os.system(f"nohup python -W ignore {os.path.join('.', 'Bot', 'Chino.py')} &> Log.txt &")
        exit()


def setup(client):
    client.add_cog(AdminCmd(client))
